# Auditor/Verifier Guide (Draft)

## Who this is for
Internal audit teams and independent verifiers evaluating ECS evidence claims.

## Goal
Validate claims from export bundles without relying on provider-private systems.

## Verification sequence
1. **Profile integrity**
   - Confirm `evidence_profile_id` and `profile_version`.
   - Confirm `producer_identity` and `verifier_expectations_ref`.
2. **Chain integrity**
   - Validate `sequence`, `prev_hash`, `event_hash`, and `chain_id`.
   - Validate segment/bundle hash methods from verifier inputs.
3. **Pointer/artifact integrity**
   - Resolve evidence/artifact references.
   - Validate content-addressed integrity and immutability expectations.
4. **Refusal semantics**
   - Confirm denied actions produce refusal events.
   - Validate refusal anchors: policy snapshot + authority snapshot + reason class/code.
5. **Claim consistency**
   - Validate profile claim aligns with emitted events and required fields.

## Mandatory red flags
- Missing refusal events for denied actions.
- Generic error responses with no evidence anchors.
- Profile drift across profile-claim/manifest/events.
- Evidence pointers not independently resolvable.
- Chain continuity break not declared as known gap.

## Outputs
- Pass/fail per check.
- Gap list with severity and evidence path.
- Statement on whether validation required privileged access.

## References
- `docs/evidence/verifier-responsibilities.md`
- `docs/evidence/export-schema.md`
- `docs/evidence/refusal-semantics.md`
- `docs/profiles/evidence-profiles.md`
