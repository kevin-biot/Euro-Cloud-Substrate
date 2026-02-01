# ADR-0002: Invariant Set v0.3 is Authoritative

## Status
Accepted

## Context
The invariant taxonomy (AUTH, POL, EXEC, DATA, EVID, INT, EXIT, DEP, SUP, OPS, PHY) was completed in `docs/invariants-v0.3.md`.

## Decision
- `docs/invariants-v0.3.md` is the single source of truth for ECS invariants and their statuses.
- No new invariants are introduced without an explicit versioned update.
- All specifications, Core10 entries, workstreams, and profiles MUST reference invariants by ID.
- Conformance discussions are anchored to these IDs; no parallel invariant definitions.

## Consequences
- Prevents scope drift and duplicate semantics.
- Profiles and mappings must bind to invariant IDs.
- Changes to invariants require a deliberate revision and ADR if semantics change.***
