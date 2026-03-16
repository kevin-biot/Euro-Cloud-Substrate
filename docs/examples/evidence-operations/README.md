# Evidence Operations Samples (Draft)

## Purpose
Provide canonical JSONL examples for common operation-level evidence emission.

These samples are intended to be copy/paste references for adapters and SDKs. They complement:
- `docs/evidence/catalog.md` (event families/shapes)
- `docs/evidence/export-schema.md` (bundle/manifest contract)

## Conventions used in all samples
- Core envelope fields included: `id`, `event_type`, `occurred_at`, `tenant_id`, `sequence`, `outcome`, `evidence_pointer`.
- Chain continuity shown with `chain_id`, `event_hash`, `prev_hash`.
- Profile self-description shown with `evidence_profile_id` (and `hash_profile_id` where relevant).
- Governed decisions include `correlation_id`, `policy_snapshot_id`, and `authority_snapshot_id` when applicable.
- Refusals are explicit (`outcome: refused`) with `refusal_reason`.

## Sample files
- `auth-check.jsonl`
- `policy-evaluate.jsonl`
- `workload-admit-refuse.jsonl`
- `object-put-get-refuse.jsonl`
- `queue-publish-consume-refuse.jsonl` (includes `stream.publish` / `stream.subscribe`)
- `api-invoke-refuse.jsonl`
- `data-transform-lineage.jsonl`

Verifier input: `evidence_profile_id` MUST match the declared profile in the export manifest.
