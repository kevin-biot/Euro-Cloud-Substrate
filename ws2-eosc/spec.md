# WS2 Spec (Draft)

## Objectives
- Define EOSC API expectations and governance semantics.

## Invariant families (refs)
- DATA (residency, metadata)
- EVID (evidence pointers, integrity)
- SUP (inventory, provenance)
- INT/EXIT (portability)

## Terms (WS2 scope)
- **data_product_id**: Identifier for a governed data product used for sharing/usage accounting.
- **usage_policy_snapshot_id**: Policy snapshot governing access to the data product at decision time.
- **consent_token_ref**: Reference to an intent/consent token used in access decisions.
- **evidence_pointer**: Must conform to the evidence pointer contract in `docs/evidence/export-schema.md`.

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
  - `x-eosc-evidence-pointer`: URI to evidence/audit record(s) (e.g., `eosc://evidence/<id>` or https URL) (string, must satisfy evidence pointer contract).
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
- Audit/export: provide a standard export of evidence/audit related to objects (aligned with WS5) and `docs/evidence/export-schema.md`.
- Export bundles MUST declare `evidence_profile_id` and include chain fields where required by the selected profile.

### Non-object storage alignment (block/file) — draft
- Block and file storage are out of scope for EOSC as a strict object contract, but MUST align on governance metadata, evidence emission, and exportability.
- **Block storage (example requirements):**
  - Volume create/attach/detach/delete MUST emit evidence with policy snapshot id, authority binding, and classification.
  - Residency and classification MUST be enforced for volume placement.
  - Snapshot/export MUST include evidence pointers and integrity hashes.
- **File storage (example requirements):**
  - Mount and access controls MUST enforce tenant and policy bindings.
  - Governance metadata MUST be associated with file shares and preserved on export.
  - Access and export events MUST emit evidence with outcome and snapshot ids.

#### Block storage evidence events (draft JSON)
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["block.volume.create", "block.volume.attach", "block.volume.detach", "block.volume.snapshot", "block.volume.export"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "volume_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "volume_id", "outcome", "evidence_pointer"]
}
```

#### File storage evidence events (draft JSON)
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["file.share.create", "file.share.mount", "file.share.unmount", "file.share.export"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "share_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "share_id", "outcome", "evidence_pointer"]
}
```

#### Usage receipts for block/file (draft)
- Governed read/export operations SHOULD emit `data.usage.receipt` events with `data_product_id`, `purpose_id`, and `policy_snapshot_id`.
- Usage receipts SHOULD be included in evidence export bundles to support neutral usage attribution.

### Data services alignment (queues/streams) — draft
- Queues/streams are out of scope for EOSC as a strict object contract, but MUST align on governance metadata, policy enforcement, and evidence emission.
- Publish/subscribe/route decisions MUST be evidenced with policy/authority context.
- Sovereignty boundary routing MUST default‑deny unless explicitly authorized and evidenced.

### Backend mapping (non-normative)
- Ceph: RGW (object), RBD (block), CephFS (file); OpenShift Data Foundation wraps Ceph for ODF deployments.
- MinIO/SeaweedFS: object storage surfaces compatible with EOSC object contract.
- OpenEBS/Longhorn: block storage surfaces; evidence and metadata requirements apply via control-plane integration.
- NFS/Gluster: file storage surfaces; evidence and metadata requirements apply via gateway or policy layer.

### Conformance outline (pass 1)
- Writes without required governance metadata fail.
- Governance metadata is preserved across copy/move/replication.
- Jurisdiction enforcement blocks placement outside declared boundary unless explicitly allowed.
- Integrity hash validated on write; optional on read; failures produce evidence/refusal as configured.
- Immutability/retention behaviors enforced; related actions emit evidence.
- Evidence is generated for governed operations with required context fields, including usage receipts where applicable.
