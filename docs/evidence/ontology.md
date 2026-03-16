# ECS Evidence Ontology (Draft, Non-Normative)

## Purpose
Define a shared semantic vocabulary for runtime proof events without changing ECS normative JSON schemas.

This ontology is an overlay for:
- `docs/evidence/catalog.md` (event shapes),
- `docs/evidence/export-schema.md` (bundle contract),
- `docs/evidence/terms.md` (core definitions).

## Status and scope
- Non-normative in this draft.
- JSON envelope/schema remains normative.
- Ontology terms provide semantic alignment for adapters, verifiers, and external mappings.

## Core classes
| Class | Meaning | Typical fields |
|---|---|---|
| `EvidenceEvent` | Canonical proof event for an operation outcome | `id`, `event_type`, `occurred_at`, `sequence`, `outcome`, `chain_id` |
| `Actor` | Human/service/delegate that initiated or executed an action | `actor`, `actor_details.*` |
| `Action` | Governed operation attempted or completed | `event_type`, `action` |
| `Decision` | Evaluation result at decision point | `outcome`, `refusal_reason` |
| `PolicySnapshot` | Immutable policy version in force | `policy_snapshot_id` |
| `AuthoritySnapshot` | Immutable authority map/version in force | `authority_snapshot_id` |
| `Artifact` | Content-addressed object used as evidence input/output | `evidence_pointer`, `artifact_ref`, `artifact_hash` |
| `ObjectRef` | Governed object identity (file/object/queue/stream/model/API) | `object_ref.*`, `data_product_id` |
| `ChainSegment` | Ordered event set with integrity continuity | `prev_hash`, `event_hash`, `sequence` |
| `EvidenceBundle` | Portable export unit for verification | `manifest.json`, `events.jsonl`, `chain-segment.json`, `verifier-inputs.json` |

## Core relations
| Relation | Subject -> Object | Envelope mapping |
|---|---|---|
| `acted_by` | `EvidenceEvent` -> `Actor` | `actor`, `actor_details` |
| `performs_action` | `EvidenceEvent` -> `Action` | `event_type`, `action` |
| `governed_by_policy` | `EvidenceEvent` -> `PolicySnapshot` | `policy_snapshot_id` |
| `governed_by_authority` | `EvidenceEvent` -> `AuthoritySnapshot` | `authority_snapshot_id` |
| `targets_object` | `EvidenceEvent` -> `ObjectRef` | `object_ref`, `data_product_id`, `workload_id` |
| `produces_decision` | `EvidenceEvent` -> `Decision` | `outcome`, `refusal_reason` |
| `references_artifact` | `EvidenceEvent` -> `Artifact` | `evidence_pointer`, `artifact_ref` |
| `prev_event` | `EvidenceEvent` -> `EvidenceEvent` | `prev_hash` |
| `included_in_segment` | `EvidenceEvent` -> `ChainSegment` | `chain_id`, `sequence` |
| `included_in_bundle` | `EvidenceEvent` -> `EvidenceBundle` | export manifest scope |

## Minimal concept shape
The conceptual primitive is:
`EvidenceEvent(actor, action, authority, policy, artifact, decision, outcome)`.

In ECS, this maps to existing fields and does not require a new event grammar.

## Example semantic mapping
Event:
- `event_type: policy.evaluate`
- `actor: policy-engine`
- `policy_snapshot_id: pol-2026-03-16-a`
- `authority_snapshot_id: auth-2026-03-16-a`
- `outcome: refused`
- `refusal_reason: jurisdiction_policy_violation`

Ontology interpretation:
- `EvidenceEvent` `performs_action` `Action(policy.evaluate)`
- `EvidenceEvent` `acted_by` `Actor(policy-engine)`
- `EvidenceEvent` `governed_by_policy` `PolicySnapshot(pol-2026-03-16-a)`
- `EvidenceEvent` `governed_by_authority` `AuthoritySnapshot(auth-2026-03-16-a)`
- `EvidenceEvent` `produces_decision` `Decision(refused)`

## Profile semantics (overlay)
Profiles constrain required semantic relations:
- Baseline: requires core `EvidenceEvent` + decision + chain continuity.
- Regulated-ML: additionally requires dataset/object lineage and hash-profile semantics.
- NCP: additionally requires authority/custody/ownership telemetry proof artifacts.

See `docs/profiles/evidence-profiles.md`.

## Machine-readable context
A draft JSON-LD context is provided at:
- `docs/evidence/ontology-context.jsonld`

This context is optional in current ECS implementations and intended for interoperability experiments.
