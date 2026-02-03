# Euro Cloud Substrate (ECS)

An architectural definition project for a portable, governable, European cloud substrate. This repo hosts the specs, invariants, and profiles that define the minimal shared contracts European providers can implement.

- Core paper: `VISION.md` (v0.2) and `architecture/`
- Invariants: `docs/invariants-v0.3.md` (authoritative), deep-dives: `docs/invariants/`, coverage: `docs/invariant-coverage.md`
- Profiles: `crp/` (Crisis Resilience Profile), `docs/profiles/README.md`
- Conformance shape: `docs/conformance-model.md`
- Conformance checklists (draft): `docs/conformance/README.md`
- Minimal metrics (draft): `docs/metrics.md`
- SOC/log control profile (draft): `docs/soc-log-control.md`
- Evidence export: `docs/evidence-export-schema.md`, catalog: `docs/evidence-catalog.md`
- Control-plane capabilities: `architecture/control-plane.md`
- EUDI wallet integration note (draft): `docs/eudi-wallet-integration.md`
- Workstreams: `ws1-olz-eu/`, `ws2-eosc/`, `ws3-exec-envelopes/`, `ws4-interop-api/`, `ws5-evidence-audit/`, `ws6-migration/`
- Core 10: `core10/`
- Governance and contribution: `GOVERNANCE.md`, `CONTRIBUTING.md`, `CALL_FOR_PARTICIPATION.md`
- Guardrails: `NON_GOALS.md`, `ANTI_CAPTURE.md`, `SECURITY.md`
- Mappings: `docs/reg-mapping.md`, `docs/irn-mapping.md`
- Data Act architecture constraint (draft): `docs/data-act-architecture-constraint.md`
- Gaia-X alignment note (draft): `docs/gaia-x/README.md`
- Comparisons/integration: `docs/comparison.md`, `docs/integration-examples.md`
- Compliance patterns (draft): `docs/compliance-pattern-library.md`
- ML evidence implementation gap (draft): `docs/ml-evidence-implementation.md`
- Qualified archiving note (draft): `docs/qualified-archiving.md`
- Open source alignment targets (draft): `docs/opensource-targets.md`
- Overview wiki: https://github.com/kevin-biot/Euro-Cloud-Substrate/wiki

## Purpose
Define an open, adoptable Euro Cloud Substrate that delivers portability, governability, auditability, and industrialisation by reusing proven primitives and specifying the missing contract layer (identity, policy, execution envelopes, evidence).

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
- Use `docs/reg-mapping.md` as a contextual guide to EU regulatory drivers.
- See `docs/irn-mapping.md` for the draft IRN crosswalk (IRN defines “what”; ECS defines “how” via invariants and evidence).
- For evidence export and admissibility, see `docs/evidence-export-schema.md`, `docs/qualified-archiving.md`, and `docs/evidence-catalog.md`.
- For ML-specific evidence gaps and implementation guidance, see `docs/ml-evidence-implementation.md`.
- For wallet/identity binding guidance, see `docs/eudi-wallet-integration.md`.
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
  1. Pick a Core10 component from `docs/core10-status.md`.
  2. Check open issues/labels for that component.
  3. Submit PR with invariant references, requirements, and evidence expectations.

## Repository structure
- `VISION.md` — core paper (v0.2)
- `ROADMAP.md` — phases and expected deliverables
- `architecture/` — reference architecture overview and diagrams
- `crp/` — Crisis Resilience Profile spec, invariants, conformance, diagrams
- `docs/invariants-v0.3.md` — authoritative invariant list and statuses
- `docs/invariants/` — family deep-dives (e.g., DEP, SUP, PHY, OPS)
- `docs/invariant-coverage.md` — structural coverage matrix
- `docs/conformance-model.md` — evidence-driven conformance shape
- `docs/conformance/` — draft conformance checklists
- `docs/metrics.md` — minimal metrics (draft)
- `docs/soc-log-control.md` — SOC/log control profile (draft)
- `core10/` — mandatory ECS components
- `ws*/` — workstream folders with scope, invariants, conformance outlines, diagrams
- `decisions/` — architectural decision records
- `docs/irn-mapping.md` — IRN crosswalk (draft)
- `docs/evidence-export-schema.md` — portable evidence bundles
- `docs/evidence-catalog.md` — evidence event/artefact catalog
- `docs/compliance-pattern-library.md` — compliance pattern library (draft)
- `docs/ml-evidence-implementation.md` — ML evidence implementation gap (draft)
- `docs/qualified-archiving.md` — qualified archiving note (draft)
- `docs/eudi-wallet-integration.md` — wallet integration note (draft)
- `docs/profiles/README.md` — how profiles use invariants
- `docs/comparison.md`, `docs/integration-examples.md` — complementary positioning and examples
- `.github/` — issue/PR templates
- `scripts/` — helper scripts (e.g., labels)

## Status
- Invariant surface defined (v0.3). Profiles, mappings, and conformance sharpening in progress. Contributors and workstream leads welcome.
