# Certification Intake Matrix (Draft, Non-Normative)

## Purpose
Provide a single intake view of cloud assurance schemes and checklists so ECS users can decide:
- what is legally binding vs voluntary,
- what evidence is needed,
- and how to validate claims consistently.

This matrix is a procurement/architecture aid, not a certification instrument.

## Intake matrix
| Scheme / framework | Current status (date-specific) | Legal nature | Primary scope | ECS evidence needed | Verification posture |
|---|---|---|---|---|---|
| EUCS (EU cloud cybersecurity scheme) | Under development in EU framework pages (as of 2026-02-28) | Future EU certification scheme (once adopted) | Cybersecurity assurance levels for cloud services | Profile claim + security control evidence + export bundle + refusal evidence | Treat as readiness mapping until final implementing text exists |
| EU Cloud CoC (GDPR Art. 40) | Operational/approved process (since 2021) | Voluntary code with supervisory authority process | Processor GDPR/cloud data-protection obligations | Policy/authority snapshots, processor control artifacts, export bundle, portability artifacts | Validate obligation-to-artifact traceability and independent verification |
| CCSL (cloud certification schemes list) | Catalogue page (legacy list context, updated 2021) | Informational registry | Discover applicable schemes/standards | N/A directly; use to pick candidate schemes and map to ECS artifacts | Use as discovery source, not as conformance proof |
| National sovereignty scorecards (member-state/public procurement approaches) | Emerging/non-uniform | Procurement criteria (typically non-EU-wide binding) | Jurisdiction/control/governance evaluation | Sovereignty assurance artifacts, trust-root and custody artifacts, refusal evidence | Require evidence-backed scoring and explicit gap register |
| Project-level compliance checklists (collaboratives, ecosystem groups) | Varies by project | Non-binding practical guidance | Operational portability, API/tooling, audit readiness | Deployment profile artifacts, interop/exit artifacts, runnable PoC evidence | Useful for execution rigor; do not treat as legal certification |

## Recommended claim discipline
- Always separate:
  - **certification status** (formal scheme result),
  - **ECS evidence status** (artifact-backed conformance evidence),
  - **readiness status** (mapped but not yet certified).
- In manifests/exports, include selected profile and verifier inputs so scheme claims are independently testable.

## Minimum intake checklist (for buyers)
1. Confirm scheme status and legal nature (binding vs voluntary vs informational).
2. Ask for an ECS-aligned evidence bundle and profile claim.
3. Run independent verifier checks (chain, pointer integrity, policy/authority refs).
4. Record gaps + compensating controls + retest date.

## Sources
- EU certification framework (EUCS status): <https://digital-strategy.ec.europa.eu/en/factpages/european-cybersecurity-certification-framework>
- EU Cloud CoC context (EDPB opinion): <https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-162021-draft-decision-belgian-supervisory_et>
- EU Cloud CoC approval note (Belgian DPA): <https://www.dataprotectionauthority.be/citizen/the-be-dpa-approves-its-first-european-code-of-conduct>
- CCSL catalogue page: <https://digital-strategy.ec.europa.eu/en/library/cloud-computing-certification-schemes-list-ccsl>
