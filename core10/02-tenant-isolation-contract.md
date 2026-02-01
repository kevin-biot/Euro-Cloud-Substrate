# Tenant Isolation Contract — Placeholder

## Intent
Minimum isolation semantics across compute, storage, network, logs, and indexes.

## Invariant families (refs)
- EXEC (isolation enforcement)
- DATA (storage/logs isolation)
- DEP (critical path declarations)
- PHY (connectivity constraints)
- EVID (evidence of isolation controls)

## To cover
- Isolation guarantees (technical and procedural).
- Cross-tenant leakage prevention and verification hooks.
- Evidence requirements for isolation controls.

## Invariants (draft)
- Compute, storage, network, logs, and indexes MUST enforce tenant isolation by default.
- Isolation controls MUST be verifiable through evidence (attestation, logs, or tests).
- Cross-tenant access MUST be explicit, least-privilege, and evidence-backed.

## Next steps
- Define testable invariants.
- Align with Execution Envelopes and Control Plane policies.
