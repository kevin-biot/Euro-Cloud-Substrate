# Gaia-X Alignment Note (Draft, Non-Normative)

## Intent
Provide a lightweight mapping between ECS data invariants and data-space concerns commonly associated with Gaia-X. This note is non-normative and does not prescribe governance or specific implementation choices.

## Scope
- Focuses on data portability, evidence export, and policy binding gaps that frequently appear in data-space discussions.
- Avoids policy or institutional positions; only addresses technical gaps ECS can address.

## Gaps ECS addresses (draft)
1. **Deterministic evidence export**  
   Data access and lineage often lack portable, cryptographically verifiable export packages. ECS provides a normative export schema.
2. **Policy snapshot binding**  
   Data usage decisions require stable policy references; ECS enforces policy snapshot ids in evidence.
3. **Consent/intent binding**  
   Purpose/consent is often UI-bound rather than machine-verifiable; ECS defines consent/intent token references.
4. **Standardized data product descriptors**  
   Data sharing requires a minimal, portable metadata contract; ECS defines a draft descriptor.
5. **Pre-hoc compliance**  
   Evidence must be generated at decision time, not reconstructed post-hoc; ECS mandates pre-hoc evidence generation.

## ECS components that address these gaps
| Gap | ECS component | Reference |
|---|---|---|
| Evidence export | Evidence Export Schema | `docs/evidence-export-schema.md` |
| Policy binding | Policy Snapshot Pattern | `docs/compliance-pattern-library.md` |
| Consent binding | Consent/Intent Token Pattern | `docs/compliance-pattern-library.md` |
| Data product metadata | DATA invariants (descriptor) | `docs/invariants/data.md` |
| Pre-hoc evidence | Evidence Event Model / Audit Chain | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-baseline.md` |

## Notes
- This document is intended to help reviewers understand how ECS can serve as a technical substrate for data-space initiatives.
- It does not assert compatibility with any single governance regime; mappings are conceptual.
- ECS is business-model neutral but provides evidence-grade primitives that enable usage attribution and monetisation without prescribing pricing.
