# Qualified Archiving for Evidence (Draft)

## Intent
Explain how evidence chains can be anchored to qualified archiving services without storing every event in a trust service.

## Why this matters
- Courts and regulators often rely on **qualified trust services** for strong integrity and timestamp assurances.
- Storing every evidence event in a qualified archive is impractical; anchoring a hash chain provides legal strength with scalability.

## Anchoring pattern (overview)
1. **Local evidence chain** emits events with `sequence` + `prev_hash`.
2. **Periodic anchor** computes a Merkle root or chain head hash for a segment.
3. **Archive submission** stores the anchor in a qualified archiving service.
4. **Export manifest** records `archive_ref` + `anchor_interval` (and declares `evidence_profile_id` / `hash_profile_id`).
5. **Verification** recomputes the anchor hash and confirms it matches the qualified archive record.

## Recommended fields (aligned with ECS)
- `archive_ref`: reference to qualified archive record.
- `anchor_interval`: anchoring cadence (e.g., `P1D`).
- `anchor_hash`: hash of chain segment.
- `from_sequence` / `to_sequence`: segment boundaries.

## ECS references
- Evidence export: `docs/evidence/export-schema.md`
- Evidence events: `docs/evidence/catalog.md` (chain.anchor)
- Audit chain baseline: `core10/06-audit-chain-baseline.md`

## Notes
- This is non‑normative guidance; implementations may vary by qualified trust service provider.
