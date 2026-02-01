# Interop API Surface — Placeholder

## Intent
Minimum APIs for workload deployment, identity, storage, and audit queries to enable portability.

## Invariant families (refs)
- INT (standard interfaces)
- AUTH/POL (authz/authn expectations)
- EXIT (portability support)
- EVID (audit/evidence queries)

## To cover
- API resources and operations per plane.
- Authentication/authorization expectations.
- Versioning and compatibility guarantees.

## Invariants (draft)
- Core resources (identity, workload, storage, audit) MUST be exposed via a documented, versioned API.
- APIs MUST be authenticated/authorized with authority mapping to roles and tenants.
- Audit/evidence queries MUST preserve ordering and integrity proofs.
- Backward-compatible changes MUST follow a published versioning policy.

## Next steps
- Draft minimal API set and error semantics.
- Align with Evidence and Audit interfaces and Core 10 dependencies.
