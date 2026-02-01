# Execution Envelope Profiles — Placeholder

## Intent
Container and VM profiles, including when stronger isolation is required.

## Invariant families (refs)
- EXEC (envelope declaration, controls)
- AUTH/POL (admission gates)
- EVID (lifecycle events, attestation)
- DEP (envelope dependencies)
- CRP tie: EXEC-03/04 for partition/degradation where applicable

## Applicable invariant IDs
- EXEC-01/02/03/04/05, AUTH-01/02/04, POL-01/02/03/04/05, EVID-01/03/04/05, DEP-01/02/04, PHY-01/02/03 (as applicable)

## Evidence expectations
- Admission/envelope selection evidence; enforcement logs.
- Attestation results; lifecycle evidence events.
- Dependency declarations for envelope-critical paths.
- Degradation/partition behavior evidence where CRP applies.

## To cover
- Kubernetes baseline (controls, admission, policy posture).
- VM envelope profile (e.g., KubeVirt) for regulated/high-liability workloads.
- Attestation, isolation, and evidence capture expectations.

## Invariants (draft)
- Workloads MUST declare container vs. VM envelope; selection criteria MUST be policy-driven.
- Admission controls MUST enforce profile selection and required controls before execution.
- Envelope operations MUST emit evidence for lifecycle events and attestation results.

## Next steps
- Define profile triggers and mandatory controls.
- Describe conformance checks for each profile.
