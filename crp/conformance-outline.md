# CRP Conformance Outline (Draft)

# WS3 Conformance Outline (Draft)

### Tier 1 — Smoke
- Simulate loss of upstream identity/control plane; verify authority checks succeed using local cache or fail closed if stale.
- Validate policy evaluation uses last valid snapshot; if missing/expired, execution refuses.
- Evidence buffering writes locally during partition.

### Tier 2 — Integration
- Disable upstream scheduler/orchestrator; CRP workloads MUST continue under local control-plane or pre-positioned runtime.
- Cross-partition routing denial: ensure governed traffic does not egress across partitions unless explicitly allowed.
- Stale cache rejection: force stale policy/authority cache and confirm refusal.
- Evidence replay after reconnect preserves ordering and integrity.

### Tier 3 — Stress
- Sustained partition operation: run workloads under partition for extended duration with deterministic degradation modes.
- Policy conflicts under partition: verify resolution is deterministic and auditable.
- Evidence volume limits: buffer under load without loss; reconcile cleanly when connectivity returns.

## Data residency
- Ensure governed data required for CRP workloads remains in-jurisdiction during partition; block cross-border replication while partitioned.
- Validate reconciliation resumes only when policy allows after connectivity returns.

## Deterministic degradation and refusal
- Force degraded conditions; verify system enters predefined reduced-capability modes with auditable state.
- Attempt execution with missing authority/policy/data dependency; expect explicit refusal (not best-effort).
