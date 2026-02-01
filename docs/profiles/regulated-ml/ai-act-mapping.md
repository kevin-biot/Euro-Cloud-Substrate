# Regulated ML Profile — AI Act Mapping (Draft, Non-Normative)

## Purpose
Map AI Act expectations to ECS “how” (invariants/evidence). This is mechanism-only; no compliance claims.

## Mapping (indicative)
- High-risk system governance → AUTH/POL/EXEC/EVID: authority-before-execution, deterministic policy, evidence by construction.
- Data governance/quality → DATA/SUP: dataset residency/classification, SBOM/provenance for models/artifacts.
- Record-keeping/logging → EVID: decision-time logging (input/context hash, model version, policy snapshot), immutable audit chain.
- Transparency/traceability → SUP/EVID: model lineage, training provenance, inference evidence export.
- Robustness/accuracy (operational) → EXEC/DEP: declared inference envelopes, dependency declarations, attestation where available.

## Notes
- ECS provides mechanism; AI Act obligations remain with the provider/operator.
- No scoring or certification implied.
