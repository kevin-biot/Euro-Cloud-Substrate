# ECS ML Inference Sidecar Adapter (Draft Spec)

## 1. Overview
- **Adapter name:** ML Inference Sidecar
- **Target system:** Model inference endpoints (K8s services, serverless ML endpoints)
- **Purpose:** Emit verifiable evidence for ML inference decisions and outcomes.
- **Scope:** Wraps inference calls to emit Core10‑05 events; does not replace model serving.

## 2. ECS alignment
- **Core10 references:** Core10‑05 (Evidence Event Model), Core10‑06 (Audit Chain)
- **Invariant families:** EVID, SUP, EXEC, DATA, AUTH, POL
- **Evidence profiles:** baseline; regulated‑ML when required

## 3. Inputs
Required:
- `policy_snapshot_id`
- `authority_snapshot_id`
- `model_id`

Optional:
- `hash_profile_id`
- `correlation_id`
- `delegation_id` / `agent_*` identifiers
- `jurisdiction`, `classification`

Config sources:
- Env vars (`ECS_EVIDENCE_PROFILE`, `ECS_HASH_PROFILE`)
- Request headers (correlation/delegation)

## 4. Evidence emission
### Event types
- `ml.inference` (accepted/refused/failed)

### Required fields
- Core10‑05 envelope fields
- `model_id`, `input_hash`, `context_hash`
- `policy_snapshot_id`, `authority_snapshot_id`

### Refusal semantics
- Refuse if policy/authority missing or invalid.
- Refuse when a required evidence profile or hash profile is not supported.
- Emit refusal evidence with `refusal_reason`.

### Correlation model
- `correlation_id` for request traceability.
- Delegation identifiers if invoked on behalf of a user/agent.

### Artifacts
- Model SBOM reference (`model_sbom_ref`)
- Policy snapshot and authority snapshot artifacts
- Optional output reference (`output_ref`)

## 5. Export behavior
- Evidence bundles as per `docs/evidence/export-schema.md`.
- Chain integrity with `chain_id`, `event_hash`, `prev_hash`.

## 6. Security & trust
- Authn/z enforced at gateway or sidecar boundary.
- Trust roots declared via authority snapshots.
- Delegation MUST be time‑bounded and scoped.

## 7. Deployment & ops
- Sidecar container next to model service.
- Failure modes:
  - **Fail‑closed** for governed workloads.
  - Optional fail‑open for non‑governed workloads (profile‑specific).

## 8. Minimal examples
### Inference request (headers)
```
X-ECS-Policy-Snapshot: pol-2026-02
X-ECS-Authority-Snapshot: auth-2026-01
X-ECS-Correlation-Id: corr-123
```

### Evidence event (accepted)
```json
{
  "event_type": "ml.inference",
  "occurred_at": "2026-02-05T12:00:00Z",
  "tenant_id": "tenant-123",
  "sequence": 881,
  "outcome": "accepted",
  "model_id": "model-001",
  "input_hash": "sha256:...",
  "context_hash": "sha256:...",
  "policy_snapshot_id": "pol-2026-02",
  "authority_snapshot_id": "auth-2026-01",
  "evidence_pointer": "eosc://evidence/sha256:..."
}
```

### Refusal event
```json
{
  "event_type": "ml.inference",
  "occurred_at": "2026-02-05T12:00:03Z",
  "tenant_id": "tenant-123",
  "sequence": 882,
  "outcome": "refused",
  "refusal_reason": "policy_missing",
  "policy_snapshot_id": "pol-2026-02",
  "authority_snapshot_id": "auth-2026-01",
  "evidence_pointer": "eosc://evidence/sha256:..."
}
```

## 9. Conformance checklist
- Emits Core10‑05 envelope.
- Declares evidence profile and hash profile (when required).
- Emits refusal evidence for policy/authority failures.
- Exports evidence bundles with chain integrity.

## 10. Non‑goals
- Not a full model serving framework.
- Does not standardize model input/output schemas.
- Does not implement watermarking or output policy in the model itself.
