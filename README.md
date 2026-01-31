# Euro Cloud Substrate (ECS)

An architectural definition project for a portable, governable, European cloud substrate. This repo hosts the drafts, specs, and workstream materials for defining the minimal shared contracts that European providers can implement.

- Current paper: `VISION.md` (v0.2)
- Roadmap: `ROADMAP.md`
- CRP profile: `crp/` (Crisis Resilience Profile)
- Workstreams: `ws1-olz-eu/`, `ws2-eosc/`, `ws3-exec-envelopes/`, `ws4-interop-api/`, `ws5-evidence-audit/`, `ws6-migration/`
- Core 10 components: `core10/`
- Governance and contribution: `GOVERNANCE.md`, `CONTRIBUTING.md`, `CALL_FOR_PARTICIPATION.md`
- Regulatory mapping (context): `docs/reg-mapping.md`
- Overview wiki: https://github.com/kevin-biot/Euro-Cloud-Substrate/wiki
- Scope guardrails: `NON_GOALS.md`, `ANTI_CAPTURE.md`
- Security policy: `SECURITY.md`
- Adoption tracking: `ADOPTERS.md`
- Integration/comparison: `docs/integration-examples.md`, `docs/comparison.md`
- Starter tasks: `GOOD_FIRST_ISSUES.md`
- Invariants v0.3 draft: `docs/invariants-v0.3.md`

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
- For a high-level overview, see the GitHub wiki.

## Repository structure
- `VISION.md` — core paper (v0.2)
- `ROADMAP.md` — phases and expected deliverables
- `architecture/` — reference architecture overview and diagrams
- `crp/` — Crisis Resilience Profile spec, invariants, conformance, diagrams
- `core10/` — mandatory ECS components
- `ws*/` — workstream folders with scope, invariants, conformance outlines, diagrams
- `decisions/` — architectural decision records
- `.github/` — issue/PR templates
- `scripts/` — helper scripts (e.g., labels)

## Status
Draft v0.2. Contributors and workstream leads to be added.
