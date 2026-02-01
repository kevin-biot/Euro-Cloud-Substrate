# Migration Baseline — Placeholder

## Intent
Minimum portability expectations: how state, objects, and audit artifacts move provider-to-provider.

## Invariant families (refs)
- EXIT (exit path, validation)
- INT (interfaces for portability)
- DEP (dependency declarations affecting migration)
- SUP (supply-chain visibility for migrated artifacts)
- EVID (evidence of migration/validation)

## To cover
- Data, configuration, and policy snapshot portability.
- Evidence and audit artifact transfer.
- Downtime, sequencing, and verification expectations.

## Invariants (draft)
- Migration MUST preserve governance metadata, policy snapshots, and authority bindings.
- Evidence and audit artifacts MUST transfer with integrity proofs intact.
- Post-migration validation MUST occur before governed execution resumes.

## Next steps
- Define migration scenarios and required guarantees.
- Align with Interop APIs and EOSC metadata requirements.
