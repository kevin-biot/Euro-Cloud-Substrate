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

### Access layer ≠ governance (context)
Access enablement (APIs, graphs, connectors) does **not** imply governance.  
ECS requires that access is **policy‑bound at execution time** with refusal evidence when obligations cannot be met.

### Trust root acceptance
Authority verification MUST be bound to explicit trust anchors (IdPs, CAs, credential issuers). The control plane MUST:
- Evaluate requests against the **declared authority snapshot** (time‑scoped trust roots).
- Refuse actions when trust roots are missing, expired, or out of scope.
- Emit evidence that records the `authority_snapshot_id` used for verification.

Note: self‑certifying identifier systems (e.g., KERI) can serve as trust anchors when their verification proofs are exportable.

### Jurisdiction‑aware routing (non‑normative)
The control plane SHOULD enforce jurisdiction‑aware routing and emit refusal evidence when a route violates policy.  
ECS remains routing‑protocol‑agnostic; specific routing standards can satisfy this requirement as long as **evidence and contract expectations** are met.

### Routing control primitives (draft, protocol‑agnostic)
To keep routing enforceable without prescribing a protocol, ECS expects **minimal routing primitives**:
- **Route intent**: action + jurisdiction path + data class.
- **Route policy snapshot**: policy version used for routing decision.
- **Corridor proof reference**: pointer to the route eligibility proof (token, matrix, signed feed).
- **Route decision evidence**: allow/refuse with refusal reason.

**Minimal routing decision input (example):**
```json
{
  "route_intent": "agent.invoke|ml.inference.route|ml.training.route|data.transfer",
  "jurisdiction_path": ["EU", "DE"],
  "data_class": "restricted",
  "policy_snapshot_id": "pol-2026-02",
  "corridor_ref": "eosc://corridor/sha256:...",
  "capability_id": "cap:agent.search.v1",
  "model_id": "model-001"
}
```

**Minimal routing decision event (example):**
```json
{
  "event_type": "route.decision",
  "occurred_at": "2026-02-05T12:02:00Z",
  "tenant_id": "tenant-123",
  "sequence": 1901,
  "outcome": "accepted|refused|failed",
  "jurisdiction_path": ["EU", "DE"],
  "policy_snapshot_id": "pol-2026-02",
  "corridor_ref": "eosc://corridor/sha256:...",
  "refusal_reason": "corridor_invalid",
  "evidence_pointer": "eosc://evidence/sha256:..."
}
```

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
  "obligations": [
    { "type": "purpose", "value": "inference-only" },
    { "type": "retention", "value": "P30D" },
    { "type": "no_onward_transfer", "value": true }
  ],
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

## EUDI wallet integration (non-normative)
- See `docs/domains/eudi-wallet-integration.md` for minimum evidence expectations and delegation notes.
