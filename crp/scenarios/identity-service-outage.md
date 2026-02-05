# Scenario: Identity Service Outage

## Trigger
- Upstream IdP or federation service is unreachable.
- Token validation and credential verification fail or time out.

## Expected CRP behavior
- **Fail‑closed** for governed actions requiring fresh authority verification.
- Continue **non‑governed** or pre‑authorized operations only if policy allows cached authority snapshots.
- Emit explicit **refusal evidence** for all blocked actions.

## Evidence generation
- `crp.partition.state` event indicating authority verification outage.
- Refusal events for governed actions with:
  - `authority_snapshot_id` (cached version, if used)
  - `policy_snapshot_id`
  - `refusal_reason=authority_unavailable`
- Evidence buffered locally until reconnection (CRP/WS5).

## Recovery path
- On IdP recovery, reconcile buffered evidence into the main chain.
- Re‑verify token validity and policy snapshot freshness.
- Resume governed actions only after successful authority checks.
