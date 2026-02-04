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

## Draft requirements (pass 3)

## Terms (WS1 scope)
- **authority_binding**: Reference to an authority snapshot (who can approve, who can revoke, escalation paths).
- **policy_baseline**: Reference to a policy template applied at tenant creation; policy snapshots are concrete, versioned applications of a baseline.
- **classification_ceiling**: Maximum data classification allowed for the tenant/workspace.
- **jurisdiction**: ISO 3166 country code (or inherited scope) used for policy evaluation and evidence.

### Tenant lifecycle (AUTH, POL, EVID)
- Operations: CREATE, GET, UPDATE, DELETE, SUSPEND tenant/project/workspace.
- Required fields on CREATE: `tenant_id` (unique), `authority_binding` (authority ref), `jurisdiction` (ISO 3166; may inherit), `classification_ceiling` (max allowed classification), `policy_baseline` (policy template ref).
- Evidence: tenant lifecycle events MUST include authority/policy snapshot IDs and outcome (success/refusal).
  - Required evidence artifacts:
    - Authority snapshot referenced by `authority_binding`.
    - Policy snapshot derived from `policy_baseline`.
    - Lifecycle decision event with outcome and refusal reason (if refused).

### Identity federation (AUTH)
- MUST support OIDC 1.0 for external IdPs.
- Required claims: `sub`, `iss`, `aud`, `exp`, `iat`; recommended: `groups`, `roles`, `jurisdiction`.
- Token validation: signature, expiry, audience, issuer allowlist. Evidence of validation outcome MUST be recorded.
  - S2S flows SHOULD use mTLS with explicit service identity and evidence of validation.

### Network baseline (EXEC, PHY)
- Tenant isolation: dedicated network namespace or equivalent; default-deny egress with explicit allowlist.
- Ingress: policy-gated with evidence of authorization decisions.
- Cross-tenant flows: MUST be explicitly authorized and evidenced.
- Connectivity dependencies MUST be declared (e.g., required egress destinations/operators).
  - Evidence of segmentation configuration and allowlist decisions MUST be retained.

### Bootstrap evidence (EVID)
- On tenant creation, capture: authority binding verification, policy baseline applied, network namespace creation, initial quotas, jurisdiction assignment.
- Emit an OLZ bootstrap event (see `docs/evidence/catalog.md`) with outcome and refusal reason if applicable.
  - Bootstrap evidence MUST be exportable with profile selection and hash-chain continuity where required by profile.

### No‑Control Profile (NCP) alignment (non‑normative)
- NCP can be applied to integrators or managed‑service partners; see `docs/profiles/no-control-profile.md`.
- Evidence SHOULD include authority graphs, delegation logs, key custody proofs, and control‑plane ownership declarations.
- This is especially relevant where integrators are subject to non‑EU judicial or administrative orders; NCP focuses on operational inability rather than contractual refusal.

## Evidence profile and export alignment
- OLZ events MUST be emitted using the Core10-05 envelope.
- Evidence exports MUST declare `evidence_profile_id` and include chain fields where required by the selected profile.
- Exported bundles SHOULD include lifecycle event ranges and the referenced authority/policy artifacts.

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
  "evidence_pointer": "eosc://evidence/err-001",
  "evidence_profile_id": "ecs-evidence-baseline"
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
