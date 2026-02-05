# ECS vs Existing Stacks (Complementary Positioning)

ECS is governance-first and aims to complement, not replace, provider stacks.

## Themes
- **Connectivity posture:** Hyperscaler edge stacks optimise for hub-spoke connectivity; ECS CRP enables sustained autonomous operation during segmentation events.
- **Authority provenance:** Existing stacks provide RBAC; ECS adds legislative-grade authority-before-execution and refusal semantics (IALP/CRP).
- **Evidence:** Provider logs focus on observability; ECS requires immutable, ordered evidence (IALP) and audit-chain portability.
- **Data governance:** ECS mandates governance metadata (EOSC) that travels with objects across providers.
- **Portability:** ECS defines minimum interop APIs and migration baselines to reduce provider lock-in.

## Comparison matrix (complementary positioning)
| Capability | ECS (contract layer) | AWS Outposts/Local Zones | Azure Stack/Arc | Google Anthos | EU providers |
|---|---|---|---|---|---|
| Landing zone | OLZ‑EU + authority binding | Provider‑specific | Provider‑specific | Provider‑specific | Varies by provider |
| Policy/authority | Authority‑before‑execution + refusal evidence | RBAC + IAM policies | RBAC + Azure policies | RBAC + policies | Varies by provider |
| Evidence/audit | Core10‑05 + export bundles | Logs/CloudTrail (provider‑specific) | Logs/Activity (provider‑specific) | Logs/Cloud Audit (provider‑specific) | Varies by provider |
| CRP/partition | Explicit fail‑closed + partition evidence | Operational best‑effort | Operational best‑effort | Operational best‑effort | Varies by provider |
| Object metadata governance | EOSC metadata contract | Provider‑specific metadata | Provider‑specific metadata | Provider‑specific metadata | Varies by provider |
| Portability baseline | WS4/WS6 contracts | Limited, provider‑specific | Limited, provider‑specific | Limited, provider‑specific | Varies by provider |

## Reference comparisons (non-exhaustive)
- AWS Outposts / Local Zones
- Azure Stack / Arc
- Google Anthos
- EU providers (e.g., OVH, Scaleway)

Use this matrix to articulate how ECS adds governance and resilience layers above these offerings. Keep language neutral and complementary.
