# Contributing (Draft)

## How to contribute
- Start with `VISION.md` and the relevant workstream README under `ws*/`.
- Open an issue to propose scope, invariants, or changes.
- Submit PRs against the specific workstream folder; include rationale and links to issues.

## Expected artifacts per workstream
- `spec.md` — draft specification.
- `invariants.md` — enforceable properties (must/should).
- `conformance-outline.md` — how to test/verify.
- `diagrams/` — architecture diagrams (Mermaid/PlantUML preferred).

## ADRs
- Use `decisions/ADR-XXXX.md` to capture architectural decisions.
- Include context, options, decision, and consequences.

## Changelog and tags
- Update `CHANGELOG.md` for notable changes that affect architecture, evidence semantics, adapters, mappings, runtime examples, or contributor workflow.
- Do not add every typo or link fix; group related work into meaningful milestones.
- Repo release tags use annotated SemVer-style tags: `vMAJOR.MINOR.PATCH`.
- Tag meaning:
  - `MAJOR`: repo-level reshaping or breaking semantic changes across the published ECS contract.
  - `MINOR`: new implementable surfaces, major new mappings, adapters, runtime kits, or materially expanded evidence semantics.
  - `PATCH`: fixes, clarifications, and non-breaking semantic tightening.
- Until `v1.0.0`, minor releases may still contain breaking changes. If they do, call them out explicitly in `CHANGELOG.md`.
- Invariant/profile versions inside docs remain independent of repo tags. Repo tags version the repository snapshot, not each internal spec surface.
- Prefer tagging after grouped milestones rather than after every merge.

## Style
- Markdown, concise and testable language.
- Prefer “must/should/may” with rationale.
- Keep examples vendor-neutral; call out assumptions.
- Use Mermaid for diagrams by default.

## Licensing
- Proposed: Creative Commons BY 4.0 for documentation (to be confirmed).

## Getting help
- File an issue with `question` or `discussion` labels.
