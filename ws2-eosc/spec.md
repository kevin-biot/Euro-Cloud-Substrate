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
  - `x-eosc-jurisdiction`: ISO 3166 country/region code for residency (string).
  - `x-eosc-retention-ttl`: ISO 8601 duration or RFC 3339 timestamp for expiry/retention (string).
  - `x-eosc-integrity`: algorithm:value (e.g., `sha256:<hex>`) (string).
  - `x-eosc-classification`: controlled vocabulary (e.g., `public|internal|restricted|secret`) (string).
  - `x-eosc-evidence-pointer`: URI to evidence/audit record(s) (e.g., `eosc://evidence/<id>` or https URL) (string).
- Format: conveyed via request headers (or canonical user metadata keys if headers unavailable); must be persisted with the object and preserved on copy/move/replication.
- Validation: writes MUST fail if required fields are missing/invalid; copies must not strip/alter governance metadata.

### Metadata field definitions (pass 2)
- Types are strings; validation rules:
  - `x-eosc-jurisdiction`: must be valid ISO code; provider enforces placement accordingly.
  - `x-eosc-retention-ttl`: must parse as ISO 8601 duration (e.g., `P30D`) or RFC 3339 timestamp; provider enforces retention/expiry.
  - `x-eosc-integrity`: must specify supported hash algo (e.g., sha256, sha512); value must match computed hash on write.
  - `x-eosc-classification`: must be from declared vocabulary published by provider; vocabulary must be documented.
  - `x-eosc-evidence-pointer`: must be a resolvable URI within provider’s evidence/audit system; clients may store multiple pointers via repeat header/user-metadata if needed.

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
