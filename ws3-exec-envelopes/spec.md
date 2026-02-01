# WS3 Spec (Draft)

## Objectives
- Define container and VM execution envelope profiles for ECS.

## Invariant families (refs)
- EXEC (envelopes, controls, degradation)
- AUTH/POL (admission gates, refusal)
- EVID (lifecycle events, attestation)
- DEP (envelope dependencies)
- PHY (connectivity assumptions)
- CRP ties: EXEC-03/04, AUTH-01/02 under partition

## Sections to draft
- Kubernetes baseline controls (admission, policy, isolation).
- VM envelope profile, isolation level, and usage criteria.
- Attestation, logging, and evidence requirements.
- Interface points with Policy/Authority and Interop APIs.
- CRP-specific behavior for envelopes under partition (local control-plane, lifecycle, evidence buffering).
