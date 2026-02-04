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

## Terms (WS3 scope)
- **execution envelope**: Declared runtime profile (container/VM/TEE) with required controls.
- **admission gate**: Policy/authority decision point that validates envelope declaration before execution.
- **attestation evidence**: Proof of runtime integrity (TEE/vTPM/driver manifest) captured as evidence.
- **envelope dependency**: Critical dependency required to execute an envelope (hypervisor, runtime, key service).
- **evidence buffer**: Local, tamper‑evident store for evidence emitted during partitions.

## Sections to draft
- Kubernetes baseline controls (admission, policy, isolation).
- VM envelope profile, isolation level, and usage criteria.
- Attestation, logging, and evidence requirements.
- Interface points with Policy/Authority and Interop APIs.
- CRP-specific behavior for envelopes under partition (local control-plane, lifecycle, evidence buffering).

## Envelope selection rules (draft)
- Container profile is DEFAULT for low/medium risk workloads.
- VM or TEE profile is REQUIRED when policy mandates stronger isolation (classification, regulated‑ML, NCP, tenant tier).
- Policy MUST explicitly define triggers for VM/TEE selection and refusal criteria.

## Requirements (draft v1)
- Workloads MUST declare an execution envelope (container, VM, or other profile).
- Admission MUST validate envelope declaration against policy; refusals are first‑class and evidenced.
- Envelope lifecycle events (create/start/stop/destroy) MUST emit evidence.
- Attestation MUST be captured where available; critical dependencies MUST be declared.
- Envelopes MUST honor jurisdiction/residency constraints and tenant isolation.

### Container profile (draft)
- Runtime isolation (hardened runc, gVisor, Kata, or equivalent).
- Mandatory controls: seccomp/apparmor or equivalent; read‑only filesystem where feasible.
- Image provenance and integrity verification (SUP‑01/04).
- Network/policy enforcement aligned with tenant isolation.
- Evidence: admission decision, image integrity check, policy snapshot id, outcome.

### VM profile (draft)
- Hypervisor isolation; vTPM/TEE attestation where available.
- Boot integrity verification; driver/firmware provenance (SUP‑01/04).
- Enforced network/policy posture consistent with tenant isolation.
- Evidence: attestation report reference and pass/fail outcome.

### TEE/Confidential profile (draft)
- Required when policy mandates hardware‑backed isolation.
- Attestation MUST include report reference, platform type, and verification result.
- Evidence MUST be recorded for admission and periodic re‑attestation.

## Evidence and export alignment
- Envelope events MUST use the Core10‑05 envelope.
- Export bundles MUST declare `evidence_profile_id` and include chain fields where required by the selected profile.
- Evidence emitted during partitions MUST be buffered locally and reconciled post‑partition.

## CRP behavior (partition tolerance)
- CRP‑designated envelopes MUST continue under local control when the upstream scheduler/control plane is unavailable.
- Admission decisions during partition MUST be locally enforceable and evidenced.
- If policy cannot be evaluated, governed actions MUST fail‑closed with refusal evidence.
