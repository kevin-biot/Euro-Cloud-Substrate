# Crisis Resilience Profile (CRP) — Overview

## Purpose
CRP defines the minimum execution posture for workloads that must continue operating under degraded or partitioned conditions, with governance intact. It is designed to handle operational uncertainty without making political or geopolitical claims.

## Scope
- Applies only to workloads explicitly designated as CRP‑compliant.
- Extends Core10 invariants with local authority/policy continuity, control‑plane independence, data residency, and evidence buffering.

## Key elements
- **Local authority/policy**: cached or locally authoritative snapshots are used during partition; fail‑closed if stale.
- **Control‑plane independence**: CRP workloads continue without upstream scheduler availability.
- **Deterministic degradation**: reduced‑capability modes are predefined and auditable.
- **Evidence buffering**: evidence persists locally and reconciles after connectivity returns.
- **Residency enforcement**: data required for continuity stays in‑jurisdiction during partition.

## Tiers (draft)
- **Tier 1 — Smoke**: basic partition survivability and evidence buffering.
- **Tier 2 — Integration**: sustained partition with local control‑plane behavior.
- **Tier 3 — Stress**: prolonged partition, load stress, deterministic degradation verification.

## Evidence expectations
- Local cache validity and staleness checks.
- Degraded mode activation and refusal outcomes.
- Evidence buffering and reconciliation logs with integrity proofs.
- Partition scenario declarations and test results.

## Related documents
- Spec: `crp/spec.md`
- Invariants: `crp/invariants.md`
- Conformance outline: `crp/conformance-outline.md`
- Diagrams: `crp/diagrams/`
- Scenarios: `crp/scenarios/`
- Edge/IoT note: `docs/domains/edge-iot.md`

## Dependencies
- WS3 (Execution Envelopes)
- WS5 (Evidence & Audit)
- WS2 (EOSC storage)
- WS4 (Interop API)
