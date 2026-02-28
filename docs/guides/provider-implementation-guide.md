# Provider Implementation Guide (Draft)

## Who this is for
Cloud/platform engineering teams implementing ECS evidence support.

## Goal
Implement one profile end-to-end with exportable, verifier-friendly evidence in 7 days.

## Day 1: Select scope and profile
- Choose one insertion point: `adapters/k8s-admission/`, `adapters/ml-inference-sidecar/`, or `adapters/object-storage-proxy/`.
- Select `evidence_profile_id` (start with `ecs-evidence-baseline`).
- Define issuer/producer identity values used in exports.

## Day 2-3: Emit Core10-05 events
- Ensure events include required envelope fields.
- Emit explicit refusal events (`outcome=refused`) for denied actions.
- Include policy/authority snapshot anchors for governed actions.
- Refusal field requirements: `docs/evidence/refusal-semantics.md`.

## Day 4: Export bundle (self-describing)
- Generate `manifest.json`, `events.jsonl`, `chain-segment.json`, `verifier-inputs.json`, `profile-claim.json`.
- Ensure exports include:
  - `evidence_profile_id`
  - `profile_version`
  - `producer_identity`
  - `verifier_expectations_ref`

## Day 5: Run verifier checks
- Validate profile claim vs manifest profile.
- Validate chain continuity and pointer integrity.
- Validate refusal events against policy/authority snapshots.
- Verifier checklist: `docs/evidence/verifier-responsibilities.md`.

## Day 6-7: Package for pilot/procurement
- Produce a pilot artifact pack (`pilots/README.md`).
- Add one accepted and one refused scenario with evidence.
- Publish gap list + compensating controls.

## Definition of done
- One profile implemented end-to-end.
- Independent verifier can validate bundle without platform-private access.
- Refusal semantics are explicit and auditable.
