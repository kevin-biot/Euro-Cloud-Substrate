import argparse
import hashlib
import json
import os
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from evidence import EvidenceStore

DEFAULT_PROFILE = "ecs-evidence-baseline"
DEFAULT_HASH_PROFILE = "ecs-hash-v1"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def resolve_header(headers, name: str) -> Optional[str]:
    value = headers.get(name)
    return value if value else None


def resolve_profile(headers) -> str:
    return (
        resolve_header(headers, "X-ECS-Evidence-Profile")
        or os.getenv("ECS_EVIDENCE_PROFILE")
        or DEFAULT_PROFILE
    )


def resolve_hash_profile(headers, evidence_profile_id: str) -> Optional[str]:
    explicit = resolve_header(headers, "X-ECS-Hash-Profile")
    if explicit:
        return explicit
    env_hash = os.getenv("ECS_HASH_PROFILE")
    if env_hash:
        return env_hash
    if "regulated-ml" in evidence_profile_id:
        return DEFAULT_HASH_PROFILE
    return None


def resolve_snapshot_ids(headers) -> tuple[str, str]:
    policy_snapshot_id = resolve_header(headers, "X-ECS-Policy-Snapshot") or "pol-default"
    authority_snapshot_id = resolve_header(headers, "X-ECS-Authority-Snapshot") or "auth-default"
    return policy_snapshot_id, authority_snapshot_id


def resolve_correlation_id(headers) -> str:
    return resolve_header(headers, "X-ECS-Correlation-Id") or f"corr-{uuid.uuid4().hex[:12]}"


def resolve_delegation_id(headers) -> Optional[str]:
    return resolve_header(headers, "X-ECS-Delegation-Id")


def resolve_model_id(headers) -> str:
    return resolve_header(headers, "X-ECS-Model-Id") or os.getenv("ECS_MODEL_ID", "model-default")


def resolve_model_sbom(headers) -> Optional[str]:
    return resolve_header(headers, "X-ECS-Model-SBOM") or os.getenv("ECS_MODEL_SBOM_REF")


def build_context_hash(headers, policy_snapshot_id: str, authority_snapshot_id: str, correlation_id: str) -> str:
    context = {
        "content_type": headers.get("Content-Type"),
        "policy_snapshot_id": policy_snapshot_id,
        "authority_snapshot_id": authority_snapshot_id,
        "correlation_id": correlation_id,
    }
    return f"sha256:{sha256_hex(json.dumps(context, sort_keys=True).encode('utf-8'))}"


class SidecarHandler(BaseHTTPRequestHandler):
    def _write_json(self, status: int, payload: dict) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def do_POST(self):
        if self.path not in ("/infer", "/v1/infer"):
            self._write_json(404, {"error": "not_found"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)

        evidence_profile_id = resolve_profile(self.headers)
        hash_profile_id = resolve_hash_profile(self.headers, evidence_profile_id)
        policy_snapshot_id, authority_snapshot_id = resolve_snapshot_ids(self.headers)
        correlation_id = resolve_correlation_id(self.headers)
        delegation_id = resolve_delegation_id(self.headers)
        model_id = resolve_model_id(self.headers)
        model_sbom_ref = resolve_model_sbom(self.headers)

        input_hash = f"sha256:{sha256_hex(body)}"
        context_hash = build_context_hash(self.headers, policy_snapshot_id, authority_snapshot_id, correlation_id)

        # Validate mandatory snapshots
        missing = []
        if policy_snapshot_id == "pol-default":
            missing.append("policy_snapshot_id")
        if authority_snapshot_id == "auth-default":
            missing.append("authority_snapshot_id")

        payload = {
            "model_id": model_id,
            "input_hash": input_hash,
            "context_hash": context_hash,
            "policy_snapshot_id": policy_snapshot_id,
            "authority_snapshot_id": authority_snapshot_id,
            "correlation_id": correlation_id,
        }
        if delegation_id:
            payload["delegation_id"] = delegation_id
        if model_sbom_ref:
            payload["model_sbom_ref"] = model_sbom_ref

        if missing:
            self.server.store.emit_event(
                "ml.inference",
                {**payload, "refusal_reason": "missing_required_snapshot"},
                evidence_profile_id,
                hash_profile_id=hash_profile_id,
                outcome="refused",
            )
            self._write_json(403, {"error": "missing_required_snapshot", "missing": missing})
            return

        if not self.server.upstream:
            self.server.store.emit_event(
                "ml.inference",
                {**payload, "refusal_reason": "upstream_unconfigured"},
                evidence_profile_id,
                hash_profile_id=hash_profile_id,
                outcome="failed",
            )
            self._write_json(503, {"error": "upstream_unconfigured"})
            return

        # Forward to upstream
        try:
            req = Request(self.server.upstream, data=body, method="POST")
            req.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))
            with urlopen(req, timeout=self.server.timeout) as resp:
                resp_body = resp.read()
                status = resp.status
        except HTTPError as err:
            status = err.code
            resp_body = err.read()
        except URLError:
            status = 502
            resp_body = b""

        outcome = "accepted" if status < 400 else "failed"
        output_hash = f"sha256:{sha256_hex(resp_body)}" if resp_body else None
        if output_hash:
            payload["output_ref"] = f"eosc://output/{output_hash}"

        self.server.store.emit_event(
            "ml.inference",
            payload,
            evidence_profile_id,
            hash_profile_id=hash_profile_id,
            outcome=outcome,
        )

        self.send_response(status)
        if resp_body:
            self.send_header("Content-Type", self.headers.get("Content-Type", "application/json"))
        self.end_headers()
        if resp_body:
            self.wfile.write(resp_body)


def main():
    parser = argparse.ArgumentParser(description="ECS ML inference sidecar (reference)")
    parser.add_argument("--listen", default="0.0.0.0", help="Listen address")
    parser.add_argument("--port", type=int, default=8081, help="Listen port")
    parser.add_argument("--store", default=os.getenv("ECS_EVIDENCE_STORE", "./evidence-store"), help="Evidence store path")
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help="Default evidence profile")
    parser.add_argument("--provider", default="provider-A", help="Provider id")
    parser.add_argument("--tenant", default="tenant-123", help="Tenant id")
    parser.add_argument("--upstream", default=os.getenv("ECS_UPSTREAM_URL"), help="Upstream inference URL")
    parser.add_argument("--timeout", type=int, default=30, help="Upstream timeout seconds")
    args = parser.parse_args()

    store = EvidenceStore(args.store, provider_id=args.provider, tenant_id=args.tenant)
    server = HTTPServer((args.listen, args.port), SidecarHandler)
    server.store = store
    server.default_profile = args.profile
    server.upstream = args.upstream
    server.timeout = args.timeout
    print(f"ECS ML inference sidecar listening on {args.listen}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
