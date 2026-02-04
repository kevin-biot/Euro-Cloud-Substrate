# WS2 Conformance Outline (Draft)

## API compatibility
- Validate S3-surface compatibility for core operations (PUT/GET/LIST/DELETE) and error semantics.
- Verify versioning/headers for governance metadata are documented and enforced.
 - Validate deterministic error codes for missing/invalid governance metadata.

## Governance metadata enforcement
- Writes MUST fail if jurisdiction/retention/integrity metadata is missing or invalid.
- Metadata MUST persist across copy/move/replication operations.
- Verify metadata survives export/import between providers.
 - Evidence pointer MUST conform to pointer contract (content-addressed, tenant-scoped, retrievability class).

## Immutability and retention
- Test object lock/immutability flags; ensure delete/overwrite is refused when locks are active.
- Verify retention timers and legal hold behaviors with evidence events.

## Evidence and integrity
- Ensure integrity hashes are validated on write and optionally on read for governed objects.
- Evidence pointers MUST be generated for compliance-relevant operations and chainable in audit logs.
 - Export bundles MUST declare `evidence_profile_id` and include chain fields required by the selected profile.
 - Governed access (GET/EXPORT) MUST emit usage receipt evidence when applicable.
