# Evidence Profiles (Draft)

## Intent
Define profile-level evidence requirements without duplicating invariant semantics. Profiles constrain required fields, event families, hash profiles, and verifier checks.

## Profile identifiers (draft)
Export bundles SHOULD declare one of the following `evidence_profile_id` values:
- `ecs-evidence-baseline`
- `ecs-evidence-admissible`
- `ecs-evidence-ncp`
- `ecs-evidence-regulated-ml`

Manifests SHOULD also declare a default `hash_profile_id` when hashes are emitted (see `docs/evidence/hash-profiles.md`).

## Baseline profile
**Scope:** default evidence envelope for governed actions.

**Required fields:**
- `id`, `event_type`, `occurred_at`, `tenant_id`, `sequence`, `outcome`, `evidence_pointer`.
- `correlation_id` for governed actions.

**Required event families:**
- AUTH, POL, EVID (minimum for governed actions).

**Hash profiles:**
- Allowed `hash_profile_id`: any declared value.

**Verifier checks:**
- Chain continuity is optional; evidence pointer integrity is required.

## Admissible profile
**Scope:** evidence intended for legal admissibility or subpoena‑resilience.

**Required fields (in addition to baseline):**
- `chain_id`, `event_hash`, `prev_hash`.

**Required event families:**
- AUTH, POL, EVID, EXIT (export and chain anchoring).

**Hash profiles:**
- Allowed `hash_profile_id`: `ecs-hash-v1` (or explicitly declared alternative with documented rules).

**Verifier checks:**
- Full chain continuity validation.
- Evidence pointer integrity and retrievability.
- Artifact immutability and snapshot integrity.
- Optional qualified timestamp/seal validation when present.

## No‑Control Profile (NCP)
**Scope:** integrators/managed‑service partners demonstrating absence of possession, custody, or control.

**Required fields (in addition to baseline):**
- `artifact_type`, `artifact_ref`, `artifact_hash` for NCP events.

**Required event families:**
- AUTH, DEP, EVID (with NCP events).

**Hash profiles:**
- Allowed `hash_profile_id`: `ecs-hash-v1` for any ML‑related NCP evidence.

**Verifier checks:**
- Validate proof artifacts for authority graph, custody model, ownership map, and telemetry egress map.

## Regulated‑ML profile
**Scope:** ML inference/training evidence for regulated or high‑risk AI.

**Required fields (in addition to baseline):**
- ML inference/training payload fields as defined in `docs/evidence/catalog.md`.
- `hash_profile_id` required on ML events.

**Required event families:**
- EVID, EXEC, SUP (ML inference and training events).

**Hash profiles:**
- Allowed `hash_profile_id`: `ecs-hash-v1`.

**Verifier checks:**
- Recompute hashes using `ecs-hash-v1` rules.
- Verify policy/authority snapshot references on ML events.

## Notes
- Profiles MAY tighten requirements but MUST NOT redefine invariants.
- See `docs/evidence/verifier-responsibilities.md` for the verifier checklist used by these profiles.
