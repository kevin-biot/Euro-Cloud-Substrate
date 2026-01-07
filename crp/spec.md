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

## Dependencies
- WS3 (Execution Envelopes) for envelope behavior under partition.
- WS5 (Evidence & Audit) for buffering/reconciliation semantics.
- WS2 (EOSC) for in-jurisdiction data handling.
- WS4 (Interop API) for export/reconciliation once connectivity resumes.
