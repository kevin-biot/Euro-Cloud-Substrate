# Data Services (Queues/Streams) — Draft (Non‑Normative)

## Purpose
Define governance expectations for queues, streams, and internal data services that can move regulated data across boundaries.

## Scope
- Applies to message queues, event streams, and internal data buses.
- Focuses on governance metadata, policy enforcement, and evidence emission.
- Does not mandate a specific broker or vendor.

## Core expectations (contract‑level)
- **Governance metadata** (jurisdiction, classification, policy snapshot) MUST be associated with topics/queues.
- **Publish/subscribe decisions** MUST be policy‑checked and evidenced (allow/refuse).
- **Sovereignty boundary routing** MUST default‑deny unless explicitly authorized.
- **Dependency declarations** MUST identify non‑sovereign managed brokers.
- **Refusal evidence** MUST be emitted when routing is blocked by policy or jurisdiction.

## Evidence expectations
- Emit evidence for:
  - `queue.publish`, `queue.consume`
  - `stream.publish`, `stream.subscribe`
  - `data.route.refuse`
- Evidence should include policy/authority snapshot ids, jurisdiction/classification, and outcome.

## Notes
This is a governance layer: providers can still offer queue/stream services as competitive differentiators, but they must surface policy‑driven routing decisions and evidence.
