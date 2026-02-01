# Open Landing Zone Profile (OLZ-EU) — Placeholder

## Intent
Define the baseline for tenant creation, identity, network, policy, and audit required for ECS.

## Scope and assumptions
- Applies to governed workloads/tenants within an ECS deployment.
- Focuses on authority/policy binding, network posture, and evidence at landing-zone bootstrap.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

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
- Authority/policy artifacts (versioned), admission outcomes, segmentation policies.
- Evidence events for control-plane actions; refusal/escalation logs.
- Declared connectivity dependencies affecting landing zone controls.

## Draft requirements (pass 1)
- Identity & authority: tenant/project creation MUST bind to explicit authority with refusal semantics (AUTH-01/02/04/05). Authority/policy artifacts are versioned (POL-01).
- Policy posture: default deny for governed workloads; exceptions are explicit and evidence-backed (POL-02/04).
- Admission: resource creation/update MUST pass through an admission gate bound to authority/policy (EXEC-01).
- Network/egress: segmentation and egress controls are declared and enforced; connectivity dependencies are declared (DATA-01, PHY-01).
- Evidence: control-plane actions emit evidence with policy snapshot/authority context; hash integrity applied where required (EVID-01/03/04).

## Conformance outline (pass 1)
- Verify authority/policy artifacts exist and are versioned; refusals recorded.
- Test admission gate blocks/approves per policy; exceptions are explicit and logged.
- Validate segmentation/egress controls default to deny and match declared dependencies.
- Confirm control-plane actions emit evidence with policy/authority context and integrity.
