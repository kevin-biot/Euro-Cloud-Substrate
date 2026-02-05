# Scenario: Stale Policy Cache

## Trigger
- Policy snapshot TTL expires while control plane is unreachable.
- Cached policy version is older than the minimum allowed by governance rules.

## Expected CRP behavior
- **Fail‑closed** for any governed action that requires current policy.
- Emit explicit refusals with `refusal_reason=policy_stale`.
- Continue only if policy allows operation under cached snapshot within a defined grace period.

## Evidence generation
- `crp.partition.state` event with `partition_state=degraded`.
- Refusal evidence for governed actions using stale policy cache.
- Evidence pointer references cached policy snapshot artifact for audit.

## Recovery path
- Refresh policy snapshot once connectivity is restored.
- Re‑issue authority/policy bindings and reconcile buffered evidence.
- Emit `crp.partition.state` with `partition_state=reconciled`.
