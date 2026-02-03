# Interoperability Invariants (INT) — Draft

## Scope
- Applies to standard interface exposure and interop profile declaration.
- Covers avoidance of proprietary critical-path extensions.

## Invariants
- **INT-01 — Standardised Interface Exposure**  
  Core resources MUST be exposed via documented, versioned interfaces.
- **INT-02 — No Proprietary Critical-Path Extensions**  
  Critical paths MUST NOT depend on proprietary extensions.
- **INT-03 — Interop Profile Declaration**  
  Providers MUST declare interop profile(s) and supported versions.

## Evidence expectations
- API specifications (OpenAPI/AsyncAPI) and version policy.
- Profile declarations and compatibility statements.
- Evidence of interoperability testing or conformance.

## Non-goals
- No mandate on specific API gateway or client tooling.
- No commercial interoperability certification requirements.
