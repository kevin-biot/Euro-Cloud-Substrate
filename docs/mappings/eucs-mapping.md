# EUCS Mapping (Draft, Non-Normative)

## Purpose
Provide an ECS crosswalk for the European Cybersecurity Certification Scheme for Cloud Services (EUCS), so teams can prepare evidence and interoperability posture while the scheme is still under development.

## Status snapshot (as of 2026-02-28)
- EU cybersecurity certification framework page lists **EUCS as "UNDER WAY"** (not yet adopted as an implementing act).
- The draft/candidate EUCS materials describe cloud-service scope and three assurance levels (Basic, Substantial, High).

ECS position:
- ECS is not a certification scheme.
- ECS provides portable evidence and verification primitives that can support future EUCS readiness and procurement evidence.

## Indicative crosswalk
| EUCS area (indicative) | ECS mapping (Core10 / WS / docs) | Evidence expectation | Verifier check |
|---|---|---|---|
| Scheme scope and assurance intent (cloud services, increasing assurance) | `docs/profiles/evidence-profiles.md`, `docs/conformance/model.md`, `core10/05-evidence-event-model.md` | Declared `evidence_profile_id`, conformance claim scope, profile claim artifact | Profile claim is present and matches exported bundle contents |
| Security governance and policy enforcement | `core10/04-policy-authority-interface.md`, `core10/09-fail-closed-profile.md`, `docs/domains/grc.md` | Policy snapshots, authority snapshots, refusal evidence | Decisions/refusals are reproducible from snapshot references |
| IAM / federation / delegated actors | `docs/domains/iam.md`, `docs/guides/agent-delegation.md`, `ws4-interop-api/spec.md` | Credential validation events, delegation issue/revoke events, out-of-scope refusal events | Actor identity and delegation scope/expiry are provable |
| Data protection and key custody posture | `docs/domains/data-security.md`, `docs/profiles/no-control-profile.md`, `docs/domains/sovereignty-assurance.md` | Key custody artifact, encryption posture artifact, trust-root declaration | Artifact refs resolve and integrity checks pass |
| Logging, audit, and forensic readiness | `core10/06-audit-chain-custody.md`, `docs/evidence/export-schema.md`, `docs/evidence/verifier-responsibilities.md` | Hash-chained events, export bundle, verifier inputs | Chain continuity and artifact pointer checks pass |
| Incident handling and traceability | `ws5-evidence-audit/spec.md`, `docs/domains/grc.md`, `docs/guides/evidence-vs-logs.md` | Incident decision traces, response/refusal evidence, immutable bundle export | Time-ordered decision trace is independently verifiable |
| Supply-chain and component trust | `docs/invariants/sup.md`, `docs/compliance/pattern-library.md`, `ws6-migration/spec.md` | SBOM/provenance artifacts, dependency declarations, exit artifacts | Critical dependencies and provenance are evidenced and exportable |
| Data location/transparency and jurisdiction constraints | `core10/03-eosc-metadata-spec.md`, `docs/domains/federation.md`, `docs/invariants/data.md` | Jurisdiction metadata, route/refusal evidence, telemetry path audit artifacts | Jurisdiction policy outcomes match emitted routing/refusal evidence |

## Readiness guidance
- Treat this mapping as **EUCS readiness**, not an EUCS certification claim.
- Keep assurance-level statements provisional until final EUCS implementing text is adopted.
- In procurement, require artifact-backed evidence, not marketing labels.

## Sources
- EU certification framework status (EUCS under way): <https://digital-strategy.ec.europa.eu/en/factpages/european-cybersecurity-certification-framework>
- ENISA EUCS draft context and three assurance levels: <https://www.enisa.europa.eu/news/enisa-news/cloud-certification-scheme>
