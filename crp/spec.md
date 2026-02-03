# Crisis Resilience Profile (CRP) — Spec (Draft)

## Objectives
Define the mandatory execution posture for critical workloads that must continue operating under degraded or partitioned conditions, with governance intact.

## Scope
- Applies to workloads explicitly designated as CRP-compliant.
- Extends Core 10 invariants with resilience requirements (local authority/policy, control-plane independence, data residency, evidence buffering).

## Design points
- Local authority/policy caches are authoritative during partition, with fail-closed behavior if stale or missing.
- Execution envelopes must run without upstream schedulers; degraded modes are deterministic and auditable.
- Evidence is buffered locally with later reconciliation.
- Data needed for continuity remains in-jurisdiction while partitioned.

## CRP tiers (draft)
- **Tier 1 — Smoke:** basic partition survivability (local auth/policy, fail-closed, evidence buffering).
- **Tier 2 — Integration:** sustained partition behavior with local control-plane and governed routing.
- **Tier 3 — Stress:** prolonged partition + volume stress + deterministic degradation verification.

## Required evidence (draft)
- Local authority/policy cache validity and staleness checks.
- Evidence buffering and reconciliation logs with integrity proofs.
- Degraded mode activation evidence and refusal outcomes.
- Partition scenario declarations and test results.

## Partition scenarios (examples)
- Identity/outbound authority outage with stale policy snapshot.
- Control-plane outage with local runtime continuity.
- Regional network partition with evidence buffering and in-jurisdiction data enforcement.

## Dependencies
- WS3 (Execution Envelopes) for envelope behavior under partition.
- WS5 (Evidence & Audit) for buffering/reconciliation semantics.
- WS2 (EOSC) for in-jurisdiction data handling.
- WS4 (Interop API) for export/reconciliation once connectivity resumes.
