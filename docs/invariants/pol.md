# Policy Invariants (POL) — Draft

## Scope
- Applies to policy artifacts, evaluation, and enforcement for governed actions.
- Covers determinism, completeness, and fail-closed behavior.

## Invariants
- **POL-01 — Policy as Versioned Artifact**  
  Policies MUST be versioned, immutable artifacts with provenance.
- **POL-02 — Deterministic Policy Evaluation**  
  Given identical inputs and policy snapshot, outcomes MUST be identical.
- **POL-03 — Complete Enforcement Coverage**  
  All governed actions MUST be subject to policy evaluation.
- **POL-04 — Fail-Closed on Policy Uncertainty**  
  If policy state is uncertain, actions MUST be refused.
- **POL-05 — Last-Known-Good Policy Fallback**  
  Systems MAY use a last-known-good policy snapshot with evidence.

## Evidence expectations
- Policy artifact registry (version, hash, issuer).
- Evaluation traces and outcome logs tied to snapshot ids.
- Refusals and fallbacks with evidence pointers.

## Non-goals
- No mandated policy language or engine.
- No legal interpretation guidance beyond enforceable policy artifacts.
