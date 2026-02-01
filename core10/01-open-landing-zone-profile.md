# Open Landing Zone Profile (OLZ-EU) — Placeholder

## Intent
Define the baseline for tenant creation, identity, network, policy, and audit required for ECS.

## Invariant families (refs)
- AUTH (authority binding, refusal)
- POL (policy artifacts/evaluation)
- EXEC (admission)
- DATA (segmentation impact)
- EVID (control-plane evidence)
- PHY (connectivity dependencies)

## To cover
- Tenant bootstrap flow and roles.
- Network segmentation, egress control, service boundaries.
- Default policy posture and exception handling (fail-closed bias).
- Audit/event capture for compliance-critical actions.

## Invariants (draft)
- Tenant creation MUST bind identity and authority before resources are provisioned.
- Network and egress baselines MUST default to deny for governed workloads.
- Exceptions to baseline policy MUST be explicitly approved and evidence-backed.
- Compliance-critical actions MUST emit evidence events at the control plane.

## Next steps
- Draft spec and invariants.
- Map to evidence requirements and Control Plane interfaces.
