# Euro Cloud Substrate (ECS)

An architectural definition project for a portable, governable, European cloud substrate. This repo hosts the specs, invariants, and profiles that define the minimal shared contracts European providers can implement.

## Who this is for / not for
**ECS is for:**
- EU cloud providers
- Sovereign operators
- Regulated deployers
- Auditors / verifiers
- Procurement authorities

**ECS is not for:**
- Building a cloud platform
- Replacing orchestration systems
- Defining business governance
- Certifying compliance
- Competing with IPCEI / 8ra / hyperscalers

## Start here
1. Evidence Profiles (what to claim): `docs/profiles/evidence-profiles.md`
2. Golden Bundles (what correct looks like): `docs/examples/evidence-bundles/`
3. Reference Adapter (how to emit it): `adapters/k8s-admission/`
4. ML Inference Sidecar (draft): `adapters/ml-inference-sidecar/`
5. Object Storage Proxy (draft): `adapters/object-storage-proxy/`
6. RFP Guide (how to buy it): `docs/procurement/rfp-guide.md`
7. Architecture Overview (big picture): `docs/architecture/ecs-architecture-overview.md`
8. Deliverables map (spec spine): `docs/deliverables.md`
9. Docs index (navigation): `docs/index.md`

## Adapters (what they are)
Adapters are **reference implementations** that show how to emit ECS evidence at key control points (admission, inference, storage).  
They are **not production frameworks**; they exist to prove contract fidelity, refusal semantics, and exportability in minimal code.

## Competition and differentiation
ECS standardizes **verifiable governance and portability**, not the commercial layer. Conformance is a minimum contract; providers still compete on performance, managed services, UX, pricing, and regional specialization. See `docs/positioning/competition.md`.

- Jurisdiction‑aware routing (agentic + ML) is treated as a contract requirement with refusal evidence; routing protocols remain implementation‑specific.

- Core paper: `VISION.md` (v0.2) and `docs/architecture/`
- Invariants: `docs/invariants/v0.3.md` (authoritative), deep-dives: `docs/invariants/`, coverage: `docs/conformance/invariant-coverage.md`
- Profiles: `crp/README.md` (Crisis Resilience Profile), `docs/profiles/README.md`
- Conformance shape: `docs/conformance/model.md`
- Conformance checklists (draft): `docs/conformance/README.md`
- Minimal metrics (draft): `docs/conformance/metrics.md`
- SOC/log control profile (draft): `docs/compliance/soc-log-control.md`
- Evidence export: `docs/evidence/export-schema.md`, catalog: `docs/evidence/catalog.md`
- Data security domain note (draft): `docs/domains/data-security.md`
- IAM domain note (draft): `docs/domains/iam.md`
- GRC domain note (draft): `docs/domains/grc.md`
- Privacy & user control note (draft): `docs/domains/privacy.md`
- Federation domain note (draft): `docs/domains/federation.md`
- Control-plane capabilities: `docs/architecture/control-plane.md`
- EUDI wallet integration note (draft): `docs/domains/eudi-wallet-integration.md`
- Workstreams: `ws1-olz-eu/`, `ws2-eosc/`, `ws3-exec-envelopes/`, `ws4-interop-api/`, `ws5-evidence-audit/`, `ws6-migration/`
- Core 10: `core10/`
- Governance and contribution: `GOVERNANCE.md`, `CONTRIBUTING.md`, `docs/call-for-participation.md`
- Guardrails: `docs/non-goals.md`, `docs/anti-capture.md`, `SECURITY.md`
- Competition & differentiation: `docs/positioning/competition.md`
- Mappings: `docs/mappings/README.md`, `docs/mappings/reg-mapping.md`, `docs/mappings/irn-mapping.md`, `docs/mappings/suse-csf-mapping.md`, `docs/mappings/techsov-catalogue.md`, `docs/mappings/tmforum-camara.md`, `docs/mappings/aws-minimal-subset.md`, `docs/mappings/vcluster.md`
- IPCEI‑CIS mapping (draft): `docs/mappings/ipcei-cis-mapping.md`
- Data Act architecture constraint (draft): `docs/mappings/data-act-architecture-constraint.md`
- Gaia-X alignment note (draft): `docs/mappings/gaia-x/README.md`
- Comparisons/integration: `docs/guides/comparison.md`, `docs/guides/integration-examples.md`
- Compliance patterns (draft): `docs/compliance/pattern-library.md`
- ML evidence implementation gap (draft): `docs/guides/ml-evidence-implementation.md`
- Qualified archiving note (draft): `docs/evidence/qualified-archiving.md`
- Open source alignment targets (draft): `docs/guides/opensource-targets.md`
- Open-source adoption note (draft): `docs/oss-adoption.md`
- Landing zone reference (draft): `docs/guides/landing-zone-reference.md`
- Minimal pipeline schema (draft): `docs/guides/pipeline-schema.md`
- No‑control profile (draft): `docs/profiles/no-control-profile.md`
- Demo flow (draft): `docs/examples/demo-flow.md`
- Overview wiki: https://github.com/kevin-biot/Euro-Cloud-Substrate/wiki

