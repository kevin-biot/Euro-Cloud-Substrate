# Tenant Isolation Contract — Placeholder

## Intent
Minimum isolation semantics across compute, storage, network, logs, and indexes.

## Scope and assumptions
- Applies to multi-tenant ECS deployments where tenant boundaries are enforced by policy and technical controls.
- Covers isolation by default; explicit cross-tenant access is treated as an exception with evidence.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Tenant boundary: logical and technical separation across identity, compute, storage, network, and telemetry.
- Isolation domain: a control plane or data plane surface where tenant separation must be enforced.
- Cross-tenant access: any read/write/execute action that crosses a tenant boundary.
- Shared infrastructure: components used by multiple tenants (hypervisors, storage clusters, control planes).

## Isolation domains (draft)
- Compute: workloads run in isolated envelopes; no cross-tenant memory, process, or runtime access.
- Network: default-deny between tenants; explicit allowlists for approved flows.
- Storage: object, block, and file surfaces enforce tenant-scoped access; metadata and logs are tenant-scoped.
- Logs/telemetry: separate indexes/tenancy tags; access restricted by tenant authority binding.
- Control plane: tenant-scoped IAM/RBAC; administrative actions are tenant-bound and audited.

## Invariant families (refs)
- EXEC (isolation enforcement)
- DATA (storage/logs isolation)
- DEP (critical path declarations)
- PHY (connectivity constraints)
- EVID (evidence of isolation controls)

## Applicable invariant IDs
- EXEC-01/02/03/04/05, DATA-01/02/04, DEP-01/02/04, PHY-01/02, EVID-01/03/04

## Evidence expectations
- Isolation policies and enforcement logs; admission outcomes.
- Dependency/critical-path declarations; connectivity constraints.
- Evidence of refusals/violations and integrity-protected logs.

## Requirements (draft v1)
- Workloads MUST be isolated by tenant; cross-tenant access MUST be explicitly authorized and evidenced (EXEC-01/02).
- Network segmentation MUST prevent unintended cross-tenant traffic by default; cross-tenant flows MUST be explicitly authorized (PHY-01/02).
- Storage/logs MUST enforce tenant boundaries; objects/logs MUST NOT be accessible across tenants without explicit policy (DATA-01/02).
- Isolation verification MUST be testable; evidence of isolation checks MUST be recorded (EVID-01/03).
- Dependency declarations MUST identify shared infrastructure that could affect isolation (DEP-01/02).

## Cross-tenant access policy (draft)
- Cross-tenant access MUST be time-bounded, least-privilege, and tied to explicit authority.
- Grants MUST include scope, duration, and evidence pointer; default remains deny.
- All cross-tenant requests MUST emit evidence (allow/refuse) with authority/policy snapshot ids.

## Conformance outline (draft v1)
- Verify tenant A cannot access tenant B resources without explicit authorization; refusals are evidenced.
- Test network segmentation blocks cross-tenant traffic by default; authorized flows are evidenced.
- Validate storage/log boundaries; access respects tenant scope and is evidenced.
- Confirm isolation verification/tests produce evidence; shared dependencies declared.

## To cover
- Isolation guarantees (technical and procedural).
- Cross-tenant leakage prevention and verification hooks.
- Evidence requirements for isolation controls.

## Invariants (draft)
- Compute, storage, network, logs, and indexes MUST enforce tenant isolation by default.
- Isolation controls MUST be verifiable through evidence (attestation, logs, or tests).
- Cross-tenant access MUST be explicit, least-privilege, and evidence-backed.

## Next steps
- Define testable invariants.
- Align with Execution Envelopes and Control Plane policies.
