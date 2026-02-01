# Migration Baseline — Placeholder

## Intent
Minimum portability expectations: how state, objects, and audit artifacts move provider-to-provider.

## Invariant families (refs)
- EXIT (exit path, validation)
- INT (interfaces for portability)
- DEP (dependency declarations affecting migration)
- SUP (supply-chain visibility for migrated artifacts)
- EVID (evidence of migration/validation)

## Applicable invariant IDs
- EXIT-01/02/03/04, INT-01/03, DEP-01/02/04, SUP-01/02/03/04, EVID-01/04/05

## Evidence expectations
- Declared exit paths and validation exercises.
- Export/import behaviors with evidence of success/refusal.
- Dependency and supply-chain visibility for migrated components.
- Evidence of state validation before/after migration.

## Requirements (draft)
- Workloads and data MUST be exportable with governance metadata intact (EXIT-01/02/03).
- Export MUST include evidence of successful transfer and integrity verification (EVID-01/03/04).
- Import MUST validate governance metadata and authority binding before activation (AUTH-01, POL-01).
- Dependency inventory MUST be provided to inform migration feasibility (DEP-01/02, SUP-01).
- Reversibility: migration MUST support rollback with evidence of state changes (EXIT-03).

### Export process (draft)
- Package: workload definition, configuration, data, governance metadata, SBOM, evidence chain segment.
- Integrity: SHA-256 hashes on all artifacts; manifest signed if supported.
- Evidence: export event logged with authority/policy snapshot and integrity results.

### Import process (draft)
- Validation: verify integrity, governance metadata, authority binding; refuse on failure.
- Activation: policy evaluation before workload start; refusal on failure.
- Evidence: import event logged with validation results and any refusals.

## Conformance outline (draft)
- Verify export includes required artifacts and governance metadata.
- Test import validation rejects on integrity/policy failure.
- Validate rollback capability with evidence.
- Confirm dependency inventory is accurate and provided.

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
