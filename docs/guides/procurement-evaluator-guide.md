# Procurement Evaluator Guide (Draft)

## Who this is for
Procurement authorities and solution evaluators comparing provider submissions.

## Goal
Assess claims using evidence artifacts, not marketing statements.

## Evaluation flow
1. **Check declared profile support**
   - Review `profile-claim.json`.
   - Confirm selected profile is stated in `manifest.json`.
2. **Check artifact completeness**
   - Require bundle package:
     - `manifest.json`
     - `events.jsonl`
     - `chain-segment.json`
     - `verifier-inputs.json`
     - `profile-claim.json`
3. **Run verifier-facing checks**
   - Chain continuity and pointer integrity.
   - Profile self-description consistency.
   - Refusal evidence for denied actions.
4. **Assess scheme alignment**
   - Use mapping set under `docs/mappings/` (EUCS, EU Cloud CoC, CSF, sovereignty matrix).
   - Record threshold pass vs score differentiators.
5. **Decide with gap controls**
   - Accept only with explicit gaps, compensating controls, and retest dates.

## Minimum acceptance baseline
- Bundle is independently verifiable.
- Refusal semantics are explicit and policy/authority anchored.
- Profile claim, manifest, and events are consistent.
- No hidden requirement for provider-private systems to verify core claims.

## Recommended scoring hooks
- Threshold critical:
  - profile conformance
  - verifier portability
  - refusal evidence quality
- Differentiators:
  - depth of supply-chain and sovereignty artifacts
  - ops parity and migration evidence quality

## References
- `docs/procurement/rfp-guide.md`
- `docs/mappings/certification-intake-matrix.md`
- `docs/mappings/eu-sovereignty-assurance-matrix.md`
- `docs/mappings/ec-cloud-sovereignty-framework-mapping.md`
