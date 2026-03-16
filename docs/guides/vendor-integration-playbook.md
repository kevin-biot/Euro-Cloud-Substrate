# Vendor Integration Playbook (Draft)

## Audience
Cloud vendor engineering teams translating ECS from docs to runtime implementation.

## Outcome
In 5 working days, ship one control-point integration with exportable evidence and verifier pass/fail outputs.

## Day 0: choose insertion point
Pick one:
- API gateway
- Object storage front door
- Queue/stream gateway
- K8s admission webhook
- ML inference sidecar

Pick one profile:
- `ecs-evidence-baseline` (start here)
- `ecs-evidence-regulated-ml`
- `ecs-evidence-ncp`

## Day 1: wire decision context
For each governed action, collect and attach:
- `policy_snapshot_id`
- `authority_snapshot_id`
- `correlation_id`
- profile fields (`evidence_profile_id`, optional `hash_profile_id`)

## Day 2: emit canonical events
Emit events for both success and denial paths:
- success: `outcome=accepted`
- denial: `outcome=refused` + `refusal_reason`
- runtime/system failure: `outcome=failed`

Use sample patterns from:
- `docs/examples/evidence-operations/`

## Day 3: attach object binding overlay
Attach governance to objects using overlay binding records:
- `object_ref`
- `purpose_id`
- `consent_token_ref`/`terms_snapshot_id` where applicable
- `jurisdiction`, `retention`, `classification`

See:
- `docs/guides/data-object-binding-model.md`
- `adapters/common/object_binding.py`

## Day 4: export bundle
Generate and publish:
- `manifest.json`
- `events.jsonl`
- `chain-segment.json`
- `verifier-inputs.json`
- `profile-claim.json`

Schema and rules:
- `docs/evidence/export-schema.md`

## Day 5: verify and gate
Run smoke checks and capture outputs in CI:
- profile declaration consistency
- chain continuity
- refusal semantics present
- artifact pointer integrity

Use:
- `docs/conformance/runtime-smoke-tests.md`

## Surface-specific recipe cards
### API gateway
- Emit `api.invoke` for request outcomes.
- For blocked calls (jurisdiction/policy), emit `outcome=refused`.

### Object storage
- Emit `object.put/get/delete` at front door.
- Emit `data.route.refuse` for blocked replication/failover.

### Queue/stream
- Emit `queue.publish/consume` and `stream.publish/subscribe`.
- Refuse non-compliant cross-jurisdiction targets explicitly.

### K8s admission
- Emit `execution.admit/refuse`.
- Bind workload to policy/authority snapshots at admission point.

### ML inference
- Emit `ml.inference` with snapshot IDs and hash-profile where required.
- Include refusal events for blocked model routing or missing governance context.

## Definition of done
- One runtime integration deployed.
- One accepted and one refused scenario exported.
- Verifier smoke checks pass in CI.
- Evidence bundle is portable without provider-private access.
