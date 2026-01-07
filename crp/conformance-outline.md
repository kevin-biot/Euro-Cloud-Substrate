# CRP Conformance Outline (Draft)

## Local authority and policy
- Simulate loss of upstream identity/control plane; verify authority checks succeed using local cache or fail closed if stale.
- Validate policy evaluation uses last valid snapshot; if missing/expired, execution refuses.

## Control-plane independence
- Disable upstream scheduler/orchestrator; CRP workloads MUST continue under local control-plane or pre-positioned runtime.
- Verify lifecycle operations (start/stop/restart) function locally for declared CRP envelopes.

## Data residency
- Ensure governed data required for CRP workloads remains in-jurisdiction during partition; block cross-border replication while partitioned.
- Validate reconciliation resumes only when policy allows after connectivity returns.

## Evidence buffering and reconciliation
- Under partition, evidence MUST buffer locally with integrity protection; verify no loss on restart.
- After connectivity restoration, evidence MUST reconcile to the primary audit chain with ordering preserved.

## Deterministic degradation and refusal
- Force degraded conditions; verify system enters predefined reduced-capability modes with auditable state.
- Attempt execution with missing authority/policy/data dependency; expect explicit refusal (not best-effort).
