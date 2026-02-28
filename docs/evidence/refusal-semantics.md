# Refusal Semantics (Quick Spec, Draft)

## Purpose
Define what a governed refusal must look like in ECS evidence so refusals are auditable, portable, and independently verifiable.

Refusals are first-class outcomes. Silent denial, ambiguous errors, or unanchored `403` responses are non-conformant.

## Minimal refusal event shape
```json
{
  "id": "evt-refuse-001",
  "event_type": "policy.evaluate",
  "occurred_at": "2025-01-01T00:00:00Z",
  "tenant_id": "tenant-123",
  "sequence": 101,
  "outcome": "refused",
  "correlation_id": "corr-123",
  "policy_snapshot_id": "pol-2026-02",
  "authority_snapshot_id": "auth-2026-01",
  "refusal_reason_class": "policy_denied",
  "refusal_reason_code": "missing_required_snapshot",
  "refusal_subject": "workload.deploy",
  "evidence_pointer": "eosc://evidence/sha256:...",
  "chain_id": "chain-001",
  "prev_hash": "sha256:...",
  "event_hash": "sha256:..."
}
```

## Required fields
- Envelope: `id`, `event_type`, `occurred_at`, `tenant_id`, `sequence`, `outcome`, `evidence_pointer`.
- Refusal anchors: `correlation_id`, `policy_snapshot_id`, `authority_snapshot_id`.
- Refusal classification: `refusal_reason_class`, `refusal_reason_code`, `refusal_subject`.
- Integrity (for admissible/stronger profiles): `chain_id`, `event_hash`, `prev_hash`.

## Refusal reason classes (baseline set)
- `policy_denied` - policy explicitly denies action.
- `authority_missing_or_invalid` - no valid authority context.
- `jurisdiction_denied` - route/placement violates jurisdiction policy.
- `delegation_invalid` - missing, expired, revoked, or out-of-scope delegation.
- `evidence_precondition_failed` - required evidence/precondition not present.
- `dependency_unavailable_fail_closed` - critical dependency unavailable under fail-closed policy.

## Verifier checks
An independent verifier should be able to:
1. Confirm `outcome=refused` and refusal fields are present.
2. Resolve `policy_snapshot_id` and `authority_snapshot_id` references.
3. Validate refusal reason class/code is consistent with referenced snapshots.
4. Validate integrity continuity (`prev_hash` -> `event_hash`) where required.
5. Confirm refusal event correlates to request/decision context via `correlation_id`.

## Anti-patterns (do not use)
- Silent fail with no evidence event.
- Generic HTTP `403` with no policy/authority anchor.
- Refusal event with no `correlation_id`.
- Refusal reason text only, with no machine-classified reason fields.
- Refusal emitted outside chain or without retrievable evidence pointer.

## Implementation notes
- HTTP/API responses may return `403`, but a refusal event with ECS fields is still required.
- Refusal evidence should be emitted at the decision point, not reconstructed later.
- Refusals should be included in export bundles under the selected profile.
