# ECS Profiles (Draft)

## What is a profile?
- A profile selects and/or tightens a subset of invariants for a declared scope.
- Profiles may be stricter (add constraints, evidence) but MAY NOT add new semantics or redefine invariants.
- Profiles must reference invariant IDs (e.g., AUTH-01, EXEC-03) to declare applicability.

## What profiles may do
- Subset the invariant set for a context (e.g., CRP for partition tolerance).
- Require stricter interpretation or additional evidence for selected invariants.
- Declare scope, assumptions, and non-applicability with rationale.

## What profiles may not do
- Invent new invariants or change invariant definitions.
- Bypass required invariants for the declared scope.
- Introduce vendor/tool bindings as part of the profile semantics.

## Existing profile
- CRP (Crisis Resilience Profile): a profile over the invariant set with explicit mappings in `crp/invariants.md`.

## Future profiles (examples, not defined here)
- Regulated ML (draft in `docs/profiles/regulated-ml/`)
- Regulated Critical Service
- Sovereign AI Stack

## Evidence profiles (draft)
- Evidence profiles define required evidence fields, event families, allowed hash profiles, and verifier checks.
- Draft definition in `docs/profiles/evidence-profiles.md`.

Profiles are how ECS becomes context-usable without fragmenting the invariant contract.***
