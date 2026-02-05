# WS4 Spec (Draft)

## Objectives
- Define the minimal API surface for workload deployment, identity, storage, and audit queries.

## Invariant families (refs)
- INT (interfaces)
- AUTH/POL (authn/authz expectations)
- EXIT (portability support)
- EVID (audit/evidence queries)

## Terms (WS4 scope)
- **interop resource**: API surface that is portable across providers (tenant, workload, storage, audit).
- **evidence export**: Bundle of events/artifacts per `docs/evidence/export-schema.md`.
- **Core10-05 envelope**: Canonical evidence event envelope used by audit APIs.

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

### Data products and permissions (OPTIONAL, MAY)
These endpoints are OPTIONAL but recommended for data‑space compatibility and ML governance.
- `GET /v1/data-products/{id}` → data product descriptor (see `docs/invariants/data.md`).
- `GET /v1/data-products/{id}/permissions` → purpose binding, obligations, and policy snapshot ids.
- `GET /v1/data-products/{id}/dataset-manifest` → dataset boundary object / DSBOM.
- `GET /v1/data-use-postures/{id}` → declared data‑use posture and exclusion handling.

### AuditEvent
- Read-only: `GET /events`, `GET /events/{id}`.
- Filtering: by `tenant`, time range, `event_type`, `outcome`.
- Must preserve ordering/integrity guarantees (aligned with WS5).
- Events MUST conform to Core10-05 and include chain fields when required by the selected evidence profile.
- Pagination: cursor-based recommended (`?cursor=...&limit=...`); include `next_cursor` if more results. Default limit 100; max 1000.
- Async events: providers MAY offer real-time subscription (see `docs/interop/asyncapi-events.yaml`).
- Export endpoints SHOULD support No‑Control Profile (NCP) evidence bundles when applicable.

## Federation roles (non-normative)
The IPCEI‑CIS reference architecture defines Federation Manager and Federation Broker roles. ECS does not mandate an implementation, but requires contract‑level capabilities that map cleanly to these roles:

- **Federation Manager (FM)** → ECS interop + migration control surface:
  - Onboarding and access negotiation via interop APIs (Core10‑08, WS4).
  - Portability/export/import with evidence of success/refusal (Core10‑10, WS6).
  - Audit/evidence queries and integrity guarantees (Core10‑05/06, WS5).

- **Federation Broker (FB)** → ECS discovery + claims surface:
  - Publish supported evidence profiles and profile claims.
  - Provide example evidence bundles and verifier inputs for procurement/testing.
  - Advertise export endpoints and interop capabilities (WS4).

This framing allows a provider, marketplace, or consortium to play the FM/FB roles without requiring a new broker product; the ECS contract is the binding layer.

See `docs/domains/federation.md` for the federation domain summary and evidence expectations.

## Authentication & authorization
- Authn:
  - mTLS for service-to-service.
  - OIDC bearer tokens for user/API access (aligned with OLZ federation).
  - API keys: OPTIONAL; if supported, MUST be scoped to tenant and least privilege.
- Token expectations (baseline):
  - Required claims: `iss`, `sub`, `aud`, `exp`, `iat`.
  - Delegated actions MUST include `delegation_id`, `scope`, and expiry; `actor_type=delegate` SHOULD be present.
  - Delegated actions SHOULD carry intent/purpose reference where governed actions require explicit intent.
- Authz:
  - Policy evaluation per POL invariants; refusals are first-class and MUST emit evidence with policy/authority snapshot.
  - Auth decisions MUST emit evidence using the Core10-05 envelope.

## Error model
- Standard HTTP status codes.
- Error body:
```json
{ "code": "ECS_...", "message": "...", "evidence_pointer": "..." }
```
- Refusals include evidence pointer for audit.
- Error bodies SHOULD include `evidence_profile_id` when refusal is governed by a declared profile.
- Providers SHOULD implement rate limiting and use standard headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`); 429 with error body on limit exceeded.

## Versioning
- Path-based versioning: e.g., `/v1/tenants`, `/v1/workloads`.
- Deprecation policy: minimum 6 months notice; use `Sunset` header on deprecated endpoints.
- Backward-compatible changes documented; breaking changes in new major versions.

## Federation claims (non‑normative)
Providers MAY expose a capability declaration to surface federation‑relevant differences rather than hide them. Example:
- `GET /v1/federation/claims`
  - identity federation model and claim mappings
  - storage classes and portability limits
  - policy enforcement scope (admission, egress, evidence)
  - audit/export capabilities (profiles, chain support)
