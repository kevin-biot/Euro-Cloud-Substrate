# WS6 Spec (Draft)

## Objectives
- Define migration and portability expectations for ECS workloads and data.

## Invariant families (refs)
- EXIT (exit path, validation)
- INT (interop for migration/export)
- DEP (dependency declarations affecting portability)
- SUP (supply-chain visibility for migrated artifacts)
- EVID (evidence of migration/validation)

## Terms (WS6 scope)
- **migration bundle**: Export package containing data, workloads, evidence, and verifier inputs.
- **portability validation**: Checks that the target environment can enforce policy/authority and data constraints.
- **cutover window**: Period when traffic is switched to the target environment.
- **rollback plan**: Documented procedure to return to source on failed validation.
- **dependency manifest**: Declared non‑substitutable dependencies affecting portability.

## Sections to draft
- Migration scenarios (container, VM, data-only, evidence-only).
- Policy and authority portability.
- Evidence and audit artifact transfer requirements.
- Verification, rollback, and downtime expectations.

## Requirements (draft v1)
- Providers MUST support export/import for: container workloads, VM workloads, data‑only, and evidence‑only scenarios.
- Policy and authority snapshots MUST migrate with workloads/data and be enforceable on the target.
- Governance metadata MUST be preserved across export/import (jurisdiction, classification, retention, evidence pointers).
- Migration MUST emit evidence events for export, import, validation, cutover, and rollback/refusal.
- Export bundles MUST declare `evidence_profile_id` and include chain fields required by the selected profile.
- Post‑migration validation MUST complete before governed execution resumes.
- Rollback MUST be supported when validation fails or cutover is aborted.
- Dependency manifests MUST be included to identify non‑substitutable components affecting portability.

## Migration scenarios (draft)
- **Container**: image + config + policy/authority snapshots + evidence; validate admission in target.
- **VM**: disk image + vTPM/attestation artifacts (if present) + policy/authority snapshots.
- **Data‑only**: governed data export with metadata, usage receipts, and evidence bundle.
- **Evidence‑only**: export evidence chain segments and verifier inputs without data movement.

## Stateful portability limits (draft)
- Some stateful assets (e.g., PVCs, managed database internals) may not be portable across providers.
- Providers MUST declare such limits in capability claims and refuse unsupported migrations with evidence.
- Where possible, provide an alternative portability path (object export, snapshot export, or evidence‑only export).

## Evidence and export alignment
- Evidence events MUST use the Core10‑05 envelope.
- Export manifests MUST include `evidence_profile_id`, range (from/to sequence), and verifier inputs.
- Refusals (e.g., blocked by jurisdiction/policy) MUST emit refusal evidence with reasons.

## Federation roles (non-normative)
In the IPCEI‑CIS reference architecture, the Federation Manager role coordinates federation and cross‑provider operations. ECS maps this to migration control-plane capabilities:
- Export/import orchestration with evidence (Core10‑10, WS6).
- Portability validation and rollback with evidence (Core10‑10).
- Interop API surface for migration endpoints (WS4).

The Federation Broker role maps to discoverability and claims (profile claims, bundle examples), which ECS treats as contract inputs rather than a mandated broker product.

See `docs/domains/federation.md` for the federation domain summary and evidence expectations.
