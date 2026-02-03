# Conformance Model (Draft)

Scope: define how ECS conformance is expressed without scoring or certification.
See `docs/terms.md` for canonical evidence event/artifact/bundle terminology.

## Principles
- Evidence-driven: claims are backed by evidence artifacts, not assertions.
- Per-invariant basis: each invariant is evaluated independently.
- No scoring, maturity levels, or “ECS compliant” labels.

## States per invariant
- **Satisfied:** evidence demonstrates the invariant holds for the declared scope.
- **Violated:** evidence shows the invariant is not met.
- **Not applicable:** invariant does not apply to the declared scope (must be justified).

## Evidence expectations (examples)
- Declarative artifacts (policies, profiles, dependency declarations, residency boundaries).
- Operational evidence (logs/events per IALP/WS5, audit chains).
- Tests/exercises (drills, fail-closed refusals, partition scenarios) with captured evidence.
- Evidence bundles annotate `evidence_profile_id` and `hash_profile_id` when applicable.

## Claims
- A conformance claim specifies: scope, invariants included/excluded (with rationale), evidence locations/ids, date/version of policies used, and the selected evidence profile.
- Evidence profile selection (e.g., baseline, admissible, NCP, regulated‑ML) constrains required fields, hash profile ids, and verifier checks (see `docs/profiles/evidence-profiles.md`).
- Profiles (e.g., CRP) should reference invariant IDs to indicate their required subset.

### Profile claims (template)
```yaml
implements:
  evidence_profiles: [ecs-evidence-baseline, ecs-evidence-admissible]
  default_evidence_profile: ecs-evidence-baseline
  hash_profiles: [ecs-hash-v1]
  export_endpoints:
    - /v1/events
    - /v1/exports
  verifier_inputs_supported:
    - chain_id
    - prev_hash
    - event_hash
    - qualified_timestamp
    - archive_ref
```

## Out of scope
- Certification schemes, labels, or scoring models are not defined here.
