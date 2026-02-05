# Open‑Source Landing Zone Reference (Draft)

## Intent
Outline the minimum components an open‑source landing zone implementation would need to satisfy OLZ‑EU as a portable standard.

## Minimum capabilities
1. **Identity & authority binding**
   - Tenant/project creation tied to explicit authority binding.
   - OIDC federation support and evidence emission for identity actions.

2. **Network baseline**
   - Default‑deny segmentation, egress controls, and declared connectivity dependencies.
   - Evidence of network posture and changes.
   - Optional service mesh for policy enforcement at L7 with evidence emission.
   - Optional L4/L7 ingress, WAF, and load‑balancer layers; if they enforce policy or route governed traffic, they SHOULD emit evidence (allow/refuse, geo/jurisdiction rules).

3. **Policy admission**
   - Admission gate enforcing policy snapshot binding and refusal semantics.
   - Deterministic policy evaluation and fail‑closed behavior.

4. **Evidence emission**
   - Evidence events for all control‑plane actions.
   - Exportable evidence bundles per `docs/evidence/export-schema.md`.

5. **Portability hooks**
   - Standard interop API surface for tenant operations.
   - Explicit exit/migration hooks for governance artifacts.

## Landing‑zone setup best practices (generic)
These are implementation‑agnostic principles to set up clusters, users, and workloads in a governed way.

1. **Tenant first, workloads last**
   - Create tenant/project boundaries before any workload admission.
   - Require authority binding and policy baseline at tenant creation.

2. **Identity is scoped and minimal**
   - Use least‑privilege roles; avoid global admin for tenants.
   - Bind users and services to tenant‑scoped identities with explicit authority.

3. **Org groups and role mapping**
   - Define org groups (e.g., platform operators, security, app teams) and map them to roles explicitly.
   - Use group‑based access for routine actions; avoid ad‑hoc user grants.
   - Require time‑bounded elevation for privileged actions and evidence it.

4. **Default‑deny networking**
   - Start with deny‑all; open egress/ingress by explicit policy only.
   - Record all changes as evidence events with policy snapshots.

5. **Admission as a control point**
   - All workload creation/updates pass through policy admission.
   - Refusals are first‑class and evidenced.

6. **Evidence by construction**
   - Emit evidence for identity, policy, network, and workload actions.
   - Ensure evidence exports are available from day one.

7. **Explicit data governance**
   - Apply governance metadata (jurisdiction/classification/retention) at data creation.
   - Refuse data flows that violate jurisdictional policy.

8. **Operational boundaries**
   - Separate operator actions from tenant actions; log and evidence both.
   - Keep break‑glass access time‑bounded and auditable.

## Portable control surface (draft)
A practical ECS landing zone should include a portable **control surface** for provisioning and workload movement:
- **CLI/IaC** for repeatable provisioning across providers.
- **GitOps/CD pipelines** for deployment, rollback, and migration.
- **Evidence hooks** integrated into pipelines to emit ECS events.

If ECS APIs are standardized, open‑source pipelines can implement **portable workflows** to move workloads and data across providers without provider‑specific tooling.

See `docs/guides/pipeline-schema.md` for a minimal pipeline schema and evidence hook guidance.

## Reference stack candidates (non‑normative)
- Identity: Keycloak or equivalent OIDC provider.
- Policy: OPA/Kyverno admission controls.
- Control plane: OKD or OpenStack (VM‑first).
- Evidence: ECS evidence exporter + chain anchoring adapter.

## Notes
- This is a gap area in the open‑source ecosystem; ECS defines the contract but does not mandate a stack.
- Service mesh is a valid optional layer; if used for policy/egress control it should emit evidence and be declared in exit manifests.
- Load balancers and WAF/Ingress are optional; if they influence jurisdictional routing (e.g., failover across borders), refusal or routing decisions MUST be evidenced.

### Examples (jurisdictional routing evidence)
- **Failover blocked**: L4 LB attempts to route to a non‑sovereign region → refusal evidence with jurisdiction rule + target region.
- **WAF geo‑policy**: request denied due to geo/jurisdiction policy → refusal evidence with policy snapshot id.
- **Ingress routing**: tenant traffic routed only to approved zone/cluster → routing decision evidence with policy snapshot id.
