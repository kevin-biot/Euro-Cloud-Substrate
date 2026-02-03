# Migration Baseline — Placeholder

## Intent
Minimum portability expectations: how state, objects, and audit artifacts move provider-to-provider.

## Scope and assumptions
- Applies to provider-to-provider migrations for governed workloads and data.
- Migration MUST preserve governance metadata, authority/policy context, and evidence chains.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Export package: portable bundle of workload definitions, data, governance metadata, and evidence.
- Validation gate: checks performed before activation in the destination environment.
- Rollback window: time-bounded ability to revert to source state with evidence.

## Invariant families (refs)
- EXIT (exit path, validation)
- INT (interfaces for portability)
- DEP (dependency declarations affecting migration)
- SUP (supply-chain visibility for migrated artifacts)
- EVID (evidence of migration/validation)

## Applicable invariant IDs
- EXIT-01/02/03/04, INT-01/03, AUTH-01, POL-01, DEP-01/02/04, SUP-01/02/03/04, EVID-01/04/05

## Evidence expectations
- Declared exit paths and validation exercises.
- Export/import behaviors with evidence of success/refusal.
- Dependency and supply-chain visibility for migrated components.
- Evidence of state validation before/after migration.
- Evidence export bundles MUST follow `docs/evidence-export-schema.md`.

## Migration phases (draft)
1. Plan: declare exit path, dependencies, and validation checks.
2. Export: produce portable package with integrity and evidence.
3. Transfer: move package with verified integrity.
4. Import: validate governance metadata and authority/policy context.
5. Activate: only after validation gates pass; emit evidence.
6. Rollback: if activation fails, revert with evidence.

## Requirements (draft v1)
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

### Export package format (draft)
- Format: OCI artifact or tarball with manifest.
- Manifest schema (fields):
  - `version`: package format version.
  - `created`: RFC 3339 timestamp.
  - `source_provider`: originating provider ID.
  - `tenant_id`: source tenant.
  - `contents`: array of `{ type, path, integrity_hash }` where type ∈ { workload_definition, config, data_snapshot, sbom, evidence_chain_segment }.
  - `governance_metadata`: jurisdiction, classification, retention.
  - `authority_snapshot_id`: authority at export time.
  - `signature`: optional provider signature.
- Integrity: manifest has SHA-256; each content item has hash; signature if available.

### Example manifest (snippet)
```json
{
  "version": "1.0",
  "created": "2025-01-01T00:00:00Z",
  "source_provider": "provider-A",
  "tenant_id": "tenant-123",
  "contents": [
    { "type": "workload_definition", "path": "workload.yaml", "integrity_hash": "sha256:abc..." },
    { "type": "data_snapshot", "path": "data.tar", "integrity_hash": "sha256:def..." },
    { "type": "sbom", "path": "model.cdx", "integrity_hash": "sha256:ghi..." }
  ],
  "governance_metadata": {
    "jurisdiction": "FR",
    "classification": "restricted",
    "retention": "P30D"
  },
  "authority_snapshot_id": "auth-001",
  "signature": "optional-signature"
}
```

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
