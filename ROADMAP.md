# Roadmap

## Phase 0 — Definition (current)
- Publish the v0.2 paper (`VISION.md`).
- Stand up repo structure, workstream stubs, Core 10 placeholders, and CRP profile.
- Recruit initial contributors/workstream leads.
- Begin architectural decision log.

## Phase 1 — Architecture Baseline (8–12 weeks)
- Draft v0.5 for each workstream (spec + invariants + conformance outline + diagrams).
- Publish first reference architecture pack under `architecture/` (Mermaid/PlantUML).
- Define conformance testing approach (without full implementation).
- Begin aligning invariants taxonomy (see `docs/invariants-v0.3.md`) with Core 10/CRP for next revision.
- Begin compliance mappings (IRN/NIS2/DORA/etc.) using `docs/irn-mapping.md` as a draft crosswalk.

## Phase 2 — Industrialisation (following)
- Implement conformance tests.
- Produce minimal reference implementations.
- Run provider pilots (2–3 vendors) and document migrations.
- Iterate specs based on pilot feedback.

### Reference stack trajectory (Phase 2+)
- Publish a reference stack blueprint mapping invariants to OSS components (e.g., K8s, GitOps, CI/CD, object storage, VM envelopes), keeping components swappable.
- Provide sample manifests/policies demonstrating OLZ-EU, EOSC metadata enforcement, policy/authority gates, evidence emission, and CRP behaviors.
- Keep the blueprint non-normative: implementations may swap components if they meet the same conformance tests.

### Performance baselines (target Q3 2026)
- IALP policy decision latency target: <10ms.
- Evidence collection impact: <2% application throughput reduction.
- CRP partition detection/failover to local authority: <30s.
- Publish benchmark suite as validation reference.

## Deliverables map
- CRP: `crp/spec.md`, `crp/invariants.md`, `crp/conformance-outline.md`, `crp/diagrams/`
- Workstreams: `ws*/spec.md`, `ws*/invariants.md`, `ws*/conformance-outline.md`, `ws*/diagrams/`
- Core 10: `core10/*.md`
- Architecture pack: `architecture/overview.md` + diagrams
- Governance & process: `GOVERNANCE.md`, `CONTRIBUTING.md`, `decisions/`
