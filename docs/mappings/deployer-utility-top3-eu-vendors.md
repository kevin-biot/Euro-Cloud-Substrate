# Deployer Utility Comparison for Top-3 EU Vendors (Draft, Non-Normative)

## Purpose
Compare the **deployer utility surface** of three EU cloud vendors for teams that need to build, ship, and automate infrastructure with minimal friction:
- **OVHcloud**
- **Scaleway**
- **STACKIT**

This is not a sovereignty score.
It answers a narrower question:

**"Can a small platform team, startup, or coding agent operate this provider through terminal-first tooling without excessive friction?"**

## Why this matters
Many cloud choices are lost before governance is even discussed.
The deciding factor is often simpler:
- is there a real CLI,
- is the API coherent,
- can auth be automated,
- can a team script common tasks without resorting to portal clicks.

AWS wins many startup decisions because its operator surface is coherent.
This document asks how close these EU vendors are on that practical day-to-day axis.

## Reading guide
- `Strong` = usable as a normal terminal-first operator surface.
- `Medium` = workable, but with visible friction or unevenness.
- `Weak` = possible, but not a serious default for a coding-heavy delivery workflow.

## Official sources
- OVHcloud CLI: [OVHcloud](https://support.us.ovhcloud.com/hc/en-us/articles/48181801023763-Getting-Started-with-OVHcloud-CLI)
- OVHcloud API getting started: [OVHcloud](https://support.us.ovhcloud.com/hc/en-us/articles/360018130839-First-Steps-with-the-OVHcloud-API)
- Scaleway API and auth: [Scaleway](https://www.scaleway.com/en/developer-api/)
- Scaleway Domains and DNS API: [Scaleway](https://www.scaleway.com/en/docs/domains-and-dns/)
- STACKIT CLI: [STACKIT](https://docs.stackit.cloud/stackit/en/stackit-cli-202179854.html)
- STACKIT service accounts: [STACKIT](https://docs.stackit.cloud/platform/access-and-identity/service-accounts/)
- STACKIT auth flows: [STACKIT](https://docs.stackit.cloud/platform/access-and-identity/service-accounts/authentication-flows/)

## Comparison matrix
| Surface | OVHcloud | Scaleway | STACKIT | Notes |
|---|---|---|---|---|
| Official CLI | Strong | Strong | Strong | All three now have an official CLI surface worth taking seriously. |
| Public API posture | Strong | Strong | Strong | All three expose an API-first story. STACKIT’s docs are increasingly coherent; Scaleway’s are very developer-facing; OVHcloud’s API surface is broad and mature. |
| Non-interactive auth | Medium | Medium | Strong | STACKIT’s service-account key flow is the most explicit machine-identity posture. OVHcloud and Scaleway are workable but still feel more API-key/token oriented. |
| Kubernetes automation path | Strong | Strong | Strong | This is now a credible strength zone for all three. |
| Object storage automation path | Strong | Strong | Strong | S3-compatible access plus provider CLI/API paths make this workable across all three. |
| DNS automation path | Medium | Strong | Strong | Scaleway and STACKIT document DNS as a first-class managed API surface. OVHcloud DNS is automatable, but the experience is less clearly cloud-integrated. |
| TLS / certificate automation path | Medium | Medium | Medium | All can be made to work, but none clearly matches AWS ACM as the smooth default operator experience. |
| Observability / logs automation path | Medium | Medium | Strong | STACKIT’s Observability surface is the clearest integrated managed story. Scaleway Cockpit is credible. OVHcloud Logs Data Platform is powerful but more tool-oriented than frictionless. |
| Secrets / KMS automation path | Medium | Strong | Strong | Scaleway and STACKIT are clearer on managed secret/KMS integration. OVHcloud has credible KMS/Secret Manager surfaces, but the story feels less unified. |
| Overall deployer utility | Medium-Strong | Strong | Strong | None matches AWS end-to-end coherence yet, but Scaleway and STACKIT currently read as the cleaner terminal-first operator surfaces. |

## Provider notes

### OVHcloud
- Strengths:
  - mature API culture,
  - official CLI,
  - broad object/K8s/database coverage,
  - powerful logs platform.
- Friction points:
  - auth and service composition still feel more “platform family” than single unified operator model,
  - DNS/cert flows are less obviously integrated into one tight default path.

### Scaleway
- Strengths:
  - very developer-oriented API/docs posture,
  - coherent CLI story,
  - strong DNS/API exposure,
  - strong secret/key manager story,
  - credible observability via Cockpit.
- Friction points:
  - certificate lifecycle still needs more hands-on validation against AWS-style expectations,
  - service breadth is good, but some production-operability questions still need PoC confirmation.

### STACKIT
- Strengths:
  - explicit service-account model for automation,
  - CLI and API maturity improving quickly,
  - strong DNS and observability docs,
  - stronger-than-average managed security service posture.
- Friction points:
  - some surfaces are still newer and need hands-on validation rather than doc-only confidence,
  - less ecosystem familiarity than AWS or OVHcloud in day-to-day operator culture.

## Practical deployer smoke tests
These are the minimum tests that matter for a terminal-first team:

1. Can the CLI authenticate without interactive prompts?
2. Can a script list or create a Kubernetes cluster?
3. Can a script list buckets or upload an object?
4. Can DNS records be managed by API/CLI?
5. Can logs/metrics be queried or listed programmatically?
6. Can secrets or keys be created and referenced in automation?

If a provider struggles on those six points, it will feel expensive to use even if the raw services exist.

## ECS relevance
This surface matters to ECS because deployer utility is how evidence and refusal semantics become real.

If the provider is too awkward to automate:
- the wrappers do not get built,
- evidence does not get emitted consistently,
- operators bypass the intended contract,
- and sovereignty collapses back into documentation and intent.

## Recommended use
Use this doc with:
- `docs/mappings/aws-core-to-top3-eu-vendors.md`
- `docs/mappings/eu-cloud-provider-selection-matrix.md`
- `docs/mappings/aws-against-ecs-gap-matrix.md`

This gives three distinct but related views:
- operator utility,
- AWS parity,
- ECS sovereignty/evidence gap.
