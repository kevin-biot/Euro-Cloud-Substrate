# Architecture Decision Records (ADRs)

## Purpose
ADRs capture decisions that shape ECS semantics, scope, or governance. They are concise and durable; specs and mappings may evolve, but ADRs explain the rationale.

## Conventions
- Filenames: `ADR-####-short-title.md`
- Status: Proposed | Accepted | Deprecated | Superseded
- Scope: decisions should be narrow and reference invariants or Core10 where relevant.

## ADR Index
1. `ADR-0001-authority-before-execution.md` — Authority checks are required before governed execution.
2. `ADR-0002-invariants-source-of-truth.md` — `docs/invariants/v0.3.md` is authoritative.
3. `ADR-0003-profiles-reference-invariants.md` — Profiles can only tighten existing invariants.
4. `ADR-0004-irn-alignment-mechanism-only.md` — IRN alignment is mechanism‑only, not certification.
5. `ADR-0005-capability-scoped-ai-media.md` — AI media invocations should be capability‑scoped (STA‑L pattern).

## When to add an ADR
- Changes to invariant semantics or scope.
- Introduction of new profile types or evidence obligations.
- Governance shifts (process, ownership, or decision authority).
