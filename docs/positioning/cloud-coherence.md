# Cloud Coherence (Draft, Non-Normative)

## Purpose
Define what **cloud coherence** means in the context of ECS and explain why AWS remains the canonical market reference for that property.

This document is intentionally blunt because the repo now needs a stable conceptual anchor for a recurring question:

**Why do startups, SMEs, and engineering teams keep defaulting to AWS even when sovereignty arguments are understood?**

The short answer is:
because coherence wins before governance wins.

## What cloud coherence means
Cloud coherence is the degree to which a cloud provider presents a usable, predictable, and internally consistent operator model across its core services.

A cloud is coherent when:
- identity fits the rest of the platform,
- networking fits the rest of the platform,
- storage fits the rest of the platform,
- logs and metrics fit the rest of the platform,
- certificates and DNS fit the rest of the platform,
- APIs, CLI, and IaC behave as one system rather than unrelated products,
- documentation reduces operator guesswork rather than increasing it.

This is not just “having many services”.
It is the difference between:
- a collection of products,
and
- a cloud that feels like one operating environment.

## Why AWS is the canonical reference
For ECS purposes, AWS should be treated as the canonical benchmark for **cloud coherence**.

Not because AWS is sovereign.
Not because AWS satisfies ECS.
Not because AWS should define Europe’s political or strategic posture.

But because AWS is still the clearest market example of:
- high service breadth,
- deep automation,
- strong terminal-first operator support,
- integrated identity and access semantics,
- mature documentation,
- and a workflow model that is legible to both humans and machines.

That is what makes AWS sticky.

In practice, many teams choose AWS not because they have concluded it is strategically perfect, but because:
- it is easier to ship on,
- easier to automate,
- easier to staff for,
- easier to script,
- easier to recover on,
- and easier to reason about as a whole.

That is coherence.

## Why this matters before sovereignty
Sovereignty discussions often start at the legal or governance layer.
But many teams never even reach that stage in practice.

They first ask:
- can we deploy this quickly,
- can we operate it without heroics,
- can a small team manage it,
- can we trust the docs,
- can our CI, IaC, and agents use it,
- can we avoid stitching five partial products into one working system.

If the answer is no, then the platform loses before sovereignty is even considered.

This is especially true for:
- startups,
- SMEs,
- teams without large platform groups,
- regulated teams under delivery pressure,
- and coding-agent workflows.

So the market sequence is usually:

`coherence first -> governance later`

If European cloud providers do not meet the coherence bar, they will continue to lose the default decision.

## Coherence is necessary but not sufficient
This is where ECS must stay precise.

AWS is the canonical benchmark for cloud coherence.
It is **not** the canonical benchmark for sovereignty.

Why?
Because a cloud can be highly coherent while still falling short on:
- provider-neutral evidence export,
- refusal semantics,
- decision-time policy state,
- portable verifier inputs,
- jurisdiction-aware routing,
- sovereign trust-root posture,
- crisis operation under sovereignty fracture,
- AI lineage and inference proof portability.

That is exactly why the repo now contains two different kinds of comparison:
- AWS as the benchmark for cloud coherence,
- AWS as incomplete against the ECS sovereignty/evidence contract.

Both statements can be true at the same time.

## The ECS position
ECS does not argue that Europe should build a cloud that is awkward but sovereign in theory.
That is not a serious market proposition.

ECS argues for two requirements at once:

1. **AWS-grade cloud coherence**
   - terminal-first usability,
   - coherent service composition,
   - practical deployer ergonomics,
   - operational predictability.

2. **ECS-grade sovereignty and proof**
   - authority before execution,
   - refusal as a first-class outcome,
   - portable evidence bundles,
   - provider-neutral verifier access,
   - portable governance attachment,
   - jurisdiction-aware control and crisis posture.

That is the actual strategic requirement.

Europe does not need:
- sovereignty without usability,
or
- coherence without proof.

It needs both.

## Why the distinction matters
Without this distinction, the debate gets confused in two predictable ways.

### Failure mode 1: coherence is ignored
People say:
- “European providers already have compute, storage, and Kubernetes”

That misses the point.
The issue is not the existence of primitives.
The issue is whether those primitives add up to a coherent cloud operating model.

### Failure mode 2: coherence is mistaken for sovereignty
People say:
- “AWS already works brilliantly, so the problem is solved”

That also misses the point.
Operational coherence is real and valuable.
But it does not by itself solve:
- compelled-access exposure,
- provider-bound evidence,
- portable auditability,
- trust-root control,
- or sovereign routing and refusal semantics.

## A useful way to talk about this
The cleanest framing is:

- **AWS is the canonical reference for cloud coherence.**
- **ECS defines what must exist in addition to coherence.**
- **EU cloud providers need to close the coherence gap without surrendering the sovereignty layer.**

That is the repo’s position.

## Related docs
- `docs/mappings/aws-core-to-top3-eu-vendors.md`
- `docs/mappings/aws-against-ecs-gap-matrix.md`
- `docs/mappings/deployer-utility-top3-eu-vendors.md`
- `docs/mappings/sme-trial-billing-top3-eu-vendors.md`
- `docs/domains/sovereignty-assurance.md`
- `docs/positioning/competition.md`
