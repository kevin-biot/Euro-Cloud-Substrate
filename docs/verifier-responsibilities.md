# Verifier Responsibilities (Draft)

## Intent
Define what an independent verifier must be able to validate **without platform access** to treat ECS evidence as auditable.

## Required checks
1. **Chain continuity**
   - Verify `sequence` order and `prev_hash` linkage.
   - Verify `chain_id` consistency across exported segments.

2. **Profile declaration**
   - Confirm `evidence_profile_id` and (if used) `hash_profile_id` are declared in the export manifest.
   - Execute verifier checks against the selected evidence profile.

3. **Evidence pointer integrity**
   - Dereference `evidence_pointer` and validate content‑addressing (hash matches).
   - Validate tenant scoping and retrievability class where metadata is present.

4. **Signature / seal verification (if present)**
   - Verify signatures over manifest + bundle hash.
   - Validate qualified timestamp/seal references when supplied.

5. **Authority / policy immutability**
   - Verify referenced authority/policy snapshots exist and are immutable.
   - Confirm snapshot references are consistent across related events (`correlation_id`).

6. **No‑Control Profile (NCP) artifacts**
   - Validate that “declare/publish” events reference proof artifacts (authority graph, custody model, ownership map, telemetry egress map).
   - Confirm artifact hashes match the referenced content.

## Minimum verifier inputs
- Evidence export bundle (manifest + chain segment + events).
- Referenced artifacts or resolvable artifact pointers.
- Optional trust service references (timestamp/seal/archive).

## Non‑goals
- Does not mandate storage backends or archive providers.
- Does not prescribe how providers generate evidence, only how verifiers validate it.
