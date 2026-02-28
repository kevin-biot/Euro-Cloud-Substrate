# European Commission Cloud Sovereignty Framework Mapping (Draft, Non-Normative)

## Purpose
Map the European Commission DG DIGIT **Cloud Sovereignty Framework (CSF) v1.2.1 (Oct 2025)** objectives (SOV-1..SOV-8) to ECS invariants, profiles, and evidence artifacts.

This mapping is for architecture and procurement alignment. It does not claim certification.

## Why this is critical for ECS
The CSF is structured around:
- objective-by-objective assurance (SOV-1..SOV-8),
- minimum assurance thresholds (SEAL levels) per objective,
- supporting evidence used in tender evaluation.

ECS is the execution/evidence layer that can make those objective claims testable and portable across providers.

## CSF objective crosswalk
| CSF objective | ECS mapping (Core10 / WS / docs) | Invariant families (primary) | Evidence expected |
|---|---|---|---|
| SOV-1 Strategic Sovereignty | `core10/04-policy-authority-interface.md`, `docs/domains/sovereignty-assurance.md`, `docs/conformance/model.md` | AUTH, POL, DEP | Authority map, control-plane ownership declarations, change-of-control artifacts |
| SOV-2 Legal & Jurisdictional Sovereignty | `core10/01-olz-eu-baseline.md`, `core10/03-eosc-metadata-spec.md`, `docs/domains/federation.md` | AUTH, DATA, POL | Jurisdiction metadata, legal-demand/refusal evidence, policy snapshot references |
| SOV-3 Data & AI Sovereignty | `core10/03-eosc-metadata-spec.md`, `docs/profiles/regulated-ml/`, `docs/evidence/catalog.md` | DATA, EVID, POL | Key custody, data-use posture, ML audit events, deletion/removal evidence artifacts |
| SOV-4 Operational Sovereignty | `core10/09-fail-closed-profile.md`, `ws6-migration/spec.md`, `docs/deployment-profile.md` | OPS, EXIT, EXEC | Fail-closed/refusal traces, migration/exit artifacts, operational continuity evidence |
| SOV-5 Supply Chain Sovereignty | `docs/invariants/sup.md`, `ws6-migration/spec.md`, `docs/compliance/pattern-library.md` | SUP, DEP, EXIT | SBOM/provenance, supplier dependency declarations, update/patch provenance evidence |
| SOV-6 Technology Sovereignty | `core10/08-interop-api-surface.md`, `core10/10-exit-interop.md`, `ws4-interop-api/spec.md` | INT, EXIT, EXEC | OpenAPI/AsyncAPI/export compatibility artifacts, portability/refusal evidence |
| SOV-7 Security & Compliance Sovereignty | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-custody.md`, `docs/domains/grc.md` | EVID, OPS, AUTH | Export bundles, chain integrity proofs, incident/audit evidence, control evidence |
| SOV-8 Environmental Sustainability | Intentionally outside ECS core scope (`docs/non-goals.md`) | N/A | If needed, handle as provider competitive layer and optional disclosure artifacts |

## SEAL-style alignment guidance
The CSF uses minimum assurance levels per objective (SEAL thresholds).  
ECS can support this by requiring, per objective:
1. a declared claim scope,
2. objective-linked artifacts,
3. verifier checks that pass without provider-private access.

Recommended claim discipline:
- no "overall sovereignty" claim without per-objective evidence,
- explicit gaps and compensating controls where evidence is partial,
- periodic re-validation cadence on exported evidence bundles.

## Invariant alignment checklist (minimum)
To align ECS with CSF objective scoring, require:
- **AUTH/POL** for SOV-1/2/7 claims,
- **DATA/EVID** for SOV-2/3/7 claims,
- **OPS/EXEC/EXIT** for SOV-4/6 claims,
- **SUP/DEP** for SOV-5 claims,
- explicit out-of-scope declaration for SOV-8.

## Related ECS docs
- `docs/mappings/eu-sovereignty-assurance-matrix.md`
- `docs/mappings/reg-mapping.md`
- `docs/profiles/no-control-profile.md`
- `docs/profiles/evidence-profiles.md`
- `docs/evidence/verifier-responsibilities.md`

## Source
- European Commission DG DIGIT, *Cloud Sovereignty Framework v1.2.1 (Oct 2025)*: <https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en>
