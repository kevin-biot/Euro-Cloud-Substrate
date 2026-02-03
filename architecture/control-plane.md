# Control Plane Capabilities (Draft)

## Intent
Define the minimum control-plane capabilities needed to satisfy ECS invariants, without prescribing specific products or implementations.

## Scope and assumptions
- Applies to all governed actions across identity, execution, and data planes.
- Capabilities are normative; implementations are non-normative.

## Core capabilities (normative)

### Policy engine
Deterministic policy evaluation service that:
- Accepts versioned policy artifacts and returns deterministic decisions.
- Supports explicit refusal semantics and fail-closed behavior.
- Emits evidence events with policy snapshot id and authority context.

### Admission gate
Decision point that MUST be invoked before any governed action (create/update/delete/execute). It:
- Calls the policy engine (or embedded policy logic) with required inputs.
- Enforces allow/refuse outcomes before action execution.
- Emits evidence for allow/refuse with authority and policy snapshot ids.

### Evidence hooks
Mandatory emission points that:
- Record decision outcomes, refusals, and escalations.
- Provide evidence pointers and integrity metadata (hash/chain refs).
- Support export and reconciliation requirements.

## Minimal interfaces (draft)

### Policy evaluation
```json
{
  "action": "workload.deploy",
  "subject": "tenant-123",
  "resource": "wl-456",
  "policy_snapshot_id": "pol-001",
  "authority_binding": "auth-789",
  "context": { "data_class": "restricted" }
}
```

Response:
```json
{
  "outcome": "accepted|refused|failed",
  "policy_snapshot_id": "pol-001",
  "authority_snapshot_id": "auth-789",
  "evidence_pointer": "eosc://evidence/evt-123",
  "refusal_reason": "policy_missing"
}
```

### Admission decision event (evidence)
```json
{
  "event_type": "admission.decision",
  "occurred_at": "2025-01-01T00:00:00Z",
  "tenant_id": "tenant-123",
  "action": "workload.deploy",
  "outcome": "accepted|refused|failed",
  "policy_snapshot_id": "pol-001",
  "authority_snapshot_id": "auth-789",
  "evidence_pointer": "eosc://evidence/evt-123"
}
```

## Non-normative implementation mapping
- Kubernetes admission controllers + OPA/Gatekeeper or Kyverno.
- Service mesh policy engines (where deterministic and evidence-backed).
- Provider-native policy services if they meet determinism and evidence requirements.
