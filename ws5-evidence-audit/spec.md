# WS5 Spec (Draft)

## Objectives
- Define the evidence event model, audit chain, and query/export interfaces.

## Invariant families (refs)
- EVID (schema, integrity, completeness, reconciliation)
- AUTH/POL (context in evidence)
- DATA (where evidence resides)
- CRP ties: EVID-02/05 for partition buffering/reconciliation

## Terms (WS5 scope)
- **Core10-05 envelope**: Canonical evidence event envelope.
- **evidence profile**: Selected profile that defines additional integrity/chaining requirements.
- **evidence pointer**: Content‑addressed reference to artifacts (see pointer contract in `docs/evidence/export-schema.md`).
- **evidence export**: Manifest + event range + artifacts + verifier inputs.
- **evidence buffer**: Local, tamper‑evident store for evidence emitted during partitions.

## Sections to draft
- Event catalog and schemas.
- Hash chaining and integrity proofs.
- Query API and access control.
- Export formats for regulators/customers.
- CRP support: partition-tolerant buffering and reconciliation semantics.

## Requirements (draft v1)
- Evidence events MUST conform to Core10‑05.
- Export bundles MUST declare `evidence_profile_id` and include chain fields required by the selected profile.
- Evidence pointers MUST satisfy the pointer contract (immutability, tenant scoping, retrievability class).
- Audit queries MUST preserve ordering and integrity proofs.
- Partition‑tolerant buffering MUST preserve integrity and reconcile to the main chain post‑partition.

## Core event types (draft)
WS5 MUST support evidence events for:
- **Access events** (e.g., `object.get`, `object.put`, `queue.consume`) with outcome/refusal evidence.
- **Policy decisions** (e.g., `admission.decision`, `policy.evaluate`) with authority + policy snapshot ids.
- **Partition state changes** (e.g., `crp.partition.state`) with buffer/reconciliation indicators.

## Required fields (baseline)
Each evidence event MUST include:
- `id`, `event_type`, `occurred_at`, `tenant_id`, `sequence`, `outcome`, `evidence_pointer`
- `authority_snapshot_id` (authority version in force)
- `policy_snapshot_id` (policy version in force)

Evidence events SHOULD include:
- `correlation_id` (for governed action traceability)
- `ialp_context_ref` (links to IALP decision context/artifact)
- `chain_id`, `event_hash`, `prev_hash` (when required by profile)

Optional metadata MAY include:
- `actor_details`, `delegation_id`, `jurisdiction`, `classification`
- `refusal_reason` (when `outcome=refused`)

## Example events (IALP decision → evidence → audit chain)

Policy decision (accepted):
```json
{
  "id": "6d7f0f7a-31b8-4e44-8c88-3f7d5f4a0e11",
  "event_type": "admission.decision",
  "occurred_at": "2026-02-05T12:00:00Z",
  "tenant_id": "tenant-123",
  "sequence": 1201,
  "outcome": "accepted",
  "authority_snapshot_id": "auth-2026-01",
  "policy_snapshot_id": "pol-2026-02",
  "ialp_context_ref": "eosc://ialp/context/ctx-889",
  "chain_id": "chain-tenant-123",
  "event_hash": "sha256:...",
  "prev_hash": "sha256:...",
  "evidence_pointer": "eosc://evidence/events/6d7f0f7a.json"
}
```

Access event (refused):
```json
{
  "id": "f92f0f7e-0c0e-44a9-b04f-3e0b2e7a3c21",
  "event_type": "object.get",
  "occurred_at": "2026-02-05T12:00:05Z",
  "tenant_id": "tenant-123",
  "sequence": 1202,
  "outcome": "refused",
  "refusal_reason": "policy_denied",
  "authority_snapshot_id": "auth-2026-01",
  "policy_snapshot_id": "pol-2026-02",
  "correlation_id": "corr-771",
  "ialp_context_ref": "eosc://ialp/context/ctx-889",
  "chain_id": "chain-tenant-123",
  "event_hash": "sha256:...",
  "prev_hash": "sha256:...",
  "evidence_pointer": "eosc://evidence/events/f92f0f7e.json"
}
```

Partition state change (CRP buffering):
```json
{
  "id": "2b4b70b2-2a2a-4e6e-8f6f-9fb2b1a6f9b7",
  "event_type": "crp.partition.state",
  "occurred_at": "2026-02-05T12:01:00Z",
  "tenant_id": "tenant-123",
  "sequence": 1203,
  "outcome": "accepted",
  "authority_snapshot_id": "auth-2026-01",
  "policy_snapshot_id": "pol-2026-02",
  "partition_state": "partitioned",
  "buffer_mode": "local",
  "evidence_pointer": "eosc://evidence/events/2b4b70b2.json"
}
```

## Interfaces (draft)
- Query API: time range, tenant, event_type, outcome, correlation_id, sequence range.
- Export API: export by time range or sequence range; include manifest, events, artifacts, verifier inputs.
- Verifier inputs SHOULD include chain_id, from_sequence, to_sequence, and anchor references when used.
