# Tech Sovereignty Catalogue Mapping — Draft (Non‑Normative)

## Purpose
Provide a practical mapping between the Tech Sovereignty Catalogue and ECS, so providers can supply evidence for catalogue visibility without changing ECS semantics.

## Catalogue summary (public)
- The Tech Sovereignty Catalogue is positioned as Europe’s showcase of trusted digital solutions.
- Submission flow includes eligibility checks for market readiness (TRL 9), EU/EFTA presence (legal, R&D), and capacity/capability/control, followed by independent expert evaluation and inclusion/visibility in the catalogue.
- The catalogue highlights two related labels: **Software Made in Europe** and **Software Hosted in Europe**.

## Label criteria (public)
**Software Made in Europe** (summary):
- Company headquartered and majority‑owned in Europe.
- Solution developed/tested mainly in Europe.
- Majority of R&D and staff in EU/EFTA.
- Key stages of development carried out in Europe.

**Software Hosted in Europe** (summary):
- Hosting and data within EU/EFTA.
- Transparency about data transfers and EU regulatory compliance.
- Commitment to privacy and European digital sovereignty.

## ECS alignment table
| Catalogue element | What ECS can evidence | Out of scope for ECS |
| --- | --- | --- |
| **Market readiness (TRL 9)** | Evidence exports, audit chains, conformance checklists (technical proof of operational readiness) | Formal TRL certification or business maturity scoring |
| **EU/EFTA presence (legal, R&D)** | Authority/ownership evidence can be referenced, but ECS does not validate corporate structure | Corporate eligibility checks, HQ/R&D location proof |
| **Capacity/Capability/Control** | NCP evidence (authority graphs, key custody proofs, telemetry paths), refusal evidence | Legal/organizational control judgments |
| **Software Made in Europe label** | Evidence of development artifacts, provenance (SBOMs, build pipelines) | Corporate ownership/location criteria for label |
| **Software Hosted in Europe label** | Jurisdiction metadata enforcement, residency evidence, export bundles | Formal label eligibility or certification |

## Suggested “catalogue submission pack” (ECS‑aligned)
1. **Profile claims** (baseline + any stronger profiles such as NCP or regulated‑ML).  
2. **Evidence export bundle** demonstrating:
   - authority/policy binding events,
   - jurisdiction and residency enforcement,
   - audit chain integrity and exportability.  
3. **Conformance checklist** pointing to invariant coverage and refusal evidence.  
4. **Optional**: SBOM/provenance artifacts for supply‑chain visibility.

## Notes
ECS is a contract layer and does not replace catalogue governance or label eligibility. It provides a **verifiable evidence trail** that can support catalogue evaluation without changing ECS semantics.
