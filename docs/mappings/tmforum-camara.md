# TM Forum & CAMARA Mapping (Draft, Non‑Normative)

## What these standards are (short)
- **TM Forum Open APIs**: a broad OSS/BSS‑oriented suite covering service, product, resource, customer, and lifecycle management across partners. It is *operationally comprehensive* but outside ECS’s core scope. citeturn0search0
- **CAMARA**: a telco‑driven API surface (via GSMA Open Gateway) to expose network capabilities such as identity/number verification, QoS, edge discovery, and location. It is *capability‑focused* and closer to ECS’s interop goals. citeturn0search1

## What ECS should map (and why)
ECS should map only the **governance‑relevant primitives**:
- **Identity verification / auth context** → ECS AUTH/POL + evidence (decision + refusal logs).
- **QoS / edge discovery** → ECS EXEC/DEP/INT (routing + capability claims + refusal evidence).
- **Consent / purpose binding** → ECS DATA/EVID (usage receipts, obligations).

The goal is **evidence‑grade interoperability**, not OSS/BSS unification.

## What ECS should not absorb
- Full TM Forum object models (product catalog, customer billing, inventory, etc.).
- Provider‑specific service lifecycle workflows.
- Sector‑specific business process definitions.

ECS remains a **mechanism‑only substrate**: it defines the evidence and policy hooks that make cross‑provider interactions auditable and portable.

## API fragmentation gap (why this matters)
Cloud API fragmentation creates **lock‑in** and slows integration.  
ECS does not attempt to replace TM Forum or CAMARA, but it **standardizes the governance/evidence contract** so different API surfaces can interoperate and be verified.  
This makes portability and procurement possible even before full API convergence.

## Suggested alignment hooks (non‑normative)
- **Capability claims**: ECS interop should allow providers to declare which CAMARA‑like capabilities they expose.
- **Refusal evidence**: when capabilities cannot be supported (e.g., QoS unavailable), ECS requires refusal evidence with policy snapshot binding.
- **Consent evidence**: usage of identity/verification capabilities should emit consent/purpose bindings.
