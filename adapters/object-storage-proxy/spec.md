# ECS Object Storage Proxy Adapter (Draft Spec)

## 1. Overview
- **Adapter name:** Object Storage Proxy
- **Target system:** S3‑compatible storage (S3/Swift/MinIO/Ceph)
- **Purpose:** Emit verifiable evidence for object operations and governance metadata.
- **Scope:** Proxies basic HTTP operations and emits Core10‑05 events; does not implement S3 auth/signing.

## 2. ECS alignment
- **Core10 references:** Core10‑03 (EOSC), Core10‑05 (Evidence Event Model)
- **Invariant families:** DATA, EVID, AUTH, POL
- **Evidence profiles:** baseline; admissible where required

## 3. Inputs
Required:
- `policy_snapshot_id`
- `authority_snapshot_id`

Optional:
- `correlation_id`
- `jurisdiction`, `classification`, `retention`
- `hash_profile_id`

## 4. Evidence emission
### Event types
- `object.get`
- `object.put`
- `object.delete`

### Required fields
- Core10‑05 envelope fields
- `object_id`, `bucket`, `key`
- `policy_snapshot_id`, `authority_snapshot_id`

### Refusal semantics
- Refuse if required snapshot ids are missing (fail‑closed).
- Emit refusal evidence with `refusal_reason`.

## 5. Export behavior
- Evidence bundles as per `docs/evidence/export-schema.md`.
- Chain integrity with `chain_id`, `event_hash`, `prev_hash`.

## 6. Security & trust
- Authn/z expected at the upstream storage layer or via fronting gateway.
- Trust roots are referenced via authority snapshots.

## 7. Deployment & ops
- Runs as a local proxy in front of storage endpoints.
- Failure modes: fail‑closed for governed requests.

## 8. Minimal examples
### Evidence event
```json
{
  "event_type": "object.put",
  "occurred_at": "2026-02-05T12:00:00Z",
  "tenant_id": "tenant-123",
  "sequence": 910,
  "outcome": "accepted",
  "object_id": "bucket/key.txt",
  "bucket": "bucket",
  "key": "key.txt",
  "policy_snapshot_id": "pol-2026-02",
  "authority_snapshot_id": "auth-2026-01",
  "evidence_pointer": "eosc://evidence/sha256:..."
}
```

## 9. Conformance checklist
- Emits Core10‑05 envelope.
- Declares evidence profile.
- Emits refusal evidence when snapshots are missing.
- Exports evidence bundles with chain integrity.

## 10. Non‑goals
- Does not implement signature v4 or storage auth.
- Does not provide lifecycle rules or replication management.
