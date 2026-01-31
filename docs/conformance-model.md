# Conformance Model (Draft)

Scope: define how ECS conformance is expressed without scoring or certification.

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

## Claims
- A conformance claim specifies: scope, invariants included/excluded (with rationale), evidence locations/ids, and date/version of policies used.
- Profiles (e.g., CRP) should reference invariant IDs to indicate their required subset.

## Out of scope
- Certification schemes, labels, or scoring models are not defined here.
