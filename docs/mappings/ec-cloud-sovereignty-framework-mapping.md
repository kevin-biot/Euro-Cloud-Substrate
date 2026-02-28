# European Commission Cloud Sovereignty Framework Mapping (Draft, Non-Normative)

## Purpose
Map the European Commission DG DIGIT **Cloud Sovereignty Framework (CSF) v1.2.1 (Oct 2025)** objectives (SOV-1..SOV-8) to ECS invariants, profiles, and evidence artifacts.

This mapping is for architecture and procurement alignment. It does not claim certification.

## CSF assessment model (anchor)
CSF assesses sovereignty through:
- objective-specific questions and supporting evidence (`Section 4`, pages 4-5),
- minimum assurance thresholds via SEAL levels (`Section 3`, page 3),
- a weighted Sovereignty Score (`Section 5`, page 6).

ECS aligns as the "how" layer: invariant-constrained behavior + exportable, verifier-friendly evidence.

## Objective matrix with CSF prompts, verifier mode, and fail criteria
| CSF objective (weight) | CSF evidence prompt(s) + ref | ECS mapping (Core10 / WS / docs) | ECS artifact set (examples) | Verifier mode | Fail-closed criteria for claim |
|---|---|---|---|---|---|
| SOV-1 Strategic (15%) | Decisive authority in EU, change-of-control assurances, EU financing/investment, ability to sustain operations (`Sec.4`, p4) | `core10/04-policy-authority-interface.md`, `docs/domains/sovereignty-assurance.md`, `docs/conformance/model.md` | `authority-graph.json`, control-plane ownership declaration, change-of-control artifact | Export bundle + public docs | If decisive-authority artifacts are missing or only private assertions exist, do not claim SOV-1 threshold |
| SOV-2 Legal & Jurisdictional (10%) | Exposure to non-EU law/authority, compel channels, legal anchoring in EU (`Sec.4`, p4) | `core10/01-olz-eu-baseline.md`, `core10/03-eosc-metadata-spec.md`, `docs/domains/federation.md` | Jurisdiction policy snapshot, legal-demand handling artifact, refusal traces | Export bundle | If compelled-access pathway cannot be evidenced/refused per policy, fail SOV-2 claim |
| SOV-3 Data & AI (10%) | Customer crypto control, access auditability, irreversible deletion evidence, strict EU confinement, EU-controlled AI/data pipelines (`Sec.4`, p4) | `core10/03-eosc-metadata-spec.md`, `docs/profiles/regulated-ml/`, `docs/evidence/catalog.md`, `docs/domains/data-security.md` | `key-custody.json`, `dataset-manifest-ml.json`, data-use posture, deletion/export evidence, ML dependency artifacts | Export bundle (preferred), privileged only for exceptional checks | If crypto custody, confinement, or deletion evidence is unverifiable without provider-private access, fail or downgrade claim |
| SOV-4 Operational (15%) | Migration ease, EU operator autonomy, EU support, documentation/know-how, supplier control (`Sec.4`, p5) | `core10/09-fail-closed-profile.md`, `ws6-migration/spec.md`, `docs/deployment-profile.md` | Migration/exit artifacts, refusal evidence for unsupported portability, operations runbooks, dependency declarations | Export bundle + public docs | If migration/exit cannot be demonstrated with artifacts, fail SOV-4 threshold |
| SOV-5 Supply Chain (20%) | Hardware/firmware/software origin, non-EU dependency degree, supplier/sub-supplier visibility/audit rights (`Sec.4`, p5) | `docs/invariants/sup.md`, `ws6-migration/spec.md`, `docs/compliance/pattern-library.md` | SBOM/provenance set, dependency graph, supplier visibility artifacts | Export bundle + privileged supplier data where required | If critical dependencies lack provenance/visibility, fail SOV-5 threshold |
| SOV-6 Technology (15%) | Open/non-proprietary interoperability, open licenses/auditability, architecture/data-flow visibility, EU independence in compute stack (`Sec.4`, p5) | `core10/08-interop-api-surface.md`, `core10/10-exit-interop.md`, `ws4-interop-api/spec.md` | Open API schemas, compatibility artifacts, portability/refusal traces | Public docs + export bundle | If portability/interoperability is only declarative (no evidence), fail SOV-6 threshold |
| SOV-7 Security & Compliance (10%) | Certifications, EU framework adherence, EU-jurisdiction SOC/logging control, breach reporting, patch autonomy, independent audits (`Sec.4`, p5) | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-custody.md`, `docs/domains/grc.md` | Export bundle, chain integrity artifacts, SOC/log control evidence, incident evidence package | Export bundle + privileged SOC evidence (as needed) | If logs/audit proofs are not independently verifiable, fail SOV-7 threshold |
| SOV-8 Environmental Sustainability (5%) | Energy efficiency targets, circularity, emissions/water disclosure, low-carbon sourcing (`Sec.4`, p5) | Out of ECS core scope (`docs/non-goals.md`) | Optional disclosure artifact interface only | Public docs | If mandatory in tender, treat as external scoring input; ECS provides link-out, not native scoring |

## SEAL ladder hooks in ECS terms (non-normative)
CSF SEAL definitions are in `Section 3` (page 3). ECS-oriented interpretation for objective claims:

| Objective | SEAL-2 (Data Sovereignty) | SEAL-3 (Digital Resilience) | SEAL-4 (Full Digital Sovereignty) |
|---|---|---|---|
| SOV-1 | EU legal enforceability evidenced | EU influence over decisive authority + continuity evidence | Complete EU control and no critical non-EU control path evidenced |
| SOV-2 | Enforceable EU legal posture + compel-path visibility | Compel-path constraints + tested refusal evidence | Only EU-law control path for critical authority/custody |
| SOV-3 | Data/key control evidence and auditable access/deletion | EU-confined processing + verified ML dependency controls | Complete EU control over critical data/AI stack and custody |
| SOV-4 | Portable operations baseline exists | Proven migration/continuity with independent evidence | Full operational autonomy from non-EU critical support/control |
| SOV-5 | Core supply-chain provenance exists | Critical dependency resilience and auditability demonstrated | Critical supply chain fully EU-controlled or non-critical where external |
| SOV-6 | Interop/exit baseline and open interfaces evidenced | Independent portability and low lock-in validated | Full technology stack control without critical foreign lock-in |
| SOV-7 | Audit-chain and control evidence available | Independent security/compliance verification operationalized | Security/compliance operations fully under EU control |
| SOV-8 | External sustainability evidence available | External resilience indicators and targets demonstrated | Full sustainability sovereignty not scored by ECS; tender-specific |

## Score contribution hooks (Section 5, page 6)
CSF defines objective weights and a score formula. ECS guidance:
- **Threshold-critical artifacts** support minimum SEAL acceptance.
- **Score-differentiating artifacts** improve ranking beyond threshold.

| Objective | Weight | Threshold-critical artifacts | Score-differentiating artifacts |
|---|---:|---|---|
| SOV-1 | 15% | Authority map, change-of-control evidence | Depth of EU financing/investment and continuity evidence quality |
| SOV-2 | 10% | Jurisdiction policy + compel/refusal evidence | Breadth and test depth of compel-channel constraints |
| SOV-3 | 10% | Key custody + confinement + deletion evidence | ML dependency transparency and verifier reproducibility depth |
| SOV-4 | 15% | Migration/exit portability evidence | Time-to-migrate and operational autonomy evidence quality |
| SOV-5 | 20% | SBOM/provenance baseline for critical components | Supply-chain visibility depth and audit rights completeness |
| SOV-6 | 15% | Interop/exit evidence | Breadth of standards support and lock-in resistance evidence |
| SOV-7 | 10% | Audit chain and incident evidence | Independent auditability depth and SOC control transparency |
| SOV-8 | 5% | External sustainability disclosure | Quality/coverage of disclosed sustainability metrics |

## Invariant alignment checklist (minimum)
- **AUTH/POL** for SOV-1/2/7 claims.
- **DATA/EVID** for SOV-2/3/7 claims.
- **OPS/EXEC/EXIT** for SOV-4/6 claims.
- **SUP/DEP** for SOV-5 claims.
- SOV-8 handled via optional link-out disclosures outside ECS core semantics.

## Related ECS docs
- `docs/mappings/eu-sovereignty-assurance-matrix.md`
- `docs/mappings/reg-mapping.md`
- `docs/profiles/no-control-profile.md`
- `docs/profiles/evidence-profiles.md`
- `docs/evidence/verifier-responsibilities.md`

## Source
- European Commission DG DIGIT, *Cloud Sovereignty Framework v1.2.1 (Oct 2025)*: <https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en>
