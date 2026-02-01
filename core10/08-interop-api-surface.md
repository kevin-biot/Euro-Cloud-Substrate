# Interop API Surface — Placeholder

## Intent
Minimum APIs for workload deployment, identity, storage, and audit queries to enable portability.

## Invariant families (refs)
- INT (standard interfaces)
- AUTH/POL (authz/authn expectations)
- EXIT (portability support)
- EVID (audit/evidence queries)

## Applicable invariant IDs
- INT-01/03, AUTH-01/02/04, POL-01/02/03/04/05, EXIT-01/02/03, EVID-01/04

## Evidence expectations
- API/interface definitions and compatibility docs.
- Authn/z decisions with authority mapping evidence.
- Portability/export behaviors with evidence of success/refusal.
- Audit/evidence query integrity guarantees.

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
