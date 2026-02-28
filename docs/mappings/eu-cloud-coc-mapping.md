# EU Cloud CoC Mapping (Draft, Non-Normative)

## Purpose
Map EU Cloud Code of Conduct (EU Cloud CoC) obligations to ECS evidence and conformance surfaces, so providers can show GDPR-aligned cloud controls with portable artifacts.

## Status snapshot (as of 2026-02-28)
- EU Cloud CoC is an approved GDPR Article 40 Code of Conduct for cloud processors.
- Approval milestones include Belgian DPA approval (2021-05-20) and EDPB opinion alignment.
- This mapping is not legal advice and does not replace formal CoC assessment processes.

## Indicative crosswalk
| EU Cloud CoC obligation area (indicative) | ECS mapping (Core10 / WS / docs) | Evidence expectation | Verifier check |
|---|---|---|---|
| Processor accountability and documented instructions | `core10/04-policy-authority-interface.md`, `docs/domains/privacy.md`, `docs/domains/grc.md` | Policy snapshot references, authority chain artifacts, decision traces | Policy and authority references are present for governed actions |
| Subprocessor transparency and control boundaries | `docs/domains/sovereignty-assurance.md`, `docs/invariants/dep.md`, `ws6-migration/spec.md` | Dependency declarations, ownership/control-plane artifacts, exit artifacts | Critical third-party dependencies are declared and traceable |
| Technical and organizational measures (security baseline) | `docs/domains/data-security.md`, `core10/09-fail-closed-profile.md`, `docs/invariants/ops.md` | Encryption/key-custody evidence, refusal behavior evidence, operational control artifacts | Control evidence exists and refusals are logged when policy requires |
| Access control and identity federation | `docs/domains/iam.md`, `ws4-interop-api/spec.md`, `docs/guides/agent-delegation.md` | Credential verification events, delegation lifecycle events, scope-bound authorization events | Authn/authz checks and delegation constraints are independently verifiable |
| Auditability, logging, and incident support to customers | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-custody.md`, `docs/evidence/export-schema.md` | Export bundle (`manifest`, `events`, `chain-segment`, verifier inputs), incident evidence package | Chain continuity and pointer integrity validate without provider-private access |
| Data deletion/return and portability support | `core10/10-exit-interop.md`, `ws6-migration/spec.md`, `docs/deployment-profile.md` | Exit/interoperability artifacts, migration evidence, refusal evidence for unsupported cases | Export is reproducible and supports third-party verification |
| Data location/transfers transparency | `core10/03-eosc-metadata-spec.md`, `docs/domains/federation.md`, `docs/invariants/data.md` | Jurisdiction metadata, routing/refusal evidence, telemetry path audit artifact | Location/routing outcomes match declared policy snapshots |

## Procurement use
- Ask suppliers to provide:
  - declared `evidence_profile_id`,
  - a sample export bundle,
  - a short obligation-to-artifact mapping based on this table.
- Evaluate claims on verifier outputs and artifacts, not self-asserted statements.

## Sources
- Belgian DPA approval notice (EU Cloud CoC): <https://www.dataprotectionauthority.be/citizen/the-be-dpa-approves-its-first-european-code-of-conduct>
- EDPB Opinion 16/2021 (Belgian draft decision on EU Cloud CoC): <https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-162021-draft-decision-belgian-supervisory_et>
