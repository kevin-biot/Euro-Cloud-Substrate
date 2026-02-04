# Privacy & User Control Domain (Draft, Non‑Normative)

## Purpose
Define privacy‑by‑design expectations and user control across the cloud‑edge continuum, focusing on **consent, minimization, and evidence** without prescribing a specific privacy framework.

## Capabilities (baseline)
- **Privacy‑by‑design** principles embedded in workflows
- **Consent management** and preference enforcement
- **Data minimization** practices
- **Differential privacy (DP)** for analytics where applicable

## ECS mapping (no new semantics)
- **DATA + EVID invariants** — residency, classification, lineage, evidence export.
- **Core10‑03 EOSC** — governance metadata for data handling.
- **Core10‑05/06** — evidence events and audit chain.
- **Compliance patterns** — consent/intent token (CITP) and usage receipt (URP).
- **Regulatory mapping** — `docs/reg-mapping.md` (GDPR alignment).

## Evidence expectations (privacy‑grade)
- **Consent tokens** bound to purpose and policy snapshot.
- **Purpose binding** events for governed data access.
- **Minimization evidence** (e.g., redaction/field‑suppression decisions) where required.
- **Differential privacy** parameters recorded when DP is used (epsilon/delta, mechanism id).

Consent and purpose binding are **decision events**: they MUST be evaluated before governed access and emit `accepted`/`refused`/`failed` outcomes with policy/authority snapshot references.

## Notes
ECS defines **the evidence contract** for privacy controls, not the privacy framework itself. Providers may implement different privacy systems as long as evidence is portable and verifiable.
