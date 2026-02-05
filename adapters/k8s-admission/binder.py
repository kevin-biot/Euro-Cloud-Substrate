import argparse
import base64
import json
import os
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional, Tuple

from evidence import EvidenceStore

DEFAULT_PROFILE = "ecs-evidence-baseline"
DEFAULT_HASH_PROFILE = "ecs-hash-v1"


def get_annotation(meta: dict, key: str) -> Optional[str]:
    return (meta.get("annotations") or {}).get(key)


def get_label(meta: dict, key: str) -> Optional[str]:
    return (meta.get("labels") or {}).get(key)


def resolve_profile(meta: dict, default_profile: str) -> str:
    return (
        get_annotation(meta, "ecs.evidence/profile")
        or get_label(meta, "ecs.evidence/profile")
        or os.getenv("ECS_EVIDENCE_PROFILE")
        or default_profile
    )


def resolve_hash_profile(meta: dict, evidence_profile_id: str) -> Optional[str]:
    explicit = get_annotation(meta, "ecs.hash/profile") or get_label(meta, "ecs.hash/profile")
    if explicit:
        return explicit
    env_hash = os.getenv("ECS_HASH_PROFILE")
    if env_hash:
        return env_hash
    if "regulated-ml" in evidence_profile_id:
        return DEFAULT_HASH_PROFILE
    return None


def resolve_snapshot_ids(meta: dict) -> Tuple[str, str]:
    policy_snapshot_id = get_annotation(meta, "ecs.policy/snapshot") or "pol-default"
    authority_snapshot_id = get_annotation(meta, "ecs.authority/snapshot") or "auth-default"
    return policy_snapshot_id, authority_snapshot_id


def resolve_correlation_id(meta: dict) -> str:
    return get_annotation(meta, "ecs.evidence/correlation_id") or f"corr-{uuid.uuid4().hex[:12]}"


def should_deny(meta: dict) -> bool:
    return get_annotation(meta, "ecs.policy/deny") == "true"


def build_patch(meta: dict, profile_id: str, hash_profile_id: Optional[str], correlation_id: str,
                policy_snapshot_id: str, authority_snapshot_id: str) -> str:
    annotations = meta.get("annotations") or {}
    patch_ops = []
    def set_annotation(key: str, value: str):
        if key in annotations:
            return
        patch_ops.append({"op": "add", "path": f"/metadata/annotations/{key.replace('/', '~1')}", "value": value})

    set_annotation("ecs.evidence/profile", profile_id)
    if hash_profile_id:
        set_annotation("ecs.hash/profile", hash_profile_id)
    set_annotation("ecs.evidence/correlation_id", correlation_id)
    set_annotation("ecs.policy/snapshot", policy_snapshot_id)
    set_annotation("ecs.authority/snapshot", authority_snapshot_id)

    if not patch_ops:
        return ""
    return base64.b64encode(json.dumps(patch_ops).encode("utf-8")).decode("utf-8")


class AdmissionHandler(BaseHTTPRequestHandler):
    def _write_response(self, response: dict, code: int = 200) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def _error_response(self, uid: str, message: str, code: int = 400) -> dict:
        return {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": uid,
                "allowed": False,
                "status": {"code": code, "message": message},
            },
        }

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        try:
            review = json.loads(body)
        except json.JSONDecodeError:
            response = self._error_response("", "Invalid JSON", 400)
            self._write_response(response, 400)
            return

        req = review.get("request", {})
        uid = req.get("uid", "")
        obj = req.get("object", {})
        meta = obj.get("metadata", {})

        if not uid:
            response = self._error_response("", "Missing request.uid", 400)
            self._write_response(response, 400)
            return

        evidence_profile_id = resolve_profile(meta, self.server.default_profile)
        hash_profile_id = resolve_hash_profile(meta, evidence_profile_id)
        policy_snapshot_id, authority_snapshot_id = resolve_snapshot_ids(meta)
        correlation_id = resolve_correlation_id(meta)

        # Ensure artifacts exist for policy/authority snapshots.
        self.server.store.ensure_artifact("policy_snapshots", policy_snapshot_id, {
            "id": policy_snapshot_id,
            "version": "1.0",
            "rules": []
        })
        self.server.store.ensure_artifact("authority_bindings", authority_snapshot_id, {
            "id": authority_snapshot_id,
            "subject": meta.get("namespace", "default"),
            "scope": ["workload.deploy"]
        })

        # Emit policy evaluation
        self.server.store.emit_event(
            "policy.evaluate",
            {
                "policy_snapshot_id": policy_snapshot_id,
                "authority_snapshot_id": authority_snapshot_id,
                "correlation_id": correlation_id,
                "action": "workload.deploy"
            },
            evidence_profile_id,
            hash_profile_id=hash_profile_id,
            outcome="accepted"
        )

        allowed = not should_deny(meta)
        exec_event = "execution.admit" if allowed else "execution.refuse"
        outcome = "accepted" if allowed else "refused"

        self.server.store.emit_event(
            exec_event,
            {
                "workload_id": meta.get("name", "workload"),
                "envelope_type": "container",
                "policy_snapshot_id": policy_snapshot_id,
                "authority_snapshot_id": authority_snapshot_id,
                "correlation_id": correlation_id,
            },
            evidence_profile_id,
            hash_profile_id=hash_profile_id,
            outcome=outcome
        )

        patch = build_patch(meta, evidence_profile_id, hash_profile_id, correlation_id,
                            policy_snapshot_id, authority_snapshot_id)
        response = {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": uid,
                "allowed": allowed,
            }
        }
        if patch:
            response["response"]["patchType"] = "JSONPatch"
            response["response"]["patch"] = patch
        if not allowed:
            response["response"]["status"] = {"code": 403, "message": "Denied by ecs.policy/deny"}

        self._write_response(response, 200)


def main():
    parser = argparse.ArgumentParser(description="ECS K8s admission binder (reference)")
    parser.add_argument("--listen", default="0.0.0.0", help="Listen address")
    parser.add_argument("--port", type=int, default=8080, help="Listen port")
    parser.add_argument("--store", default=os.getenv("ECS_EVIDENCE_STORE", "./evidence-store"), help="Evidence store path")
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help="Default evidence profile")
    parser.add_argument("--provider", default="provider-A", help="Provider id")
    parser.add_argument("--tenant", default="tenant-123", help="Tenant id")
    args = parser.parse_args()

    store = EvidenceStore(args.store, provider_id=args.provider, tenant_id=args.tenant)
    server = HTTPServer((args.listen, args.port), AdmissionHandler)
    server.store = store
    server.default_profile = args.profile
    print(f"ECS admission binder listening on {args.listen}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
