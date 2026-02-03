# WS4 Spec (Draft)

## Objectives
- Define the minimal API surface for workload deployment, identity, storage, and audit queries.

## Invariant families (refs)
- INT (interfaces)
- AUTH/POL (authn/authz expectations)
- EXIT (portability support)
- EVID (audit/evidence queries)

## Sections to draft
- Resources and operations per plane (identity, control, execution, data).
- Authentication/authorization model and required claims.
- Error semantics, pagination, and compatibility expectations.
- Evidence and audit query interfaces.

## Core resources (draft)

### Tenant (aligns with OLZ)
- Fields: `id`, `authority_binding`, `jurisdiction`, `classification_ceiling`, `policy_baseline`, `status`.
- Endpoints: `POST /tenants`, `GET /tenants/{id}`, `PATCH /tenants/{id}`, `DELETE /tenants/{id}`, `POST /tenants/{id}/suspend`.
- Evidence: lifecycle events include authority/policy snapshot and outcome.

### Workload
- Fields: `id`, `tenant_id`, `envelope_type` (container|vm), `image_ref`, `policy_ref`, `status`.
- Endpoints: `POST /workloads`, `GET /workloads/{id}`, `DELETE /workloads/{id}`.
- Evidence: admission/refusal logged with policy/authority context.

### StorageObject (EOSC)
- S3-compatible surface; governance headers per `ws2-eosc/spec.md`.
- Endpoint base: `/storage/{bucket}/objects/*` with required governance metadata headers.

### AuditEvent
- Read-only: `GET /events`, `GET /events/{id}`.
- Filtering: by `tenant`, time range, `event_type`, `outcome`.
- Must preserve ordering/integrity guarantees (aligned with WS5).
- Pagination: cursor-based recommended (`?cursor=...&limit=...`); include `next_cursor` if more results. Default limit 100; max 1000.
- Async events: providers MAY offer real-time subscription (see `docs/interop/asyncapi-events.yaml`).
- Export endpoints SHOULD support No‑Control Profile (NCP) evidence bundles when applicable.

## Authentication & authorization
- Authn:
  - mTLS for service-to-service.
  - OIDC bearer tokens for user/API access (aligned with OLZ federation).
  - API keys: OPTIONAL; if supported, MUST be scoped to tenant and least privilege.
- Authz:
  - Policy evaluation per POL invariants; refusals are first-class and MUST emit evidence with policy/authority snapshot.

## Error model
- Standard HTTP status codes.
- Error body:
```json
{ "code": "ECS_...", "message": "...", "evidence_pointer": "..." }
```
- Refusals include evidence pointer for audit.
- Providers SHOULD implement rate limiting and use standard headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`); 429 with error body on limit exceeded.

## Versioning
- Path-based versioning: e.g., `/v1/tenants`, `/v1/workloads`.
- Deprecation policy: minimum 6 months notice; use `Sunset` header on deprecated endpoints.
- Backward-compatible changes documented; breaking changes in new major versions.
