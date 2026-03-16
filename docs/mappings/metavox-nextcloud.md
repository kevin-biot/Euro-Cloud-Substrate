# MetaVox + Nextcloud Mapping (Draft, Non-Normative)

## Purpose
This mapping shows how MetaVox file metadata can be used as an ECS metadata input layer, with ECS adapters emitting audit-grade events and export bundles.

MetaVox metadata alone is not a substitute for ECS evidence chain, refusal semantics, or verifier-ready export.

## Storage model and portability implication
MetaVox metadata is stored as Nextcloud app data keyed to Nextcloud object IDs (file/team-folder), not embedded into file formats such as PDF metadata blocks, EXIF, or XMP.

Implications:
- Metadata is non-intrusive and format-agnostic.
- Moving files outside Nextcloud without an export/mapping step can lose governance context.
- ECS adapters should export metadata + evidence as portable artifacts/bundles so verifier workflows are independent of Nextcloud internals.

## Integration pattern (minimal)
1. Define MetaVox fields aligned to ECS keys.
2. Trigger adapter emission on file + metadata lifecycle events.
3. Emit ECS events with snapshot refs and outcomes.
4. Export verifier bundles with `evidence_profile_id`.

## Field mapping (MetaVox -> ECS)
| MetaVox field (example) | ECS field | Used in events | Notes |
|---|---|---|---|
| `ecs_data_product_id` | `data_product_id` | `data.product.publish`, `data.transform.link` | Stable identifier for file/data product |
| `ecs_purpose_id` | `purpose_id` | `data.purpose.bind`, `data.transform.link` | Required for governed use |
| `ecs_consent_ref` | `consent_token_ref` | `data.consent.bind`, `data.transform.link` | Reference only; consent proof stays external |
| `ecs_terms_snapshot_id` | `terms_snapshot_id` | `data.terms.attach`, `data.transform.link` | Binds usage terms/version |
| `ecs_jurisdiction` | `jurisdiction` | DATA + EVID events | Used for routing and retention checks |
| `ecs_retention` | `retention` | DATA + EVID events | Needed for deletion propagation checks |
| `ecs_classification` | `classification` | DATA, EXEC, EVID | Drives policy conditions |
| `ecs_lineage_parents` | `parent_refs[]` | `data.transform.link` | Parent-child continuity |
| `ecs_transform_type` | `transform_type` | `data.transform.link` | e.g., redact, extract, summarize |
| `ecs_quality_score` | `quality_score` | `policy.outcome.measure` | Optional but useful for policy learning loops |

## Event trigger matrix (recommended)
| Nextcloud/MetaVox trigger | ECS event(s) | Minimum required fields |
|---|---|---|
| New governed file published | `data.product.publish` | `data_product_id`, `jurisdiction`, `retention`, `policy_snapshot_id`, `authority_snapshot_id`, `outcome` |
| Purpose metadata set/changed | `data.purpose.bind` | `data_product_id`, `purpose_id`, snapshots, `outcome` |
| Consent metadata set/changed | `data.consent.bind` | `data_product_id`, `consent_token_ref`, snapshots, `outcome` |
| Terms metadata set/changed | `data.terms.attach` | `data_product_id`, `terms_snapshot_id`, snapshots, `outcome` |
| Derived file created (transform/export/redaction) | `data.transform.link` | `data_product_id`, `parent_refs`, `transform_type`, `purpose_id`, snapshots, `outcome` |
| Policy effectiveness measured | `policy.outcome.measure` | `policy_snapshot_id`, `measured_event_type`, `metric_id`, `metric_value`, `outcome` |
| Rule change applied | `policy.rule.update` | `policy_snapshot_id`, `rule_id`, `updated_rule_hash`, `supersedes_snapshot_id`, `outcome` |
| Policy blocks action (share/export/move) | refusal event in family (DATA/POL/EXEC) | `outcome=refused`, `refusal_reason`, snapshots, `correlation_id` |

## Profile and verifier notes
- Always include `evidence_profile_id` in export manifests.
- Include `hash_profile_id` when ML evidence is present or required by profile.
- For regulated/sovereignty scenarios, verifier checks should include:
  - parent-child lineage continuity,
  - purpose/consent/terms propagation,
  - deletion/rectification propagation evidence.

## Minimal adapter responsibilities
- Read MetaVox metadata and Nextcloud context.
- Resolve policy and authority snapshots at decision time.
- Emit ECS events with `accepted`/`refused` outcomes.
- Write chain-ready evidence and export bundle artifacts.
