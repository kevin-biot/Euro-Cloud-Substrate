# Airbus‑style Procurement Checklist (2026) — Draft

## Intent
Provide a practical, year‑1 procurement checklist for a large European buyer seeking ECS‑aligned evidence, portability, and jurisdictional safeguards.

## Minimum profile requirements (Year‑1)
- **Required profiles:** `ecs-evidence-baseline` and `ecs-evidence-admissible`
- **Optional profiles:** `ecs-evidence-regulated-ml` (if AI workloads), `ecs-evidence-ncp` (if non‑EU exposure risk)

## Required supplier declarations (profile claims)
Supplier MUST provide:
- Supported evidence profiles (baseline/admissible required)
- Default evidence profile
- Supported hash profiles (if ML scope)
- Export endpoints and mechanisms
- Verifier inputs supported (chain_id, prev_hash, event_hash, archive_ref)

Template: `docs/conformance-model.md` (Profile claims)

## Evidence bundle acceptance criteria
Supplier MUST provide example bundles (or live exports) that include:
- `manifest.json` with `evidence_profile_id`
- `events.jsonl` (Core10‑05 envelope + chain fields)
- `chain-segment.json` + `verifier-inputs.json`
- Referenced artifacts (policy snapshots, authority bindings, SBOMs if ML)

## Verifier checks (required)
A third‑party verifier MUST be able to:
- Validate chain continuity (`sequence`, `prev_hash`, `event_hash`)
- Resolve evidence pointers and verify content‑addressed integrity
- Confirm artifacts for the declared profile are present and immutable

## Portability / exit
Supplier MUST demonstrate:
- Export bundle generation within agreed time window
- Migration validation evidence per Core10‑10
- Refusal evidence when policy/authority blocks export

## AI workloads (if in scope)
- Require `ecs-evidence-regulated-ml`
- ML events MUST include `hash_profile_id`
- Evidence bundles must include model SBOM + training/inference events

## Jurisdictional risk (if in scope)
- Require `ecs-evidence-ncp`
- Provide NCP proof artifacts (authority graph, key custody model, ownership map, telemetry egress map)

## Demonstration requirement (recommended)
Supplier SHOULD run the reference demo flow:
- `docs/demo-flow.md`
- Provide exported bundle and verifier inputs for review

## References
- RFP Guide: `docs/rfp-evidence-support.md`
- Evidence profiles: `docs/profiles/evidence-profiles.md`
- Verifier responsibilities: `docs/verifier-responsibilities.md`
- Example bundles: `docs/examples/evidence-bundles/`
