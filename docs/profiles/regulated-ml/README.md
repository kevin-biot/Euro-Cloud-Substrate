# Regulated ML Profile (Draft)

Profile goal: tighten ECS invariants for regulated ML workloads (e.g., AI Act, finance/health/public sector).

## Scope
- Applies to training and inference workloads using models with regulatory impact.
- Focuses on model/data provenance, execution envelopes for accelerators, and evidence for decision-time behavior.

## Applicable invariant families (refs)
- DATA (residency/classification for training data and artifacts)
- SUP (model SBOM/provenance)
- EVID (decision-time logging, immutable evidence)
- EXEC (inference/training envelopes, accelerator isolation)
- DEP (critical-path dependencies for accelerators/storage)
- OPS (runbooks/drills for ML operations)

## Draft requirements (to be refined)
- Model provenance: declare training data lineage, model SBOM, and fine-tuning provenance (SUP, DATA).
- Data-use posture: bind training to a declared data-use posture and exclusion policy snapshot; reference dataset manifest (DSBOM).
- Inference envelopes: declare GPU/accelerator envelope with attestation and isolation evidence (EXEC, DEP).
- Decision logging: capture input/context hashes, policy snapshot, authority, and outputs/refusals (EVID).
- Residency: enforce jurisdiction for training data, checkpoints, and models (DATA).
- Evidence: link model artifacts and inferences to evidence pointers; integrity on checkpoints (EVID, SUP).

## Non-goals
- No scoring or certification.
- No specific ML frameworks mandated.
- No policy/ethics content beyond enforceable invariants.

## Status
- Draft; no additional invariants introduced. References existing invariant IDs per `docs/invariants/v0.3.md`.