## Purpose
Define an open, adoptable Euro Cloud Substrate that delivers portability, governability, auditability, and industrialisation by reusing proven primitives and specifying the missing contract layer (identity, policy, execution envelopes, evidence).

## Why this matters
Most platforms handle compute and storage well, but **portable governance evidence** is still fragmented. ECS fills that gap by defining a verifiable contract for authority, policy, portability, and evidence export—so providers can compete commercially while customers retain auditability and exit options.

## How to get involved
- Read `VISION.md` for the problem framing and objectives.
- Read `crp/` for partition/continuity posture.
- Browse workstream folders for scope and deliverables.
- Open issues or PRs against the relevant workstream. Follow `CONTRIBUTING.md`.
- Add architectural decisions under `decisions/` (ADR format).

## How to read this repo
- Start with `VISION.md` for the architecture, invariants, CRP, and IALP.
- Check `crp/` for the Crisis Resilience Profile details and conformance.
- Look at `core10/` for the mandatory components.
- Dive into `ws*/` for per-workstream specs, invariants, conformance, and diagrams.
- Use `docs/mappings/reg-mapping.md` as a contextual guide to EU regulatory drivers.
- See `docs/mappings/irn-mapping.md` for the draft IRN crosswalk (IRN defines “what”; ECS defines “how” via invariants and evidence).
- For evidence export and admissibility, see `docs/evidence/export-schema.md`, `docs/evidence/qualified-archiving.md`, and `docs/evidence/catalog.md`.
- For ML-specific evidence gaps and implementation guidance, see `docs/guides/ml-evidence-implementation.md`.
- For wallet/identity binding guidance, see `docs/domains/eudi-wallet-integration.md`.
- For a high-level overview, see the GitHub wiki.

## Out of scope by design
- Executive governance and sponsorship decisions.
- Legal acceptability determinations.
- Contract negotiation outcomes.
- Human resource policies.
- Risk acceptance decisions.

## Phase status
- Phase 0 complete: invariant set v0.3 defined. Further work focuses on profiles, mappings, and conformance (no new invariant families).

## Quick start for contributors
- Implementable now: `ws2-eosc/spec.md` (governed object storage), `docs/profiles/regulated-ml/` (ML governance).
- Needs more depth: `ws4-interop-api` (OpenAPI/AsyncAPI expansion), conformance/evidence catalog, reference implementations.
- How to contribute:
  1. Pick a Core10 component from `docs/architecture/core10-status.md`.
  2. Check open issues/labels for that component.
  3. Submit PR with invariant references, requirements, and evidence expectations.

## Repository structure
- `VISION.md` — core paper (v0.2)
- `ROADMAP.md` — phases and expected deliverables
- `docs/architecture/` — reference architecture overview and diagrams
- `crp/` — Crisis Resilience Profile spec, invariants, conformance, diagrams
- `docs/invariants/v0.3.md` — authoritative invariant list and statuses
- `docs/invariants/` — family deep-dives (e.g., DEP, SUP, PHY, OPS)
- `docs/conformance/invariant-coverage.md` — structural coverage matrix
- `docs/conformance/model.md` — evidence-driven conformance shape
- `docs/conformance/` — draft conformance checklists
- `docs/conformance/metrics.md` — minimal metrics (draft)
- `docs/compliance/soc-log-control.md` — SOC/log control profile (draft)
- `core10/` — mandatory ECS components
- `ws*/` — workstream folders with scope, invariants, conformance outlines, diagrams
- `decisions/` — architectural decision records (`decisions/README.md`)
- `docs/mappings/irn-mapping.md` — IRN crosswalk (draft)
- `docs/evidence/export-schema.md` — portable evidence bundles
- `docs/evidence/catalog.md` — evidence event/artefact catalog
- `docs/compliance/pattern-library.md` — compliance pattern library (draft)
- `docs/guides/ml-evidence-implementation.md` — ML evidence implementation gap (draft)
- `docs/evidence/qualified-archiving.md` — qualified archiving note (draft)
- `docs/domains/eudi-wallet-integration.md` — wallet integration note (draft)
- `docs/profiles/README.md` — how profiles use invariants
- `docs/guides/comparison.md`, `docs/guides/integration-examples.md` — complementary positioning and examples
- `.github/` — issue/PR templates
- `scripts/` — helper scripts (e.g., labels)

## Status
- Invariant surface defined (v0.3). Profiles, mappings, and conformance sharpening in progress. Contributors and workstream leads welcome.
