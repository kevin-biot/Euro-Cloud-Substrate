import argparse
import hashlib
import json
import os
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional, Tuple
from urllib.parse import urlsplit
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


def resolve_snapshot_ids(headers) -> Tuple[str, str]:
    policy_snapshot_id = resolve_header(headers, "X-ECS-Policy-Snapshot") or "pol-default"
    authority_snapshot_id = resolve_header(headers, "X-ECS-Authority-Snapshot") or "auth-default"
    return policy_snapshot_id, authority_snapshot_id


def resolve_correlation_id(headers) -> str:
    return resolve_header(headers, "X-ECS-Correlation-Id") or f"corr-{uuid.uuid4().hex[:12]}"


def resolve_governance(headers) -> dict:
    out = {}
    jurisdiction = resolve_header(headers, "X-ECS-Jurisdiction")
    classification = resolve_header(headers, "X-ECS-Classification")
    retention = resolve_header(headers, "X-ECS-Retention")
    if jurisdiction:
        out["jurisdiction"] = jurisdiction
    if classification:
        out["classification"] = classification
    if retention:
        out["retention"] = retention
    return out


def parse_object_path(path: str) -> Tuple[str, str, str]:
    split = urlsplit(path)
    raw = split.path.lstrip("/")
    if not raw:
        return "", "", ""
    parts = raw.split("/", 1)
    bucket = parts[0]
    key = parts[1] if len(parts) > 1 else ""
    return raw, bucket, key


def map_event_type(method: str) -> str:
    if method in ("GET", "HEAD"):
        return "object.get"
    if method in ("PUT", "POST"):
        return "object.put"
    if method == "DELETE":
        return "object.delete"
    return "object.request"


def outcome_from_status(status: int) -> Tuple[str, Optional[str]]:
    if status < 400:
        return "accepted", None
    if status in (401, 403):
        return "refused", f"http_{status}"
    return "failed", f"http_{status}"


class ProxyHandler(BaseHTTPRequestHandler):
    def _write_json(self, status: int, payload: dict) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def _forward(self, method: str, body: bytes) -> Tuple[int, dict, bytes]:
        upstream = self.server.upstream.rstrip("/") + self.path
        req = Request(upstream, data=body if method not in ("GET", "HEAD") else None, method=method)
        for key, value in self.headers.items():
            if key.lower() in ("host", "content-length"):
                continue
            req.add_header(key, value)
        try:
            with urlopen(req, timeout=self.server.timeout) as resp:
                return resp.status, dict(resp.headers), resp.read()
        except HTTPError as err:
            return err.code, dict(err.headers), err.read()
        except URLError:
            return 502, {}, b""

    def _handle(self, method: str) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""

        evidence_profile_id = resolve_profile(self.headers)
        hash_profile_id = resolve_hash_profile(self.headers, evidence_profile_id)
        policy_snapshot_id, authority_snapshot_id = resolve_snapshot_ids(self.headers)
        correlation_id = resolve_correlation_id(self.headers)
        governance = resolve_governance(self.headers)

        object_id, bucket, key = parse_object_path(self.path)
        event_type = map_event_type(method)

        # Ensure artifacts exist for policy/authority snapshots.
        self.server.store.ensure_artifact(
            "policy_snapshots",
            policy_snapshot_id,
            {"id": policy_snapshot_id, "version": "1.0", "rules": []},
        )
        self.server.store.ensure_artifact(
            "authority_bindings",
            authority_snapshot_id,
            {"id": authority_snapshot_id, "subject": bucket or "unknown", "scope": ["object.*"]},
        )

        missing = []
        if policy_snapshot_id == "pol-default":
            missing.append("policy_snapshot_id")
        if authority_snapshot_id == "auth-default":
            missing.append("authority_snapshot_id")

        if missing and self.server.fail_closed:
            payload = {
                "object_id": object_id,
                "bucket": bucket,
                "key": key,
                "policy_snapshot_id": policy_snapshot_id,
                "authority_snapshot_id": authority_snapshot_id,
                "correlation_id": correlation_id,
                "refusal_reason": "missing_required_snapshot",
                **governance,
            }
            self.server.store.emit_event(
                event_type,
                payload,
                evidence_profile_id,
                hash_profile_id=hash_profile_id,
                outcome="refused",
            )
            self._write_json(403, {"error": "missing_required_snapshot", "missing": missing})
            return

        status, resp_headers, resp_body = self._forward(method, body)
        outcome, refusal_reason = outcome_from_status(status)

        payload = {
            "object_id": object_id,
            "bucket": bucket,
            "key": key,
            "policy_snapshot_id": policy_snapshot_id,
            "authority_snapshot_id": authority_snapshot_id,
            "correlation_id": correlation_id,
            **governance,
        }

        if body and method in ("PUT", "POST"):
            payload["content_hash"] = f"sha256:{sha256_hex(body)}"

        if refusal_reason:
            payload["refusal_reason"] = refusal_reason

        self.server.store.emit_event(
            event_type,
            payload,
            evidence_profile_id,
            hash_profile_id=hash_profile_id,
            outcome=outcome,
        )

        self.send_response(status)
        if "Content-Type" in resp_headers:
            self.send_header("Content-Type", resp_headers["Content-Type"])
        if "ETag" in resp_headers:
            self.send_header("ETag", resp_headers["ETag"])
        if "Last-Modified" in resp_headers:
            self.send_header("Last-Modified", resp_headers["Last-Modified"])
        self.end_headers()
        if resp_body:
            self.wfile.write(resp_body)

    def do_GET(self):
        self._handle("GET")

    def do_HEAD(self):
        self._handle("HEAD")

    def do_PUT(self):
        self._handle("PUT")

    def do_POST(self):
        self._handle("POST")

    def do_DELETE(self):
        self._handle("DELETE")



def main():
    parser = argparse.ArgumentParser(description="ECS object storage proxy (reference)")
    parser.add_argument("--listen", default="0.0.0.0", help="Listen address")
    parser.add_argument("--port", type=int, default=8082, help="Listen port")
    parser.add_argument("--store", default=os.getenv("ECS_EVIDENCE_STORE", "./evidence-store"), help="Evidence store path")
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help="Default evidence profile")
    parser.add_argument("--provider", default="provider-A", help="Provider id")
    parser.add_argument("--tenant", default="tenant-123", help="Tenant id")
    parser.add_argument("--upstream", default=os.getenv("ECS_UPSTREAM_URL"), help="Upstream S3/Swift endpoint")
    parser.add_argument("--timeout", type=int, default=30, help="Upstream timeout seconds")
    parser.add_argument("--fail-closed", action="store_true", help="Fail closed on missing snapshots")
    args = parser.parse_args()

    store = EvidenceStore(args.store, provider_id=args.provider, tenant_id=args.tenant)
    server = HTTPServer((args.listen, args.port), ProxyHandler)
    server.store = store
    server.default_profile = args.profile
    server.upstream = args.upstream
    server.timeout = args.timeout
    server.fail_closed = args.fail_closed or os.getenv("ECS_FAIL_CLOSED", "true").lower() == "true"

    if not server.upstream:
        raise SystemExit("Upstream endpoint is required. Set --upstream or ECS_UPSTREAM_URL.")

    print(f"ECS object storage proxy listening on {args.listen}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
