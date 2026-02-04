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

## Interfaces (draft)
- Query API: time range, tenant, event_type, outcome, correlation_id, sequence range.
- Export API: export by time range or sequence range; include manifest, events, artifacts, verifier inputs.
- Verifier inputs SHOULD include chain_id, from_sequence, to_sequence, and anchor references when used.
