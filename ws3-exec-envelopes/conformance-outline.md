# WS3 Conformance Outline (Draft)

## Profiles and admission
- Verify admission policies enforce profile selection (container vs. VM) based on declared requirements.
- Test VM envelope requirements for regulated/high-isolation workloads.

## Isolation and controls
- Validate isolation controls (network, storage, compute) per profile.
- Verify attestation/evidence capture for lifecycle events.

## CRP scenarios (partition tolerance)
- Simulate loss of upstream scheduler/control plane; CRP-designated envelopes MUST continue under local control.
- Validate lifecycle operations (start/stop/restart) locally for CRP envelopes.
- Verify evidence buffering locally during partition with later reconciliation (WS5).
