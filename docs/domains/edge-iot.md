# Edge & IoT (Draft, Non‑Normative)

## Purpose
Clarify how ECS primitives apply to edge and IoT deployments where connectivity is intermittent and local autonomy is required.

## Scope
- Edge clusters, gateways, and IoT workloads that must operate under partial connectivity.
- Focuses on authority/policy caching, fail‑closed behavior, and evidence buffering.
- Does not define device protocols or IoT platform requirements.

## Core expectations (ECS‑aligned)
- **Authority & policy caching:** local snapshots MUST be used when upstream is unavailable.
- **Fail‑closed semantics:** governed actions MUST refuse if authority/policy cannot be verified.
- **Evidence buffering:** events MUST be captured locally and reconciled after reconnect.
- **Jurisdictional routing:** edge failover across borders MUST be policy‑checked and evidenced.

## Evidence considerations
- Use Core10‑05 envelope for edge events.
- Export bundles MUST declare `evidence_profile_id` and include chain fields when required.
- Buffer integrity and reconciliation are mandatory (CRP/WS5).

## Notes
Edge/IoT is a deployment context, not a new ECS layer. ECS remains the contract; implementation choices are left to providers.
