# Regulated ML Profile — Conformance (Draft)

Conformance is evidence-driven. No scoring/certification.

## Criteria (draft)
- SBOM/provenance: Model artifacts include SBOM (e.g., CycloneDX) with base model, training data identifiers, and code version.
- Training evidence: Training runs record dataset hashes/IDs, hyperparameters, checkpoints with integrity and residency evidence.
- Inference envelope: Inference workloads declare accelerator envelope; isolation/attestation evidence captured.
- Decision logging: Inference events log input/context hash, model version/SBOM ref, policy/authority snapshot, outcome/refusal.
- Integrity: Checkpoints and models include integrity metadata; verification evidence recorded.
- Residency: Models, checkpoints, and logs honor declared residency; moves/exports evidenced.
- Audit/export: Evidence for training/inference is exportable in a provider-neutral format.

Each criterion links to invariant IDs; refusal/exception are valid outcomes and MUST be evidenced.
