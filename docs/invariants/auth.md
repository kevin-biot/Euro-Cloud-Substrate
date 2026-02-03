# Authority Invariants (AUTH) — Draft

## Scope
- Applies to authority binding, verification, and refusal for governed actions.
- Covers authority boundaries, delegation, and offline survivability.

## Invariants
- **AUTH-01 — Local Authority Satisfiability**  
  Authority checks MUST be satisfiable locally for governed actions.
- **AUTH-02 — No Hard Upstream Authority Dependency**  
  Critical actions MUST NOT require uninterrupted upstream authority calls.
- **AUTH-03 — Authority Plane Separation**  
  Authority verification MUST be separable from execution/data planes.
- **AUTH-04 — Explicit Authority Refusal**  
  Refusals MUST be explicit and evidenced, not silent failures.
- **AUTH-05 — Authority Boundary Declaration**  
  Authority boundaries and scopes MUST be declared and auditable.

## Evidence expectations
- Authority binding records with scope, issuer, validity window, and proof.
- Refusal logs with reason codes and snapshot ids.
- Boundary declarations for delegated authority.

## Non-goals
- No mandate on identity provider or certificate authority choices.
- No organizational governance model specification.
