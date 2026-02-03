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
  - On metadata failure: 400-style error with reason (missing/invalid field) and a machine-parsable code.
  - Baseline error codes (examples): `EOSC_MISSING_JURISDICTION`, `EOSC_INVALID_RETENTION_FORMAT`, `EOSC_INTEGRITY_MISMATCH`, `EOSC_CLASSIFICATION_UNKNOWN`, `EOSC_JURISDICTION_BLOCKED`.

### Governance metadata schema
- Fields (required on write):
  - `x-eosc-jurisdiction`: ISO 3166 country/region code for residency (string).
  - `x-eosc-retention-ttl`: ISO 8601 duration or RFC 3339 timestamp for expiry/retention (string).
  - `x-eosc-integrity`: algorithm:value (e.g., `sha256:<hex>`) (string).
  - `x-eosc-classification`: controlled vocabulary (e.g., `public|internal|restricted|secret`) (string).
  - `x-eosc-evidence-pointer`: URI to evidence/audit record(s) (e.g., `eosc://evidence/<id>` or https URL) (string).
  - `x-eosc-data-product-id`: data product identifier for governed sharing (string).
  - `x-eosc-usage-policy-snapshot-id`: policy snapshot governing access (string).
  - `x-eosc-consent-token-ref`: consent/intent token reference (string).
- Format: conveyed via request headers (or canonical user metadata keys if headers unavailable); must be persisted with the object and preserved on copy/move/replication.
- Validation: writes MUST fail if required fields are missing/invalid; copies must not strip/alter governance metadata.

### Metadata field definitions (pass 2)
- Types are strings; validation rules:
  - `x-eosc-jurisdiction`: must be valid ISO code; provider enforces placement accordingly. Special values MAY include `EU`, `EEA`, or a comma-separated list of allowed jurisdictions (e.g., `DE,FR`); provider must document supported values.
  - `x-eosc-retention-ttl`: must parse as ISO 8601 duration (e.g., `P30D`) or RFC 3339 timestamp; provider enforces retention/expiry. If parseable as RFC 3339, treat as absolute; otherwise parse as duration.
  - `x-eosc-integrity`: must specify supported hash algo; providers MUST support `sha256`; MAY support `sha384`, `sha512`, `sha3-256`; MUST reject `md5`, `sha1`. Value must match computed hash on write.
  - `x-eosc-classification`: must be from declared vocabulary published by provider; vocabulary must be documented.
  - `x-eosc-evidence-pointer`: must be a resolvable URI within provider’s evidence/audit system; clients may store multiple pointers via repeat header/user-metadata if needed.

### Metadata schema example (JSON)
```json
{
  "x-eosc-jurisdiction": "FR",
  "x-eosc-retention-ttl": "P30D",
  "x-eosc-integrity": "sha256:abcd1234...",
  "x-eosc-classification": "restricted",
  "x-eosc-evidence-pointer": "eosc://evidence/123e4567",
  "x-eosc-data-product-id": "dp-001",
  "x-eosc-usage-policy-snapshot-id": "pol-001",
  "x-eosc-consent-token-ref": "consent-123"
}
```

### Example: PUT with required governance headers
```
PUT /bucket/object
x-eosc-jurisdiction: FR
x-eosc-retention-ttl: P30D
x-eosc-integrity: sha256:abcd1234...
x-eosc-classification: restricted
x-eosc-evidence-pointer: eosc://evidence/123e4567
Content-Length: ...
Content-Type: application/octet-stream
```

### Metadata schema (JSON Schema snippet)
```json
{
  "type": "object",
  "properties": {
    "x-eosc-jurisdiction": { "type": "string", "pattern": "^[A-Z]{2}$" },
    "x-eosc-retention-ttl": { "type": "string" },
    "x-eosc-integrity": { "type": "string", "pattern": "^[a-z0-9]+:[A-Fa-f0-9]+$" },
    "x-eosc-classification": { "type": "string" },
    "x-eosc-evidence-pointer": { "type": "string" },
    "x-eosc-data-product-id": { "type": "string" },
    "x-eosc-usage-policy-snapshot-id": { "type": "string" },
    "x-eosc-consent-token-ref": { "type": "string" }
  },
  "required": [
    "x-eosc-jurisdiction",
    "x-eosc-retention-ttl",
    "x-eosc-integrity",
    "x-eosc-classification",
    "x-eosc-evidence-pointer",
    "x-eosc-data-product-id",
    "x-eosc-usage-policy-snapshot-id",
    "x-eosc-consent-token-ref"
  ]
}
```

### Immutability and retention
- Object lock/immutability MUST be supported for governed objects; delete/overwrite refused when lock active.
- Retention timers and legal holds MUST be enforced; changes must emit evidence events.
- Example enforcement:
  - Attempt to delete/overwrite a locked object MUST fail with explicit error and evidence event.
  - Retention change requests MUST be logged with authority/policy context and evidence pointer.

### Jurisdiction enforcement
- Placement MUST honor `x-eosc-jurisdiction`; cross-border replication MUST be blocked unless explicitly allowed and evidenced.
- Portable metadata: governance metadata MUST travel with the object across providers/regions.
- Example enforcement:
  - Replication/copy to a non-permitted region MUST fail with explicit error and evidence.
  - Placement decisions MUST be auditable (evidence pointer with jurisdiction decision).

### Integrity
- On write: validate declared hash; store hash metadata.
- On read (configurable): option to validate stored hash; failures emit evidence and can trigger refusal.
- Example enforcement:
  - Write MUST fail if computed hash does not match `x-eosc-integrity`.
  - Optional read-verify mode produces evidence of validation or refusal on mismatch.

### Evidence and audit
- Operations generating evidence events: PUT, DELETE, COPY/MOVE/REPLICATION, LOCK/UNLOCK, retention changes, metadata updates.
- Evidence events MUST include: authority/policy snapshot IDs, object identifier/version, governance metadata values, integrity info, outcome (accepted/refused/failed).
- Data access events (GET/EXPORT) MUST emit evidence including data product id, policy snapshot id, consent token ref, and usage receipt reference when applicable.
- Audit/export: provide a standard export of evidence/audit related to objects (aligned with WS5) and `docs/evidence-export-schema.md`.

### Conformance outline (pass 1)
- Writes without required governance metadata fail.
- Governance metadata is preserved across copy/move/replication.
- Jurisdiction enforcement blocks placement outside declared boundary unless explicitly allowed.
- Integrity hash validated on write; optional on read; failures produce evidence/refusal as configured.
- Immutability/retention behaviors enforced; related actions emit evidence.
- Evidence is generated for governed operations with required context fields, including usage receipts where applicable.
