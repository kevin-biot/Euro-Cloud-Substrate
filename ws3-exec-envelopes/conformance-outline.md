# WS3 Conformance Outline (Draft)

## Profiles and admission
- Verify admission policies enforce profile selection (container vs. VM) based on declared requirements.
- Test VM envelope requirements for regulated/high-isolation workloads.
 - Verify refusal paths emit evidence with policy snapshot IDs and refusal reasons.

## Isolation and controls
- Validate isolation controls (network, storage, compute) per profile.
- Verify attestation/evidence capture for lifecycle events.
 - Verify image provenance/integrity checks for container profiles.
 - Verify vTPM/TEE attestation evidence for VM/TEE profiles where available.

## CRP scenarios (partition tolerance)
- Simulate loss of upstream scheduler/control plane; CRP-designated envelopes MUST continue under local control.
- Validate lifecycle operations (start/stop/restart) locally for CRP envelopes.
- Verify evidence buffering locally during partition with later reconciliation (WS5).
 - Validate fail‑closed behavior when policy cannot be evaluated during partition.

## Evidence export
- Export bundles MUST declare `evidence_profile_id` and include chain fields required by the selected profile.
