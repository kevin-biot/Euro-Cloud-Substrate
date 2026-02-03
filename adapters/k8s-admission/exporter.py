import argparse
import json
import os
from typing import Optional

from evidence import canonical_json, ensure_dir, sha256_hex, write_profile_claim


def load_events(events_path: str) -> list[dict]:
    if not os.path.exists(events_path):
        return []
    with open(events_path, "r", encoding="utf-8") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    return [json.loads(line) for line in lines]


def load_artifact_index(index_path: str) -> dict:
    if not os.path.exists(index_path):
        return {}
    with open(index_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, obj: dict) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
        f.write("\n")


def export_bundle(store: str, out_dir: str, from_seq: int, to_seq: int,
                  evidence_profile_id: str, hash_profile_id: Optional[str],
                  provider_id: str, tenant_id: str, trust_services: Optional[dict]) -> None:
    events_path = os.path.join(store, "events.jsonl")
    events = [e for e in load_events(events_path) if from_seq <= e.get("sequence", 0) <= to_seq]
    if not events:
        raise SystemExit("No events found in the requested range")

    chain_id = events[0].get("chain_id", "chain-unknown")

    # Chain segment
    event_hashes = [e["event_hash"] for e in events]
    segment_hash = sha256_hex("\n".join(event_hashes).encode("utf-8"))
    chain_segment = {
        "segment_id": f"seg-{from_seq}-{to_seq}",
        "tenant_id": tenant_id,
        "evidence_profile_id": evidence_profile_id,
        "from_sequence": from_seq,
        "to_sequence": to_seq,
        "algorithm": "sha256",
        "events": [
            {
                "id": ev["id"],
                "sequence": ev["sequence"],
                "prev_hash": ev.get("prev_hash"),
                "event_hash": ev["event_hash"],
                "evidence_profile_id": evidence_profile_id,
                "event_ref": ev["evidence_pointer"],
            }
            for ev in events
        ],
        "segment_hash": f"sha256:{segment_hash}",
        "signature": "optional-signature",
    }
    chain_segment_path = os.path.join(out_dir, "chain-segment.json")
    write_json(chain_segment_path, chain_segment)
    with open(chain_segment_path, "rb") as f:
        chain_segment_hash = sha256_hex(f.read())
    chain_segment_ref = f"eosc://evidence/chain/sha256:{chain_segment_hash}"

    # Bundle hash (same as segment hash here)
    bundle_hash = f"sha256:{segment_hash}"

    # Artifacts
    index_path = os.path.join(store, "artifact-index.json")
    artifacts = load_artifact_index(index_path)
    evidence_artifacts = []
    for ev in events:
        ref = ev["evidence_pointer"].replace("eosc://evidence/", "eosc://artifact/")
        evidence_artifacts.append(ref)
    artifacts["evidence_artifacts"] = sorted(set(evidence_artifacts))

    manifest = {
        "schema_version": "1.0",
        "export_id": f"exp-{from_seq}-{to_seq}",
        "created_at": "2025-01-01T00:00:00Z",
        "provider_id": provider_id,
        "tenant_id": tenant_id,
        "evidence_profile_id": evidence_profile_id,
        "scope": {"from_sequence": from_seq, "to_sequence": to_seq},
        "chain_id": chain_id,
        "chain_segment_ref": chain_segment_ref,
        "bundle_hash": bundle_hash,
        "artifacts": artifacts,
        "signatures": [{"key_id": "key-001", "signature": "base64..."}],
    }
    if hash_profile_id:
        manifest["hash_profile_id"] = hash_profile_id
    if trust_services:
        manifest["trust_services"] = trust_services

    write_json(os.path.join(out_dir, "manifest.json"), manifest)

    # Events JSONL
    events_path_out = os.path.join(out_dir, "events.jsonl")
    ensure_dir(out_dir)
    with open(events_path_out, "w", encoding="utf-8") as f:
        for ev in events:
            f.write(canonical_json(ev))
            f.write("\n")

    # Verifier inputs
    verifier_inputs = {
        "evidence_profile_id": evidence_profile_id,
        "hash_profile_id": hash_profile_id,
        "chain_id": chain_id,
        "from_sequence": from_seq,
        "to_sequence": to_seq,
        "event_hash_method": "sha256(canonical_json(event) without event_hash)",
        "segment_hash_method": "sha256(newline-joined event_hash values)",
        "bundle_hash_method": "sha256(newline-joined event_hash values)",
        "chain_segment_ref": chain_segment_ref,
    }
    if trust_services:
        verifier_inputs["trust_services"] = trust_services
    write_json(os.path.join(out_dir, "verifier-inputs.json"), verifier_inputs)

    # Profile claim
    write_profile_claim(os.path.join(out_dir, "profile-claim.json"), evidence_profile_id, hash_profile_id)


def main():
    parser = argparse.ArgumentParser(description="ECS evidence bundle exporter (reference)")
    parser.add_argument("--store", default="./evidence-store", help="Evidence store path")
    parser.add_argument("--out", default="./bundle", help="Output directory")
    parser.add_argument("--from-seq", type=int, required=True, help="Start sequence (inclusive)")
    parser.add_argument("--to-seq", type=int, required=True, help="End sequence (inclusive)")
    parser.add_argument("--profile", required=True, help="Evidence profile id")
    parser.add_argument("--hash-profile", default=None, help="Hash profile id (optional)")
    parser.add_argument("--provider", default="provider-A", help="Provider id")
    parser.add_argument("--tenant", default="tenant-123", help="Tenant id")
    parser.add_argument("--trust-services", default=None, help="JSON trust_services object")
    args = parser.parse_args()

    trust_services = json.loads(args.trust_services) if args.trust_services else None
    export_bundle(
        store=args.store,
        out_dir=args.out,
        from_seq=args.from_seq,
        to_seq=args.to_seq,
        evidence_profile_id=args.profile,
        hash_profile_id=args.hash_profile,
        provider_id=args.provider,
        tenant_id=args.tenant,
        trust_services=trust_services,
    )


if __name__ == "__main__":
    main()
