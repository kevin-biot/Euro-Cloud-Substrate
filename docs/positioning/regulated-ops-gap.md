# Regulated Operations Experience Gap — Positioning Note (Draft, Non-Normative)

## Purpose
Document why sovereign cloud architecture designed without regulated operations experience
produces specifications that appear correct under normal conditions but fail under the
conditions they were designed for — and how ECS addresses this gap.

---

## The Gap

Most open infrastructure and sovereign cloud working groups are staffed by engineers
with deep expertise in:
- Hyperscale cloud platforms
- Open-source orchestration (Kubernetes, OpenStack)
- Networking and storage architecture
- Compliance checklists and certification frameworks

What is largely absent is experience **operating infrastructure under regulatory
scrutiny during actual incidents** — the conditions where sovereignty claims are tested.

Regulated operations experience means having been in the room when:
- A regulator demands an audit trail for a decision made 18 months ago
- A court issues a preservation order on infrastructure logs
- A crisis event severs upstream connectivity and the cluster must continue operating
- An insurance underwriter asks for evidence that an AI decision was authorised
- A government authority demands to know who had access to what, when, and under
  what authority — and the answer must be provable, not reconstructed

This experience is common in:
- Telecommunications carriers (BT, Orange, Vodafone — network incident regulatory reporting)
- Payment infrastructure operators (PCI-DSS under investigation, PSD2 audit)
- Aviation operations (DO-178C, incident investigation, flight recorder evidence)
- Healthcare regulated systems (MDR, GDPR Article 9 audit, clinical trial evidence)
- Financial market infrastructure (DORA, MiFID II transaction reporting)

It is uncommon in open infrastructure communities whose primary operational context
is development, testing, and cloud-native deployment.

---

## What This Looks Like in Practice

### Logs vs Evidence
Communities without regulated operations experience conflate logs with evidence.

Logs are:
- Operational records of system activity
- Typically mutable (log rotation, storage limits, provider retention policies)
- Format-specific to the platform that generated them
- Reconstructed after the fact to answer questions that were not anticipated

Evidence is:
- Structured, timestamped, tamper-evident
- Causally linked to the decision or action it documents
- Emitted at execution time as a consequence of the execution path
- Independently verifiable without access to the originating system
- Admissible: interpretable by a regulator, auditor, or court without the originating
  team present to explain it

A regulator asking for evidence of an AI decision does not want a billion log entries.
They want a structured record showing: who authorised the action, under what policy,
with what inputs, producing what output, at what time, with cryptographic integrity.

ECS IALP (Immutable AI Workload Log Primitives) defines exactly this.
Open infrastructure discussions that treat CloudTrail or Kafka logs as sufficient
have not encountered this requirement under adversarial conditions.

### Crisis Resilience
Communities without regulated operations experience design for availability, not continuity.

Availability means: the system is up and reachable.
Continuity means: the system operates correctly, maintains governance integrity,
and produces admissible evidence under conditions of degraded or severed connectivity,
legal injunction, provider suspension, or geopolitical disruption.

The question is not "can my cluster survive a node failure?"
The question is: "on day one of a crisis — cyberattack, grid failure, geopolitical
cut, provider account suspension — can my cluster:
- evaluate authority and policy using locally cached state?
- continue operating without upstream orchestration?
- produce evidence that will be admissible when the incident is investigated?
- degrade deterministically into predefined reduced-capability modes rather than
  behaving unpredictably?"

ECS CRP (Crisis Resilience Profile) defines this posture explicitly.
OpenStack-focused sovereignty discussions that define resilience as HA cluster
configuration have not operated under these conditions.

### Root of Trust
Communities without regulated operations experience accept provider-asserted security.

"Our platform uses AES-256 encryption" is not a sovereignty claim.
The question is: who controls the key?

If the key management infrastructure is operated by a US-headquartered provider,
a US court order reaches the key regardless of:
- Where the workload runs
- What the contract says
- What sovereignty label the deployment carries

The Apple 2016 precedent (FBI v Apple) is the definitive demonstration. Apple's
architecture did not provide a key extraction mechanism. The court order was
unenforceable not because of contract but because of architecture.

Sovereignty at the key level requires:
- HSM under customer or neutral-party physical control
- Key ceremony conducted in-jurisdiction with documented chain of custody
- No provider break-glass access path
- Architecture that makes key extraction technically impossible regardless of
  legal pressure on the provider

---

## What ECS Does About It

ECS was designed with regulated operations experience as a first-class input.
The invariant set reflects requirements that emerge under adversarial conditions,
not just normal operations:

| Regulated ops requirement | ECS response |
|---|---|
| Evidence admissibility | IALP: evidence emitted at execution time, not reconstructed |
| Crisis continuity | CRP: local authority/policy, control-plane independence, deterministic degradation |
| Root of trust sovereignty | Core10-04: authority before execution; `docs/profiles/no-control-profile.md` |
| Audit portability | Core10-10: provider-neutral export; `docs/evidence/export-schema.md` |
| Refusal as valid outcome | Core10-02: fail-closed; IALP-6: refusal log as first-class event |
| Temporal integrity | Core10-06: decision-time state preserved and addressable |

---

## Implication for Working Groups

Sovereign cloud working groups that lack regulated operations participants will
produce specifications that:

- Pass review by infrastructure engineers
- Satisfy checklist-based compliance assessments
- Fail under actual regulatory scrutiny, incident investigation, or crisis conditions

The gap is not malicious. It is a function of who is in the room.

ECS is offered as an architectural reference that encodes regulated operations
requirements as invariants — so that groups without this experience can adopt
the outcomes without having to learn them the hard way.

---

## Related ECS Documents
- `VISION.md` — IALP and CRP definitions
- `crp/README.md` — Crisis Resilience Profile
- `docs/mappings/jurisdictional-fragmentation.md` — copy-paste sovereignty problem
- `docs/evidence/export-schema.md` — portable evidence bundle
- `docs/guides/evidence-vs-logs.md` — evidence vs logs distinction
- `docs/profiles/no-control-profile.md` — no-control posture

---

*This note reflects architectural and operational observations. It does not constitute
legal advice or certification guidance.*
