# Open Landing Zone Profile (OLZ-EU) — Placeholder

## Intent
Define the baseline for tenant creation, identity, network, policy, and audit required for ECS.

## Scope and assumptions
- Applies to governed workloads/tenants within an ECS deployment.
- Focuses on authority/policy binding, network posture, and evidence at landing-zone bootstrap.
- Uses invariant IDs from `docs/invariants/v0.3.md`; no new semantics introduced.

## OLZ‑EU as portable standard (draft)
OLZ‑EU is intended as a **provider‑agnostic landing zone contract** that can be implemented across different control planes (Kubernetes/OKD, OpenStack, managed platforms). It defines the minimum identity, network, policy, and evidence posture required to onboard tenants in a portable way. A reference open‑source implementation does not yet exist; ECS treats this as a gap to be filled by community adapters rather than a mandated stack.

## Definitions (draft)
- Landing zone: the initial tenant boundary (identity, network, policy, evidence) created before workloads run.
- Authority binding: verifiable link between tenant and an issuing authority with scope and validity.
- Policy baseline: default-deny policy snapshot applied at tenant bootstrap.
- Control-plane action: any tenant or policy operation that changes authority, access, network, or workload admission.

## Inputs and artifacts (draft)
- Tenant request: tenant id, jurisdiction, classification ceiling, owner/contact, requested policy baseline.
- Authority binding: issuer, subject, scope, validity window, signature/proof.
- Policy baseline: versioned policy artifact reference and hash.
- Network posture: segmentation rules, egress allowlist, inbound defaults.
- Evidence sink: endpoint or buffer where evidence events are written.

## Invariant families (refs)
- AUTH (authority binding, refusal)
- POL (policy artifacts/evaluation)
- EXEC (admission)
- DATA (segmentation impact)
- EVID (control-plane evidence)
- PHY (connectivity dependencies)

## Applicable invariant IDs
- AUTH-01/02/04/05, POL-01/02/04, EXEC-01, DATA-01, EVID-01/03/04, PHY-01

## Evidence expectations
- Authority/policy artifacts (versioned) and admission outcomes.
- Evidence events for control-plane actions; refusal/escalation logs with snapshot ids.
- Declared connectivity dependencies affecting landing zone controls.
- Network posture definitions and proof of enforcement at bootstrap.

## Bootstrap flow (draft)
1. Submit tenant request with authority binding and policy baseline reference.
2. Verify authority binding validity and scope; refuse if invalid/expired.
3. Fetch and validate policy baseline; refuse if missing/stale.
4. Create tenant boundary (identity, network, storage/log segmentation).
5. Apply default-deny policy and admission gate.
6. Emit evidence events for each control-plane action with snapshot references.

## Authority binding schema (draft JSON)
```json
{
  "issuer": "authority.example",
  "subject": "tenant-123",
  "scope": ["tenant.create", "tenant.manage"],
  "valid_from": "2025-01-01T00:00:00Z",
  "valid_to": "2026-01-01T00:00:00Z",
  "proof": "sig-or-attestation-ref"
}
```

## Requirements (draft v1)
- Tenant creation MUST bind to explicit authority; invalid/expired bindings MUST be refused with evidence (AUTH-01/02/04/05).
- Policy baseline MUST be versioned and validated before any governed action is enabled (POL-01/02/04).
- Default posture MUST be deny; exceptions MUST be explicit, time-bound, and evidenced (POL-02/04).
- Control-plane actions (create/update/delete/suspend) MUST pass through an admission gate bound to authority/policy (EXEC-01).
- Segmentation and egress controls MUST be declared and enforced; dependencies MUST be declared (DATA-01, PHY-01).
- Evidence events MUST include authority and policy snapshot ids and be integrity-protected where required (EVID-01/03/04).

## Conformance outline (draft v1)
- Declare selected evidence profile for OLZ evidence outputs and bundle exports.
- Verify authority binding validation and refusal evidence on invalid/expired bindings.
- Verify policy baseline validation and default-deny enforcement prior to workload admission.
- Test admission gate decisions with evidence pointers for allow/refuse outcomes.
- Validate network segmentation and egress defaults match declared posture.
- Confirm evidence events include authority/policy snapshot ids and integrity proofs.
