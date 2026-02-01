# WS2 Spec (Draft)

## Objectives
- Define EOSC API expectations and governance semantics.

## Invariant families (refs)
- DATA (residency, metadata)
- EVID (evidence pointers, integrity)
- SUP (inventory, provenance)
- INT/EXIT (portability)

## Sections to draft
- API surface and compatibility expectations.
- Metadata contract (jurisdiction, retention/TTL, evidence pointers, integrity hashes).
- Immutability and retention behaviors.
- Audit/evidence integration and export.

## Draft requirements (pass 1)

### API surface (S3-compatible subset)
- Required operations: PUT, GET, DELETE, LIST, multipart upload, versioning, object lock/immutability.
- Optional/clarify: presigned URLs (if supported, must enforce metadata requirements).
- Error semantics: explicit, deterministic errors when governance metadata is missing/invalid.

### Governance metadata schema
- Fields (required on write):
  - `x-eosc-jurisdiction`: ISO country/region code for residency.
  - `x-eosc-retention-ttl`: retention period or expiration timestamp.
  - `x-eosc-integrity`: hash algorithm and hash (e.g., sha256:<value>).
  - `x-eosc-classification`: data classification (controlled vocabulary TBD).
  - `x-eosc-evidence-pointer`: reference to audit/evidence record(s) for governed objects/ops.
- Format: conveyed via request headers (or canonical user metadata keys if headers unavailable); must be persisted with the object and preserved on copy/move/replication.
- Validation: writes MUST fail if required fields are missing/invalid; copies must not strip/alter governance metadata.

### Immutability and retention
- Object lock/immutability MUST be supported for governed objects; delete/overwrite refused when lock active.
- Retention timers and legal holds MUST be enforced; changes must emit evidence events.

### Jurisdiction enforcement
- Placement MUST honor `x-eosc-jurisdiction`; cross-border replication MUST be blocked unless explicitly allowed and evidenced.
- Portable metadata: governance metadata MUST travel with the object across providers/regions.

### Integrity
- On write: validate declared hash; store hash metadata.
- On read (configurable): option to validate stored hash; failures emit evidence and can trigger refusal.

### Evidence and audit
- Operations generating evidence events: PUT, DELETE, COPY/MOVE/REPLICATION, LOCK/UNLOCK, retention changes, metadata updates.
- Evidence events MUST include: authority/policy snapshot IDs, object identifier/version, governance metadata values, integrity info, outcome (success/refusal).
- Audit/export: provide a standard export of evidence/audit related to objects (aligned with WS5).

### Conformance outline (pass 1)
- Writes without required governance metadata fail.
- Governance metadata is preserved across copy/move/replication.
- Jurisdiction enforcement blocks placement outside declared boundary unless explicitly allowed.
- Integrity hash validated on write; optional on read; failures produce evidence/refusal as configured.
- Immutability/retention behaviors enforced; related actions emit evidence.
- Evidence is generated for governed operations with required context fields.
