# Evidence Catalog (Skeleton)

Evidence types should be tied to invariant IDs. This skeleton lists families with placeholders for future detail.

All evidence events MUST conform to the Core10-05 envelope (id, occurred_at, sequence, outcome, tenant_id, evidence_pointer, correlation_id for governed actions) and export bundles MUST follow `docs/evidence-export-schema.md`.

## Base envelope (draft)
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "type": "string" },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "actor": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "outcome", "evidence_pointer"]
}
```

## AUTH
- Evidence types (tbd)

## POL
- Evidence types (tbd)

## EXEC
- Evidence types (tbd)

## DATA
- Evidence types (tbd)

## EVID
- Evidence events for storage (EVID/DATA/SUP example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["object.put", "object.delete", "object.copy", "object.replicate", "object.lock", "object.unlock", "object.retention-update"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "object_id": { "type": "string" },
    "version_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "governance_metadata": {
      "$ref": "#/definitions/eosc-metadata"
    },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "object_id", "outcome", "evidence_pointer"]
}
```

Definitions (snippet):
```json
{
  "definitions": {
    "eosc-metadata": {
      "type": "object",
      "properties": {
        "x-eosc-jurisdiction": { "type": "string" },
        "x-eosc-retention-ttl": { "type": "string" },
        "x-eosc-integrity": { "type": "string" },
        "x-eosc-classification": { "type": "string" },
        "x-eosc-evidence-pointer": { "type": "string" }
      },
      "required": [
        "x-eosc-jurisdiction",
        "x-eosc-retention-ttl",
        "x-eosc-integrity",
        "x-eosc-classification",
        "x-eosc-evidence-pointer"
      ]
    }
  }
}
```
- Evidence events for ML inference (EVID/SUP/EXEC example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["ml.inference"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "workload_id": { "type": "string" },
    "model_id": { "type": "string" },
    "model_sbom_ref": { "type": "string" },
    "input_hash": { "type": "string" },
    "context_hash": { "type": "string" },
    "output_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "workload_id", "model_id", "input_hash", "outcome", "evidence_pointer"]
}
```

- Evidence events for ML training (EVID/SUP/EXEC example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["ml.training.start", "ml.training.checkpoint", "ml.training.complete"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "training_run_id": { "type": "string" },
    "model_id": { "type": "string" },
    "dataset_refs": { "type": "array", "items": { "type": "string" } },
    "code_version": { "type": "string" },
    "hyperparameters_hash": { "type": "string" },
    "checkpoint_hash": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "training_run_id", "model_id", "outcome", "evidence_pointer"]
}
```

- Evidence events for OLZ bootstrap (EVID/AUTH/POL/DATA example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["olz.bootstrap"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "authority_binding": { "type": "string" },
    "policy_baseline": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification_ceiling": { "type": "string" },
    "network_namespace_id": { "type": "string" },
    "initial_quotas": { "type": "object" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "authority_binding", "policy_baseline", "jurisdiction", "outcome", "evidence_pointer"]
}
```

- Evidence artifacts for block storage (EVID/DATA example):
```json
{
  "type": "object",
  "properties": {
    "volume_id": { "type": "string" },
    "snapshot_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "integrity_hash": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["volume_id", "jurisdiction", "classification", "integrity_hash", "policy_snapshot_id", "evidence_pointer"]
}
```

- Evidence artifacts for file storage (EVID/DATA example):
```json
{
  "type": "object",
  "properties": {
    "share_id": { "type": "string" },
    "export_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "integrity_hash": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["share_id", "jurisdiction", "classification", "integrity_hash", "policy_snapshot_id", "evidence_pointer"]
}
```

- Evidence events for usage receipts (EVID/DATA example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["data.usage.receipt"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "data_product_id": { "type": "string" },
    "consumer_id": { "type": "string" },
    "purpose_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "consent_token_ref": { "type": "string" },
    "usage_quantity": { "type": "number" },
    "usage_unit": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "data_product_id", "consumer_id", "purpose_id", "policy_snapshot_id", "outcome", "evidence_pointer"]
}
```

## INT
- Evidence types (tbd)

## EXIT
- Evidence types (tbd)

## DEP
- Evidence types (tbd)

## SUP
- Evidence types (tbd)

## OPS
- Evidence types (tbd)

## PHY
- Evidence types (tbd)

## Tenant Isolation (EXEC/DATA/PHY/DEP)
- Evidence events for tenant isolation verification:
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["tenant.isolation.verify"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "target_tenant_id": { "type": "string" },
    "check_type": { "type": "string", "enum": ["network", "storage", "identity"] },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "check_type", "outcome", "evidence_pointer"]
}
```

## Execution Envelopes (EXEC/SUP/EVID/DEP)
- Evidence events for envelope lifecycle:
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["workload.envelope.create", "workload.envelope.start", "workload.envelope.stop", "workload.envelope.destroy"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "workload_id": { "type": "string" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "envelope_type": { "type": "string", "enum": ["container", "vm"] },
    "attestation_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "workload_id", "envelope_type", "outcome", "evidence_pointer"]
}
```

## Audit Chain (EVID)
- Evidence events for chain reconciliation/tamper detection:
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["chain.reconciliation"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "chain_id": { "type": "string" },
    "gap_detected": { "type": "boolean" },
    "tamper_detected": { "type": "boolean" },
    "details": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "chain_id", "outcome", "evidence_pointer"]
}
```

## Migration (EXIT/INT/DEP/SUP/EVID)
- Evidence events for migration:
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["migration.export", "migration.import"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "workload_id": { "type": "string" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "artifact_manifest_hash": { "type": "string" },
    "integrity_verified": { "type": "boolean" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "workload_id", "artifact_manifest_hash", "outcome", "evidence_pointer"]
}
```
