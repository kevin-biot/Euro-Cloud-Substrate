# Regulated ML Profile — Spec (Draft)

## Scope
- Applies to training and inference workloads with regulatory impact (e.g., AI Act high-risk, finance, health, public sector).
- Tightens existing invariants; no new invariants introduced.

## Invariant families (refs)
- DATA: residency/classification for training data, checkpoints, models.
- SUP: model SBOM/provenance.
- EVID: decision-time logging, immutable evidence.
- EXEC: envelopes for accelerators (GPU/TPU), isolation/attestation.
- DEP: critical-path dependencies for accelerators/storage.
- OPS: runbooks/drills for ML operations.

## Applicable invariant IDs
- DATA-01/02/05, SUP-01/02/03/04, EVID-01/03/04, EXEC-01/02/05, DEP-01/02/04, AUTH-01/04, POL-01/02/04, OPS-01/02/04, PHY-01/03, EXIT-01/02

## Requirements (draft)

### Model SBOM and provenance (SUP, DATA)
- SBOM MUST be provided for models/artifacts (CycloneDX 1.5+ recommended).
- SBOM content (minimum):
  - `bom-ref`, `type` = "machine-learning-model", `name`, `version`
  - `hashes`: SHA-256 of model weights/artifacts
  - Model card fields: `modelType` (classification/regression/generative/etc.), `architecture` (transformer/cnn/etc.), `quantization` (if applicable)
  - Training data references: dataset identifiers (with governance metadata links)
  - External references: training code version, hyperparameters location, base model lineage
- Provenance MUST include base model lineage, fine-tuning dataset identifiers, and training code version.
- Training data residency/classification MUST be declared and enforced (DATA-01/02).

### Training governance (DATA, EVID)
- Training runs MUST record: dataset hashes/IDs, code version, hyperparameters, checkpoints with integrity hashes.
- Checkpoints MUST have integrity metadata and evidence of storage location/jurisdiction.
- Training MUST honor residency for data, checkpoints, and intermediate artifacts.

### Inference envelopes (EXEC, DEP, PHY)
- Inference workloads MUST declare an execution envelope with accelerator requirements (GPU/TPU).
- Accelerator isolation/attestation evidence MUST be captured. Providers MUST support at least one:
  - vTPM attestation (TPM 2.0 quotes/PCRs for driver/firmware)
  - Confidential computing attestation (e.g., AMD SEV-SNP, Intel TDX, NVIDIA CC)
  - Signed driver manifest (cryptographic signature on driver/runtime version)
- Attestation evidence MUST include: attestation type, timestamp, verification result (pass/fail), attestation report reference.
- Critical-path dependencies (accelerator drivers/runtime/storage) MUST be declared (DEP).

### Decision logging (EVID)
- Inference events MUST capture: input/context hash, model version/SBOM ref, policy/authority snapshot, decision output/refusal, outcome.
- Logs MUST be immutable, ordered, and integrity-protected; refusal is first-class.
- Evidence pointers MUST be associated with inference events for audit/export.

### Residency and portability (DATA, EXIT)
- Models and artifacts MUST declare residency; moves/exports MUST be evidenced.
- Portability expectations: export of model + SBOM + evidence, with integrity.

## Non-goals
- No scoring/certification.
- No mandate of specific ML frameworks.
- No policy/ethics content beyond enforceable invariants.
