# ADR-0004: IRN Alignment Is Mechanism-Only

## Status
Accepted

## Context
The IRN crosswalk (`docs/irn-mapping.md`) maps IRN “what” to ECS “how” via invariants and evidence. ECS is not a certification or scoring scheme.

## Decision
- IRN mapping is non-normative and mechanism-only; it does not define scoring, compliance labels, or certification.
- ECS will map IRN criteria to existing invariants and evidence expectations; no new invariants are introduced to satisfy IRN.
- IRN meta-criteria (e.g., executive sponsorship) remain out of scope for ECS.

## Consequences
- Prevents ECS from being treated as a certification scheme.
- Keeps IRN alignment grounded in existing invariants and evidence.
- Changes to IRN mappings do not alter ECS semantics; they update crosswalk guidance only.***
