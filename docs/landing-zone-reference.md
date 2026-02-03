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

3. **Policy admission**
   - Admission gate enforcing policy snapshot binding and refusal semantics.
   - Deterministic policy evaluation and fail‑closed behavior.

4. **Evidence emission**
   - Evidence events for all control‑plane actions.
   - Exportable evidence bundles per `docs/evidence-export-schema.md`.

5. **Portability hooks**
   - Standard interop API surface for tenant operations.
   - Explicit exit/migration hooks for governance artifacts.

## Reference stack candidates (non‑normative)
- Identity: Keycloak or equivalent OIDC provider.
- Policy: OPA/Kyverno admission controls.
- Control plane: OKD or OpenStack (VM‑first).
- Evidence: ECS evidence exporter + chain anchoring adapter.

## Notes
- This is a gap area in the open‑source ecosystem; ECS defines the contract but does not mandate a stack.
