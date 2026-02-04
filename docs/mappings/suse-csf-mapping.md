# SUSE Cloud Sovereignty Framework (CSF) Mapping — Draft (Non‑Normative)

## Purpose
Provide a crosswalk between the SUSE Cloud Sovereignty Framework Self‑Assessment (SOV‑1…SOV‑8) and ECS components. This is informational only; ECS does not claim certification or endorsement.

## CSF summary (from SUSE assessment)
- SEAL scale: 0–4 (SEAL‑0 no sovereignty → SEAL‑4 full digital sovereignty).
- Eight sovereignty objectives (SOV‑1…SOV‑8) with weighted scoring.
- Critical violations occur when fundamental questions score SEAL‑2 or below.

## Crosswalk table
| CSF Objective | Weight | ECS mapping (Core10 / WS / invariants) | Evidence profile notes |
| --- | --- | --- | --- |
| SOV‑1 Strategic Sovereignty | 15% | Governance/process (`GOVERNANCE.md`, `decisions/`), profile claims; Core10‑04 (authority/policy), Core10‑10 (migration baseline) | Profile claims and export bundles show governance posture |
| SOV‑2 Legal & Jurisdictional | 10% | Core10‑01 (OLZ), Core10‑03 (EOSC), Core10‑05/06 (evidence), WS1/WS2; DATA‑01/02, AUTH‑01/02 | Jurisdiction metadata + refusal evidence; NCP for non‑EU control |
| SOV‑3 Data & AI | 10% | Core10‑03 (EOSC), Core10‑05/06 (evidence), regulated‑ML profile; WS2/WS5 | Regulated‑ML profile + usage receipts + export bundles |
| SOV‑4 Operational | 15% | Core10‑07 (execution envelopes), Core10‑09 (fail‑closed), CRP; WS3/WS5 | Evidence of partition behavior, refusal, and reconciliation |
| SOV‑5 Supply Chain | 20% | SUP invariants, SBOM/provenance, Core10‑03/07/10, WS2/WS6 | Provenance evidence and SBOM artifacts in exports |
| SOV‑6 Technology | 15% | Core10‑08 (interop), Core10‑10 (migration), WS4/WS6; INT/EXIT | Interop API claims + migration bundles |
| SOV‑7 Security & Compliance | 10% | IAM/Data‑security/GRC domain notes; Core10‑04/05/06; WS5 | Audit chain integrity + evidence export |
| SOV‑8 Environmental | 5% | Not explicitly covered in ECS today | Gap: environmental metrics / energy reporting |

## Critical‑violation interpretation (ECS, non‑normative)
If any of these conditions are not met, treat the outcome as a likely SEAL‑2‑or‑below risk for the related objective:
- **Authority/policy cannot be proven** (no authority binding or policy snapshot evidence) → SOV‑1/2/7
- **Jurisdiction metadata not enforced** (placement not enforced or unauditable) → SOV‑2/3
- **Evidence export unavailable** (no export bundles or integrity proofs) → SOV‑4/7
- **Supply‑chain provenance missing** (no SBOM/provenance for critical components) → SOV‑5
- **Interop/exit paths undefined** (no migration/export path for governed workloads/data) → SOV‑6

## ECS gaps vs CSF (current)
- **Environmental (SOV‑8):** ECS does not define energy or carbon reporting requirements; this is intentionally out of scope.
- **Strategic (SOV‑1):** ECS provides governance documentation and profile claims, but does not quantify ownership/control structures.

## Notes
- This mapping should be revisited if CSF objective definitions change.
- ECS is a contract layer; it can be used to *evidence* sovereignty objectives but does not certify them.
