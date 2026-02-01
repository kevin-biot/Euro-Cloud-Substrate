# Evidence Catalog (Skeleton)

Evidence types should be tied to invariant IDs. This skeleton lists families with placeholders for future detail.

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
    "event_type": { "enum": ["object.put", "object.delete", "object.copy", "object.replicate", "object.lock", "object.unlock", "object.retention-update"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "object_id": { "type": "string" },
    "version_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "governance_metadata": {
      "$ref": "#/definitions/eosc-metadata"
    },
    "outcome": { "enum": ["success", "refusal"] },
    "refusal_reason": { "type": "string" }
  },
  "required": ["event_type", "timestamp", "object_id", "outcome"]
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
    "event_type": { "enum": ["ml.inference"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "workload_id": { "type": "string" },
    "model_id": { "type": "string" },
    "model_sbom_ref": { "type": "string" },
    "input_hash": { "type": "string" },
    "context_hash": { "type": "string" },
    "output_ref": { "type": "string" },
    "outcome": { "enum": ["success", "refusal"] },
    "refusal_reason": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["event_type", "timestamp", "workload_id", "model_id", "input_hash", "outcome"]
}
```

- Evidence events for ML training (EVID/SUP/EXEC example):
```json
{
  "type": "object",
  "properties": {
    "event_type": { "enum": ["ml.training.start", "ml.training.checkpoint", "ml.training.complete"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "training_run_id": { "type": "string" },
    "model_id": { "type": "string" },
    "dataset_refs": { "type": "array", "items": { "type": "string" } },
    "code_version": { "type": "string" },
    "hyperparameters_hash": { "type": "string" },
    "checkpoint_hash": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "outcome": { "enum": ["success", "failure", "aborted"] }
  },
  "required": ["event_type", "timestamp", "training_run_id", "model_id", "outcome"]
}
```

- Evidence events for OLZ bootstrap (EVID/AUTH/POL/DATA example):
```json
{
  "type": "object",
  "properties": {
    "event_type": { "enum": ["olz.bootstrap"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "authority_binding": { "type": "string" },
    "policy_baseline": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification_ceiling": { "type": "string" },
    "network_namespace_id": { "type": "string" },
    "initial_quotas": { "type": "object" },
    "outcome": { "enum": ["success", "refusal"] },
    "refusal_reason": { "type": "string" }
  },
  "required": ["event_type", "timestamp", "tenant_id", "authority_binding", "policy_baseline", "jurisdiction", "outcome"]
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
