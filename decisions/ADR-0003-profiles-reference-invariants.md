# ADR-0003: Profiles Reference Invariants

## Status
Accepted

## Context
Profiles (e.g., CRP) make ECS usable in context. Without guardrails, profiles could redefine semantics or fragment the invariant contract.

## Decision
- Profiles may only select and/or tighten existing invariants; they MUST reference invariant IDs (e.g., AUTH-01, EXEC-03).
- Profiles MUST NOT introduce new semantics or redefine invariants.
- Profiles may require additional evidence or stricter interpretation for selected invariants.
- CRP is an example profile and is to be interpreted over the invariant set.

## Consequences
- Profiles remain compatible and composable.
- Prevents fragmentation and semantic drift.
- New profiles must declare scope, applicable invariant IDs, and any stricter evidence requirements.
