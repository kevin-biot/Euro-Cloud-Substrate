import base64
import hashlib
import json
import os
import uuid
from datetime import datetime, timezone
from typing import Optional


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class EvidenceStore:
    def __init__(self, root: str, provider_id: str, tenant_id: str, chain_id: Optional[str] = None):
        self.root = root
        self.provider_id = provider_id
        self.tenant_id = tenant_id
        self.events_path = os.path.join(root, "events.jsonl")
        self.artifacts_dir = os.path.join(root, "artifacts")
        self.meta_path = os.path.join(root, "meta.json")
        self.index_path = os.path.join(root, "artifact-index.json")
        ensure_dir(self.root)
        ensure_dir(self.artifacts_dir)
        self.chain_id = chain_id or self._load_chain_id() or f"chain-{uuid.uuid4().hex[:8]}"
        self._save_meta()

    def _load_chain_id(self) -> Optional[str]:
        if not os.path.exists(self.meta_path):
            return None
        with open(self.meta_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("chain_id")

    def _save_meta(self) -> None:
        with open(self.meta_path, "w", encoding="utf-8") as f:
            json.dump({"chain_id": self.chain_id}, f, indent=2)
            f.write("\n")

    def _load_last_event(self) -> Optional[dict]:
        if not os.path.exists(self.events_path):
            return None
        with open(self.events_path, "r", encoding="utf-8") as f:
            lines = [line for line in f.read().splitlines() if line.strip()]
        if not lines:
            return None
        return json.loads(lines[-1])

    def _record_artifact(self, kind: str, ref: str) -> None:
        index = {}
        if os.path.exists(self.index_path):
            with open(self.index_path, "r", encoding="utf-8") as f:
                index = json.load(f)
        refs = index.get(kind, [])
        if ref not in refs:
            refs.append(ref)
        index[kind] = refs
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2)
            f.write("\n")

    def ensure_artifact(self, kind: str, artifact_id: str, content: dict) -> str:
        filename = f"{kind}-{artifact_id}.json"
        path = os.path.join(self.artifacts_dir, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(content, f, indent=2, ensure_ascii=True)
                f.write("\n")
        with open(path, "rb") as f:
            h = sha256_hex(f.read())
        ref = f"eosc://artifact/sha256:{h}"
        self._record_artifact(kind, ref)
        return ref

    def _write_evidence_artifact(self, event_id: str, event_type: str, sequence: int, occurred_at: str, payload: dict) -> str:
        content = {
            "event_type": event_type,
            "sequence": sequence,
            "timestamp": occurred_at,
            "details": payload,
        }
        filename = f"evidence-{event_id}.json"
        path = os.path.join(self.artifacts_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2, ensure_ascii=True)
            f.write("\n")
        with open(path, "rb") as f:
            h = sha256_hex(f.read())
        ref = f"eosc://evidence/sha256:{h}"
        self._record_artifact("evidence_artifacts", f"eosc://artifact/sha256:{h}")
        return ref

    def emit_event(
        self,
        event_type: str,
        payload: dict,
        evidence_profile_id: str,
        hash_profile_id: Optional[str] = None,
        actor: str = "system",
        outcome: str = "accepted",
    ) -> dict:
        last_event = self._load_last_event()
        sequence = (last_event.get("sequence") if last_event else 0) + 1
        prev_hash = last_event.get("event_hash") if last_event else None
        event_id = f"evt-{uuid.uuid4().hex[:12]}"
        occurred_at = utc_now()

        event = {
            "id": event_id,
            "event_type": event_type,
            "occurred_at": occurred_at,
            "tenant_id": self.tenant_id,
            "actor": actor,
            "evidence_profile_id": evidence_profile_id,
            "sequence": sequence,
            "outcome": outcome,
            "evidence_pointer": "",
            "chain_id": self.chain_id,
        }

        if hash_profile_id:
            event["hash_profile_id"] = hash_profile_id

        event.update(payload)
        if prev_hash:
            event["prev_hash"] = prev_hash

        evidence_pointer = self._write_evidence_artifact(event_id, event_type, sequence, occurred_at, payload)
        event["evidence_pointer"] = evidence_pointer

        # Compute event hash over canonical json without event_hash
        event_hash = sha256_hex(canonical_json(event).encode("utf-8"))
        event["event_hash"] = f"sha256:{event_hash}"

        with open(self.events_path, "a", encoding="utf-8") as f:
            f.write(canonical_json(event))
            f.write("\n")

        return event


def build_profile_claim(profile_id: str, hash_profile_id: Optional[str]) -> dict:
    return {
        "implements": {
            "evidence_profiles": [profile_id],
            "default_evidence_profile": profile_id,
            "hash_profiles": [hash_profile_id] if hash_profile_id else [],
            "export_endpoints": ["/v1/events", "/v1/exports"],
            "verifier_inputs_supported": ["chain_id", "prev_hash", "event_hash", "archive_ref"],
        }
    }


def write_profile_claim(path: str, profile_id: str, hash_profile_id: Optional[str]) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(build_profile_claim(profile_id, hash_profile_id), f, indent=2, ensure_ascii=True)
        f.write("\n")


def b64_json(obj: dict) -> str:
    return base64.b64encode(json.dumps(obj).encode("utf-8")).decode("utf-8")
