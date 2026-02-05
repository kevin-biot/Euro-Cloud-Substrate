# Evidence vs Logs (Draft)

## Purpose
Explain the difference between **runtime evidence** and **post‑hoc logs**, why pre‑hoc evidence reduces compliance burden, and how this supports human‑in‑the‑loop and explainability requirements.

## The core distinction
- **Logs** are operational traces (often incomplete, inconsistent, or non‑portable).
- **Evidence** is a **governance artifact**: decision‑time, verifiable, and exportable.

ECS is designed around evidence, not log aggregation.

## Pre‑hoc vs post‑hoc
- **Pre‑hoc evidence**: emitted at the decision point (policy/authority evaluation), tied to the policy snapshot in force.
- **Post‑hoc logs**: reconstructed later, often without the original decision context.

Pre‑hoc evidence reduces:
- audit reconstruction cost,
- compliance disputes,
- reliance on untrusted log pipelines.

## Why this matters for AI and human‑in‑the‑loop
- **Explainability** is not just model math; it includes *who* approved, *what* policy applied, and *why* a decision was allowed or refused.
- **Human‑in‑the‑loop** actions must be captured as evidence (approval/refusal/escalation).
- Without evidence at runtime, AI Act‑style explainability becomes guesswork.

## The cloud gap ECS addresses
Most clouds provide logs and telemetry, but **not portable evidence**.  
ECS provides:
- a canonical evidence envelope (Core10‑05),
- export bundles with integrity proofs,
- refusal and escalation as first‑class outcomes.

## Relationship to the Compliance Pattern Library
ECS evidence aligns to the patterns in `docs/compliance/pattern-library.md` (e.g., usage receipts, policy snapshots, audit chains).

## Practical takeaway
If you can export evidence bundles, you reduce the need for bespoke post‑hoc reporting and make audits repeatable across providers.
