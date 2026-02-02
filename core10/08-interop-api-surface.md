# Interop API Surface — Placeholder

## Intent
Minimum APIs for workload deployment, identity, storage, and audit queries to enable portability.

## Scope and assumptions
- Applies to external and intra-provider APIs that expose ECS portability surfaces.
- References `ws4-interop-api/spec.md` and `docs/interop/openapi-skeleton.yaml` for concrete shapes.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Interop API: versioned, documented API surface for core ECS resources.
- Evidence query: read-only interface for audit events with integrity guarantees.
- Portability interface: APIs that enable export/import and validation of governed artifacts.

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

## Minimum resources (draft)
- Tenant: create/read/update/suspend/delete (aligned with OLZ).
- Workload: create/read/delete (aligned with Execution Envelopes).
- Storage: EOSC-compatible object operations.
- Audit events: list/read with cursor-based pagination.
- Export/import: initiate and verify migration jobs (Core10-10).

## Authentication and authorization (draft)
- Default auth: OIDC for user/API access; mTLS for service-to-service (S2S) flows.
- Authn/z MUST map to authority binding and tenant scope (AUTH/POL invariants).
- API keys MAY be supported but MUST be tenant-scoped and least-privilege.

## Error model (draft)
- Standard HTTP status codes with ECS error body:
```json
{ "code": "ECS_...", "message": "...", "evidence_pointer": "..." }
```
- Refusals MUST include `evidence_pointer`.

## Versioning and compatibility (draft)
- Path-based versioning (e.g., `/v1/...`).
- Backward-compatible changes MUST preserve contract; breaking changes require new major version.
- Deprecation MUST include notice window and `Sunset` header.

## Pagination and ordering (draft)
- Cursor-based pagination REQUIRED for audit/event streams.
- Responses MUST include `next_cursor` when more results exist.
- Ordering MUST be stable and integrity-preserving.

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
