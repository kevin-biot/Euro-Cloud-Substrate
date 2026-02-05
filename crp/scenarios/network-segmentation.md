# Scenario: Network Segmentation

## Trigger
- Network partitions isolate control plane from execution plane or data plane.
- Cross‑region connectivity drops; egress is restricted by policy.

## Expected CRP behavior
- **Local autonomy** continues using cached authority/policy snapshots within TTL.
- **Deterministic routing**: requests are routed only to approved in‑jurisdiction resources.
- **Fail‑closed** if routing would cross a disallowed boundary.

## Evidence generation
- `crp.partition.state` event with `partition_state=partitioned` and `buffer_mode=local`.
- Routing decision evidence with policy snapshot binding.
- Refusal evidence for out‑of‑jurisdiction failover attempts.

## Recovery path
- Reconcile buffered evidence when connectivity is restored.
- Re‑sync policy/authority snapshots and re‑validate cache freshness.
- Emit `crp.partition.state` with `partition_state=reconciled`.
