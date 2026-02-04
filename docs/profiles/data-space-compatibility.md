# Data Space Compatibility Profile — Draft (Non‑Normative)

## Purpose
Define a profile for **enforceable, auditable data‑space participation** without mandating any specific data‑space platform. This profile is a contract layer over ECS primitives.

## Scope (in scope)
- Federated identity and trust for cross‑org data sharing.
- Policy decision + enforcement points (PDP/PEP) with **usage obligations**.
- Evidence for sharing/processing decisions and post‑access obligations.
- Minimal data‑product descriptor contract and portability.
- Connector pattern as a reference (non‑normative).

## Out of scope
- Implementing a data‑space platform (GAIA‑X/IDS/EDC/etc.).
- Sector governance, ontologies, or marketplace operations.

## Required primitives (profile expectations)
### Identity & trust
- Federated identity for org‑to‑org and service‑to‑service access (AUTH/POL).
- Authority bindings and policy snapshots MUST be referenced in access decisions.

### Policy decisions + obligations
- Policy MUST express **purpose binding** and **post‑access obligations** (e.g., no onward transfer, delete after N days, compute only in approved environment).
- Obligation verification MUST emit evidence (see events below).

### Evidence & audit
- Sharing and access decisions MUST emit evidence using Core10‑05.
- Evidence exports MUST declare `evidence_profile_id` and include chain fields when required.

### Data product descriptor (minimum)
- Data products MUST expose the descriptor contract in `docs/invariants/data.md`.
- Descriptor MUST include ownership, jurisdiction, classification, policy snapshot, and evidence pointer.

### Portability
- Data product exports MUST preserve governance metadata and evidence references (INT/EXIT).
- Refusals MUST emit evidence when portability is blocked.

## Required evidence events (profile)
Implementers SHOULD support the following events (see `docs/evidence/catalog.md`):
- `data.product.publish`
- `data.product.update`
- `data.access.grant` / `data.access.refuse`
- `data.obligation.verify`
- `data.usage.receipt` (when applicable)

## Connector pattern (non‑normative)
An ECS‑aligned data‑space connector:
- Validates identity + authority bindings.
- Evaluates policy with obligations and purpose binding.
- Emits evidence events for sharing decisions and obligation checks.
- Exposes export bundles for audit and portability.

## Mapping to Core10 / WS
- Core10‑01 (OLZ) — tenant/authority binding
- Core10‑03 (EOSC) — governance metadata and evidence pointers
- Core10‑04 (Policy & Authority) — policy snapshots and refusal semantics
- Core10‑05/06 — evidence envelopes and audit chain
- Core10‑08/10 — interop and portability
- WS1/WS4/WS6 — federation, interop APIs, migration/export

## Applicable invariant IDs (non‑exhaustive)
- AUTH‑01/02/04, POL‑01/02/04/05
- DATA‑01/02/04/05, EVID‑01/03/04/05
- INT‑01/03, EXIT‑01/02/03

## Notes
This profile **does not** redefine invariants. It selects and tightens existing invariants for data‑space interoperability.
