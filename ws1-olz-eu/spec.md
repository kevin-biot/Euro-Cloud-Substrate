# WS1 Spec (Draft)

## Objectives
- Define a reusable landing zone profile for ECS providers.

## Invariant families (refs)
- AUTH, POL (authority/policy binding and refusal)
- EXEC (admission)
- DATA (segmentation impact)
- EVID (control-plane evidence)
- PHY (connectivity dependencies)
- DEP (declared critical paths)

## Draft requirements (pass 2)

### Tenant lifecycle (AUTH, POL, EVID)
- Operations: CREATE, GET, UPDATE, DELETE, SUSPEND tenant/project/workspace.
- Required fields on CREATE: `tenant_id` (unique), `authority_binding` (authority ref), `jurisdiction` (ISO 3166; may inherit), `classification_ceiling` (max allowed classification), `policy_baseline` (policy template ref).
- Evidence: tenant lifecycle events MUST include authority/policy snapshot IDs and outcome (success/refusal).

### Identity federation (AUTH)
- MUST support OIDC 1.0 for external IdPs.
- Required claims: `sub`, `iss`, `aud`, `exp`, `iat`; recommended: `groups`, `roles`, `jurisdiction`.
- Token validation: signature, expiry, audience, issuer allowlist. Evidence of validation outcome MUST be recorded.

### Network baseline (EXEC, PHY)
- Tenant isolation: dedicated network namespace or equivalent; default-deny egress with explicit allowlist.
- Ingress: policy-gated with evidence of authorization decisions.
- Cross-tenant flows: MUST be explicitly authorized and evidenced.
- Connectivity dependencies MUST be declared (e.g., required egress destinations/operators).

### Bootstrap evidence (EVID)
- On tenant creation, capture: authority binding verification, policy baseline applied, network namespace creation, initial quotas, jurisdiction assignment.
- Emit an OLZ bootstrap event (see `docs/evidence/catalog.md`) with outcome and refusal reason if applicable.

### No‑Control Profile (NCP) alignment (non‑normative)
- NCP can be applied to integrators or managed‑service partners; see `docs/profiles/no-control-profile.md`.
- Evidence SHOULD include authority graphs, delegation logs, key custody proofs, and control‑plane ownership declarations.
- This is especially relevant where integrators are subject to non‑EU judicial or administrative orders; NCP focuses on operational inability rather than contractual refusal.

### API examples
- Example `POST /tenants` request:
```json
{
  "tenant_id": "tenant-123",
  "authority_binding": "auth-001",
  "jurisdiction": "FR",
  "classification_ceiling": "restricted",
  "policy_baseline": "policy-olz-001"
}
```
- Example 201 response:
```json
{
  "id": "tenant-123",
  "status": "active"
}
```
- Example 400 error (missing authority_binding):
```json
{
  "code": "ECS_MISSING_AUTHORITY",
  "message": "authority_binding is required",
  "evidence_pointer": "eosc://evidence/err-001"
}
```
- Example `GET /tenants/{id}` response:
```json
{
  "id": "tenant-123",
  "authority_binding": "auth-001",
  "jurisdiction": "FR",
  "classification_ceiling": "restricted",
  "policy_baseline": "policy-olz-001",
  "status": "active"
}
```

## Sections to draft
- Tenant model and lifecycle.
- Identity binding and role semantics.
- Network segmentation and egress controls.
- Policy baselines and exception workflows.
- Audit/event capture requirements.
