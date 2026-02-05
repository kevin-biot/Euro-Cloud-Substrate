# Competition & Differentiation (Draft)

## Purpose
ECS standardizes **verifiable governance and portability**, not the commercial layer. Conformance is a minimum contract; it does not remove competition.

## What ECS standardizes (the contract layer)
- Evidence envelopes, integrity, and exportability.
- Authority/policy binding and refusal semantics.
- Portability requirements (interop + migration).
- Minimum controls for landing zones and execution envelopes.

## API fragmentation gap (why ECS matters)
Cloud API fragmentation is a major lock‑in vector: each provider’s proprietary surface slows integration, complicates portability, and raises switching costs.  
ECS does **not** replace provider APIs. Instead, it standardizes the **governance/evidence contract** so different API surfaces can still be audited, compared, and migrated.

## What ECS leaves open (competitive differentiation)
Vendors can still compete on:
- **Performance tiers** (latency, IOPS, throughput).
- **Reliability/SLA** commitments and operational excellence.
- **Managed services** (databases, AI/ML, analytics, observability).
- **Security add‑ons** (HSMs, advanced KMS, higher isolation profiles).
- **Operational UX** (dashboards, incident tooling, developer workflow).
- **Platform extensions** (e.g., CRDs/operators) that add capabilities beyond the core contract.
- **Cost models** (pricing, discounts, egress strategies).
- **Regional specialization** (local expertise, jurisdictional support).
- **Vertical bundles** (healthcare, public sector, defense‑grade profiles).

## Conformance ≠ commoditization
ECS ensures **trust and portability** are provable. Vendors can exceed ECS by:
- Supporting stronger evidence profiles (e.g., NCP, regulated‑ML).
- Providing richer export tooling and verifier support.
- Offering higher integrity/availability guarantees.

## Example: Same contract, different value
Two providers can both export ECS‑compliant evidence bundles, but one may:
- deliver lower latency and higher availability,
- provide managed ML services with stronger evidence hooks,
- include specialized compliance packaging,
while the other competes on lower cost or local presence.

## Summary
ECS defines **minimum interoperability and auditability**. Everything above that is where competition thrives.

## Companion standard (future‑looking)
If ECS gains traction, a **separate Cloud API standard** could emerge to define common service surfaces.  
ECS would remain the **contract layer**, while the API standard defines the **interface layer**; vendors would then compete above both.
