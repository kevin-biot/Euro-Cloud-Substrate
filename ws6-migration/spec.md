# WS6 Spec (Draft)

## Objectives
- Define migration and portability expectations for ECS workloads and data.

## Invariant families (refs)
- EXIT (exit path, validation)
- INT (interop for migration/export)
- DEP (dependency declarations affecting portability)
- SUP (supply-chain visibility for migrated artifacts)
- EVID (evidence of migration/validation)

## Sections to draft
- Migration scenarios (container, VM, data-only, evidence-only).
- Policy and authority portability.
- Evidence and audit artifact transfer requirements.
- Verification, rollback, and downtime expectations.

## Federation roles (non-normative)
In the IPCEI‑CIS reference architecture, the Federation Manager role coordinates federation and cross‑provider operations. ECS maps this to migration control-plane capabilities:
- Export/import orchestration with evidence (Core10‑10, WS6).
- Portability validation and rollback with evidence (Core10‑10).
- Interop API surface for migration endpoints (WS4).

The Federation Broker role maps to discoverability and claims (profile claims, bundle examples), which ECS treats as contract inputs rather than a mandated broker product.
