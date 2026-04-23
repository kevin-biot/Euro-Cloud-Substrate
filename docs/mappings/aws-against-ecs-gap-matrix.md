# AWS Against ECS Gap Matrix (Draft, Non-Normative)

## Purpose
Show where AWS can be operationally strong while still falling short of the **ECS sovereignty and runtime evidence contract**.

This matters because two different arguments are often collapsed into one:
- `AWS vs EU vendors on service coherence`
- `AWS vs ECS on sovereignty, refusal, and portable proof`

They are not the same comparison.

AWS may remain very strong on operator coherence and breadth while still leaving important ECS gaps open.

## Reading guide
- `Strong native support` means AWS offers a mature native surface close to the need.
- `Workaround possible` means the need can be approximated by additional layers, wrappers, or exports.
- `ECS gap` means the underlying ECS contract is not fully satisfied without substantial externalization or architectural compensation.

## Matrix
| ECS surface | AWS native support | Workaround possible | ECS gap | Why the gap matters |
|---|---|---|---|---|
| Authority before execution | Partial | Yes | Medium | IAM policies and identities are strong, but ECS wants the authority state preserved in a provider-neutral, verifier-readable way on the execution path. |
| Policy snapshot at execution time | Partial | Yes | Medium | AWS services evaluate policy, but ECS expects an explicit, addressable policy snapshot linked to the decision event, not only provider-internal evaluation semantics. |
| Refusal as first-class outcome | Partial | Yes | Medium | AWS emits denials and access errors, but ECS expects structured refusal evidence with explicit reason classes and exportable semantics. |
| Portable evidence export bundle | Weak | Yes | High | AWS has strong internal audit sources, but not a native ECS-style manifest + events + verifier-inputs export contract. |
| Provider-neutral verifier access | Weak | Partial | High | Many AWS proofs still depend on AWS-specific APIs, consoles, or semantics. ECS expects evidence that a third party can validate without provider lock-in. |
| Evidence by construction | Weak | Partial | High | CloudTrail and service logs are powerful, but they are still largely post-hoc audit surfaces. ECS wants execution-path evidence primitives. |
| Chain continuity across decisions | Weak | Yes | Medium | AWS can be transformed into chained evidence, but the chain is not the default unit of proof. |
| Crisis / partition posture | Partial | Partial | High | AWS is strong on availability, but ECS asks a different question: what survives with governance intact under disruption, separation, or sovereignty fracture? |
| Jurisdiction-aware routing with refusal | Weak | Partial | High | AWS has region controls and policy tools, but ECS expects routing/jurisdiction decisions to be explicit, evidenced, and refusable. |
| Portable object/data binding continuity | Weak | Yes | Medium | Tags and service metadata exist, but ECS expects a portable overlay binding model across object classes and providers. |
| AI lineage and inference evidence | Weak | Partial | High | AWS has AI/ML services and logs, but ECS expects explicit model lineage, routing evidence, refusal semantics, and portable proof. |
| Sovereign trust-root posture | Weak | Partial | High | AWS can implement strong controls, but ECS asks about trust-root control, compelled-access posture, and portable proof independent of the provider. |

## Key conclusion
AWS is not weak because it lacks services.
AWS is strong precisely because it has:
- a coherent operator model,
- deep automation,
- wide service breadth,
- mature documentation.

But ECS is asking for something different:
- provider-neutral evidence,
- exportable verifier inputs,
- refusal semantics,
- decision-time policy state,
- sovereignty-oriented crisis posture,
- portable governance attachments.

That is why AWS can simultaneously be:
- the practical benchmark for startup/operator coherence,
and
- insufficient against the full ECS contract.

## The two arguments this enables

### Argument 1: to EU cloud vendors
You do not only need compute, storage, and Kubernetes.
You need a coherent operating model that can compete with AWS on day-to-day buildability.

### Argument 2: to the market more broadly
Even AWS coherence is not enough if the goal is portable sovereignty and runtime proof.

That is the ECS position:
- **service coherence matters**
- **sovereignty proof still requires more than hyperscaler ergonomics**

## Recommended use of this matrix
Use this together with:
- `docs/mappings/aws-core-to-top3-eu-vendors.md`
- `docs/mappings/aws-minimal-subset.md`
- `docs/evidence/export-schema.md`
- `docs/evidence/refusal-semantics.md`
- `docs/domains/sovereignty-assurance.md`

## Practical next step
For each ECS gap marked `High`, define one concrete compensating pattern:
- export wrapper,
- refusal adapter,
- object binding overlay,
- jurisdiction-routing gateway,
- AI lineage emitter.

That turns the gap matrix from critique into implementation work.
