# RFP Guide — ECS Evidence Support (Draft)

## Intent
Provide procurement-ready language to request ECS evidence support in a measurable, testable way.

## Required declarations (profile claims)
Suppliers MUST provide a profile claim using the template in `docs/conformance-model.md`, including:
- Supported evidence profiles (e.g., baseline, admissible, regulated-ML, NCP).
- Default evidence profile.
- Supported hash profiles.
- Export endpoints or mechanisms.
- Verifier inputs supported (chain, seals, archive refs).

## Required evidence bundles
Suppliers MUST provide export bundles that include:
- `manifest.json` with `evidence_profile_id` and (if applicable) `hash_profile_id`.
- `events.jsonl` (Core10-05 envelope with chain fields).
- `chain-segment.json` and `verifier-inputs.json`.
- Referenced artifacts (policy snapshots, authority bindings, SBOMs, etc.).

## Acceptance criteria (verifier checks)
A third-party verifier MUST be able to:
- Validate chain continuity (`sequence`, `prev_hash`, `event_hash`).
- Resolve evidence pointers and verify content-addressed integrity.
- Confirm artifacts referenced by the profile are present and immutable.
- Validate qualified timestamp/seal/anchor references when present.

## Profile-specific clauses
### Baseline / Admissible
- Supplier MUST support `ecs-evidence-baseline` at minimum.
- If `ecs-evidence-admissible` is claimed, bundles MUST include chain fields and verifier inputs.

### Regulated-ML
- Supplier MUST support `ecs-evidence-regulated-ml` when ML services are in scope.
- ML events MUST include `hash_profile_id` and required model/lineage fields.

### No-Control Profile (NCP)
- Supplier MUST support `ecs-evidence-ncp` if jurisdictional exposure is in scope.
- Bundles MUST include NCP proof artifacts (authority graph, custody model, ownership map, telemetry egress map).

## Reference materials
- Evidence export schema: `docs/evidence-export-schema.md`
- Evidence profiles: `docs/profiles/evidence-profiles.md`
- Verifier responsibilities: `docs/verifier-responsibilities.md`
- Example bundles: `docs/examples/evidence-bundles/`
- Reference adapter: `adapters/k8s-admission/`
