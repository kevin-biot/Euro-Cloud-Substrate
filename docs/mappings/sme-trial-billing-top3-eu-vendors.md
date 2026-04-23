# SME Trial, Billing, and Limit Warnings for Top-3 EU Vendors (Draft, Non-Normative)

## Purpose
Provide a dated operational-commercial snapshot for SMEs and early-stage teams asking:

**"Can we safely experiment on this provider without getting trapped by unclear trial terms, billing surprises, or missing spend visibility?"**

This is not an architecture score.
It is a practical onboarding-risk note.

## Snapshot date
**This snapshot reflects public materials reviewed on 2026-04-23.**

Commercial terms can change materially faster than technical docs.
Re-check official pricing and legal pages before relying on this for any actual buying decision.

## Why this matters
Many SMEs do not reject a cloud because it lacks compute.
They reject it because:
- they cannot tell what the free path is,
- they do not know when billing starts,
- they do not know what happens after credits expire,
- or they do not trust themselves not to get surprised.

The easier and clearer the experimentation path, the easier it is for an SME to test sovereign alternatives.

## Reading guide
- `Clear` = the public trial/billing posture is easy to understand from official sources.
- `Fragmented` = some trial or promotional paths exist, but they are not presented as one clear cloud-experiment story.
- `Unclear` = public legal/commercial signals exist, but the practical experimentation path is not cleanly obvious.

## Official sources used

### OVHcloud
- Public Cloud free trial (US): [OVHcloud](https://us.ovhcloud.com/public-cloud/free-trial/)
- Public Cloud free trial (FR): [OVHcloud](https://www.ovhcloud.com/fr/public-cloud/free-trial/)

### Scaleway
- Free MongoDB trial: [Scaleway](https://www.scaleway.com/en/free-mongodb/)
- Startup program: [Scaleway](https://www.scaleway.com/en/startup-program-3/)
- Billing docs: [Scaleway](https://www.scaleway.com/en/docs/billing/how-to)

### STACKIT
- Cloud terms of use: [STACKIT](https://stackit.com/en/asset/download/34542/file/Terms_of_use_STACKIT_Cloud.pdf?inLanguage=eng-DE)
- Price list: [STACKIT](https://stackit.com/en/asset/download/37788/file/STACKIT_price_list.pdf?version=13)

## Snapshot matrix
| Surface | OVHcloud | Scaleway | STACKIT | Notes |
|---|---|---|---|---|
| Broad public cloud trial signal | Clear | Fragmented | Unclear | OVHcloud has the clearest public-cloud experimentation story. Scaleway appears stronger on product- or program-specific offers. STACKIT publicly references free products for trial purposes, but the onboarding path is less obvious. |
| Free credits / trial scope | Clear | Fragmented | Unclear | OVHcloud clearly advertises public-cloud credits. Scaleway has targeted free trials and startup credits. STACKIT requires more reading across terms and product material. |
| Payment method requirement | Clear | Likely yes / verify | Likely yes / verify | OVHcloud states this explicitly. For the others, assume payment method and identity checks will matter unless proven otherwise. |
| Billing after trial/credit exhaustion | Clear | Likely standard billing / verify | Likely standard billing / verify | OVHcloud states auto-billing clearly once credits are exhausted. SMEs should assume normal billing starts unless the provider states otherwise. |
| Spend visibility / billing docs clarity | Medium | Medium | Medium | All three need more direct hands-on validation on alerting, limits, and proactive cost warnings. |
| SME experimentation confidence | Strong | Medium | Medium-Low | OVHcloud currently has the clearest “try this now” commercial path. Scaleway may still be attractive, but the public experimentation story is less unified. STACKIT looks promising but less frictionless from public materials alone. |

## Provider notes

### OVHcloud
- Strongest public experimentation story of the three.
- Clear public-cloud trial messaging with credits and an explicit post-credit billing model.
- Explicit warning for SMEs:
  - payment method is required,
  - billing starts automatically after credit exhaustion or expiry if resources remain active.

### Scaleway
- Public offers appear more fragmented:
  - specific free product trials,
  - startup program credits,
  - product-level incentives.
- This may be perfectly workable in practice, but it is not as clear as one unified “here is your cloud trial” path.
- Explicit SME warning:
  - do not assume a broad free tier just because some product trials exist.

### STACKIT
- Public legal terms clearly mention free products for trial purposes.
- But the broad practical story for a small team wanting to spin up a few services and learn the platform is less immediately obvious from public materials.
- Explicit SME warning:
  - treat the experimentation path as a sales-assisted or terms-driven onboarding model until proven otherwise.

## Billing and limit warnings SMEs should care about
Regardless of provider, check these before experimenting:

1. Does the provider require a credit card or payment method before trial activation?
2. Does billing begin automatically when credits expire or trial ends?
3. Are idle resources still billable?
4. Are there region restrictions on the trial?
5. Are managed databases, object storage, and egress included in credits?
6. Are observability/logging products billed separately from compute?
7. Are there built-in budget alerts or only billing dashboards?

If the answer is unclear, assume the risk exists.

## Recommended SME guardrails
If you are testing any provider:
- create one dedicated trial project,
- set naming conventions for all test resources,
- record activation date and expected expiry,
- set a diary reminder before expiry,
- delete unused resources immediately,
- export billing screenshots or usage summaries during the trial,
- test one small end-to-end slice only.

For ECS-style evaluation, that slice should be:
- Kubernetes or API runtime,
- object storage,
- database,
- logs/observability,
- one ingress/TLS endpoint.

## ECS relevance
This surface is not core architecture, but it matters strategically.

If SMEs cannot cheaply and safely test EU cloud providers:
- they stay on AWS by default,
- they never reach the stage where sovereignty evidence matters,
- and the whole market conversation stays abstract.

So while trial/billing posture is not an ECS invariant, it is a real adoption surface.

## Recommended use
Use this with:
- `docs/mappings/deployer-utility-top3-eu-vendors.md`
- `docs/mappings/aws-core-to-top3-eu-vendors.md`
- `docs/mappings/eu-cloud-provider-selection-matrix.md`

That combination gives:
- operator usability,
- practical parity,
- and experimentation risk.
