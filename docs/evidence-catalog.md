# Evidence Catalog (Skeleton)

Evidence types should be tied to invariant IDs. This skeleton lists families with placeholders for future detail.

All evidence events MUST conform to the Core10-05 envelope (id, occurred_at, sequence, outcome, tenant_id, evidence_pointer, correlation_id for governed actions) and export bundles MUST follow `docs/evidence-export-schema.md`. Evidence bundles MAY include qualified timestamp/seal references in the export manifest to support legal admissibility.

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
    "actor_details": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "type": { "type": "string", "enum": ["human", "service", "delegate"] },
        "org_id": { "type": "string" },
        "credential_ref": { "type": "string" },
        "jurisdiction": { "type": "string" }
      }
    },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" },
    "chain_id": { "type": "string" },
    "event_hash": { "type": "string" },
    "prev_hash": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "outcome", "evidence_pointer"]
}
```

Evidence pointers are expected to be content‑addressed and tenant‑scoped; see `docs/evidence-export-schema.md` for pointer contract details.

## AUTH
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["authority.binding", "authority.refusal"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "authority_snapshot_id": { "type": "string" },
    "scope": { "type": "array", "items": { "type": "string" } },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "authority_snapshot_id", "outcome", "evidence_pointer"]
}
```

- Evidence events for wallet credential verification (AUTH example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["wallet.credential.verify"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "credential_id": { "type": "string" },
    "proof_type": { "type": "string", "enum": ["device_se", "esim", "token", "hsm", "other"] },
    "policy_snapshot_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "credential_id", "proof_type", "policy_snapshot_id", "outcome", "evidence_pointer"]
}
```

- Evidence events for delegated agent credentials (AUTH example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["wallet.delegation.issue", "wallet.delegation.revoke"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "delegation_id": { "type": "string" },
    "delegator_id": { "type": "string" },
    "delegate_id": { "type": "string" },
    "scope": { "type": "array", "items": { "type": "string" } },
    "valid_from": { "type": "string", "format": "date-time" },
    "valid_to": { "type": "string", "format": "date-time" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "delegation_id", "delegator_id", "delegate_id", "scope", "valid_from", "valid_to", "outcome", "evidence_pointer"]
}
```

- Evidence events for payment/usage binding (AUTH/DATA example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["payment.usage.bind"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "delegation_id": { "type": "string" },
    "receipt_id": { "type": "string" },
    "payment_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "receipt_id", "payment_ref", "outcome", "evidence_pointer"]
}
```

- Evidence events for no‑control profile (AUTH/DEP example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["authority.graph.publish", "key.custody.declare", "controlplane.ownership.declare", "telemetry.path.audit"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "subject_id": { "type": "string" },
    "artifact_type": {
      "type": "string",
      "enum": ["authority_graph", "key_custody_model", "controlplane_ownership", "telemetry_egress_map"]
    },
    "artifact_ref": { "type": "string" },
    "artifact_hash": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "artifact_type", "artifact_ref", "outcome", "evidence_pointer"]
}
```

## POL
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["policy.snapshot.publish", "policy.evaluate"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "policy_snapshot_id": { "type": "string" },
    "action": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "policy_snapshot_id", "outcome", "evidence_pointer"]
}
```

## EXEC
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["execution.admit", "execution.refuse", "runtime.dependency.declare"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "workload_id": { "type": "string" },
    "envelope_type": { "type": "string" },
    "dependencies": { "type": "array", "items": { "type": "string" } },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "workload_id", "outcome", "evidence_pointer"]
}
```

## DATA
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["data.residency.enforce", "data.export", "data.erasure"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "data_product_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "data_product_id", "outcome", "evidence_pointer"]
}
```

- Evidence events for purpose/consent/terms/lineage binding (DATA example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["data.purpose.bind", "data.consent.bind", "data.terms.attach", "data.lineage.link"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "data_product_id": { "type": "string" },
    "purpose_id": { "type": "string" },
    "consent_token_ref": { "type": "string" },
    "terms_snapshot_id": { "type": "string" },
    "lineage_sources": { "type": "array", "items": { "type": "string" } },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "data_product_id", "outcome", "evidence_pointer"]
}
```
Purpose/consent/terms/lineage fields are required when applicable (e.g., `purpose_id` for `data.purpose.bind`, `consent_token_ref` for `data.consent.bind`, `terms_snapshot_id` for `data.terms.attach`, `lineage_sources` for `data.lineage.link`).

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
Evidence for ML inference is required for regulatory traceability (e.g., decision accountability, model version lineage, and refusal semantics). A common industry gap is the lack of standardized, portable evidence for inference decisions, so this schema defines a minimal, exportable record aligned with ECS evidence bundles. `hash_profile_id` SHOULD identify the canonicalization/hash rules used. See `docs/ml-evidence-implementation.md` for implementation gaps and insertion points.

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
    "hash_profile_id": { "type": "string" },
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

Evidence for ML training is required to demonstrate dataset provenance, model lineage, and governance controls across the training lifecycle. This schema addresses the frequent absence of deterministic, reusable training evidence artifacts in cloud platforms by defining a portable event shape. `hash_profile_id` SHOULD identify the canonicalization/hash rules used for dataset and checkpoint hashes. See `docs/ml-evidence-implementation.md` for implementation gaps and insertion points.

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
    "hash_profile_id": { "type": "string" },
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
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["interop.profile.declare", "interop.compatibility.test"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "profile_id": { "type": "string" },
    "version": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "profile_id", "version", "outcome", "evidence_pointer"]
}
```

## EXIT
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["exit.path.declare", "exit.validation.run"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "exit_plan_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "exit_plan_id", "outcome", "evidence_pointer"]
}
```

## DEP
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["dependency.graph.publish", "dependency.exception.accept"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "service_id": { "type": "string" },
    "graph_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "service_id", "graph_ref", "outcome", "evidence_pointer"]
}
```

## SUP
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["supplychain.sbom.publish", "supplychain.provenance.attest"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "component_id": { "type": "string" },
    "sbom_ref": { "type": "string" },
    "provenance_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "component_id", "outcome", "evidence_pointer"]
}
```

## OPS
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["ops.runbook.publish", "ops.drill.complete"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "service_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "service_id", "outcome", "evidence_pointer"]
}
```

## PHY
- Evidence types (draft):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["phy.dependency.declare", "phy.partition.exercise"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "service_id": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "service_id", "outcome", "evidence_pointer"]
}
```

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

- Evidence events for chain anchoring (EVID example):
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "enum": ["chain.anchor"] },
    "occurred_at": { "type": "string", "format": "date-time" },
    "tenant_id": { "type": "string" },
    "correlation_id": { "type": "string" },
    "sequence": { "type": "integer" },
    "from_sequence": { "type": "integer" },
    "to_sequence": { "type": "integer" },
    "anchor_hash": { "type": "string" },
    "archive_ref": { "type": "string" },
    "outcome": { "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["id", "event_type", "occurred_at", "tenant_id", "sequence", "from_sequence", "to_sequence", "anchor_hash", "archive_ref", "outcome", "evidence_pointer"]
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
