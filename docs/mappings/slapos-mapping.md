# SlapOS — Reference Implementation Mapping (Draft, Non-Normative)

**Status:** Draft v0.1
**Purpose:** Document SlapOS as a proof-of-existence reference for the ECS sovereign
substrate pattern — not a compliance crosswalk but an architectural validation that
the M1–M7 minimum properties have been implementable in production since 2010.

---

## What SlapOS Is

SlapOS (Service Level Agreement Protocol Operating System) is a general-purpose
distributed cloud operating system developed by Nexedi SA (France), authored
principally by Jean-Paul Smets, first released in 2010, presented at FOSDEM 2013,
and taught annually at Telecom Paris since at least 2017.

It is Free Software under GNU GPL v3.

**Architecture in two components:**

- **SlapOS Master** — installed on at least one node; defines the common state
  shared by all nodes. Backed by ERP5 (open source ERP) for accounting, provisioning,
  billing, and issue tracking. Authority, policy, and allocation are managed here.

- **SlapOS Node** — installed on each node; autonomously converges toward the
  state defined by the Master. If the Master is unreachable, the Node continues
  running its last known state.

**Network fabric:** Re6st — an IPv6 overlay mesh that keeps all nodes connected
regardless of underlying network topology or backbone availability.

**Workload model:** Any POSIX-compatible process, container, or virtual machine
is a workload. VMs (KVM/QEMU), databases, web services, 4G/5G network functions,
edge AI inference — all are first-class SlapOS software instances. The cloud
is not a data centre. It is any collection of registered nodes anywhere.

**Use cases supported natively:**
- Public and private cloud (IaaS, PaaS, SaaS, DRaaS)
- Hyperconverged infrastructure
- Edge computing (CDN, IoT, AI offloading)
- 4G/5G network management
- Resilient low-latency network as a service
- **Tactical cloud bubble** — sovereign, disconnected, self-managing deployment

---

## Why SlapOS Matters to ECS

SlapOS is not a framework to adopt. It is **proof that the sovereign substrate
pattern works and has been working in production for 15 years.**

Every ECS invariant that is sometimes challenged as theoretical or aspirational
has a working implementation in SlapOS. The table below maps them.

---

## Architectural Mapping to ECS Invariants

| ECS invariant / property | SlapOS implementation | Notes |
|---|---|---|
| **M1 — Locatable Authority** | SlapOS Master (ERP5) manages all allocation requests. Every software instance is requested by an identified user or organisation against declared resources. Anonymous allocation is not possible. | Authority is structural — enforced by the Master's allocation engine, not by contract. |
| **M2 — Policy at Execution Time** | Software profiles (Buildout) declare the exact software stack and configuration at instantiation time. Profile versions are immutable references. | Policy snapshot = software release + instance profile at request time. Reproducible. |
| **M3 — Evidence by Construction** | **Promises** — every SlapOS software instance declares named, continuous assertions about its own health state. Promises run continuously and emit structured pass/fail state. Not logs — structured, named, typed assertions. | This is evidence by construction implemented in 2010. Operational state is asserted, not reconstructed. |
| **M4 — Data Jurisdiction Enforcement** | Node registration is under Master control. The operator defines which nodes are admitted to the fabric. Geographic scope of the cloud = geographic scope of admitted nodes. No data centre dependency. | Jurisdiction boundary is wherever you register nodes. Enforced architecturally. |
| **M5 — Refusal as First-Class Outcome** | SlapOS Master refuses allocation requests that cannot be satisfied given current node state, resource availability, or policy constraints. Refusal is a valid allocation outcome, not an error. | Fail-closed allocation by design. |
| **M6 — Crisis Continuity Under Partition** | SlapOS Node runs autonomously. If Master is unreachable, Node continues running last known state. Re6st mesh maintains connectivity across backbone failures. **Tactical cloud bubble** is an explicit deployment mode for disconnected sovereign operation. | CRP-3 (control-plane independence) and CRP-6 (deterministic degradation) implemented in production since 2010. |
| **M7 — Portable Provider-Neutral Audit** | ERP5 backend provides open, exportable accounting, invoicing, and provisioning records. Promises export structured health state. Source code is open and auditable. | Provider-neutral by open-source definition. Audit surface is the open ERP5 instance. |

---

## SlapOS as Evidence Against "It Cannot Be Done"

The most common objection to M1–M7 as a procurement requirement is that
no real system implements all of them simultaneously. SlapOS refutes this.

Specific production deployments:

- **2015:** A government selected SlapOS decentralised cloud to serve 30,000 users.
- **2016:** Institut Mines Télécom deployed TeraLab big data platform on SlapOS.
- **2013:** Nexedi offered to deploy France's sovereign cloud (Cloudwatt programme)
  in 8 days using SlapOS. France chose an OpenStack-based joint venture instead.
  That venture (Cloudwatt, Orange + SFR) cost hundreds of millions of euros
  and was shut down in 2016. SlapOS continues in production.
- **2021:** SlapOS presented as "12 years of Edge Computing" at Open Source
  Innovation Spring, Systematic Paris-Region.
- **Ongoing:** Taught annually at Telecom Paris engineering school.
  Over 200 students trained.

---

## The Cloudwatt Case Study: Institutional Blindness in Practice

In 2013, Nexedi publicly offered to deploy France's sovereign cloud using SlapOS
within 8 days. The French government had already committed to Cloudwatt — a joint
venture between Orange and SFR using OpenStack.

| Dimension | SlapOS (Nexedi) | Cloudwatt (Orange + SFR) |
|---|---|---|
| Origin | French, Nexedi SA | US-originated (OpenStack) |
| Architecture | Master/Node separation, autonomous convergence, Re6st mesh | OpenStack stack, centralised control plane |
| Sovereign continuity | Node continues autonomously under partition | Dependent on control-plane availability |
| Evidence model | Promises — structured, continuous, typed | Logs — mutable, operational, reconstructive |
| Deployment offer | 8 days | Multi-year programme |
| Cost | Open source | Hundreds of millions EUR |
| Outcome | Still in production 2026 | Shut down 2016 |

**The lesson:** The French government's procurement criteria selected for
institutional recognisability (OpenStack community momentum, large industrial
partners) over architectural correctness (sovereign continuity, evidence by
construction, autonomous node operation).

This is the regulated-ops-gap problem in its purest form. The evaluation criteria
did not include: "can this system continue operating with governance intact when
the upstream control plane is unavailable?" If it had, SlapOS would have won.

---

## SlapOS and the Cross-Geo Sovereignty Minimum

SlapOS satisfies M1–M7 (see `docs/mappings/cross-geo-sovereignty-minimum.md`)
without being designed against any specific regulatory framework.

It satisfies them because Jean-Paul Smets designed for the hard operational
problem — how do you run software reliably across heterogeneous, geographically
distributed, partially-connected nodes with accounting, authority, and continuity
intact — and the regulatory frameworks, written years later, are trying to enforce
the same properties.

This is the correct design sequence:

```
Hard operational problem → Architectural solution → Regulatory framework
                                                     names the same properties
```

The incorrect design sequence, repeated across sovereign cloud procurement:

```
Regulatory framework → Contractual wrapper → Existing stack unchanged
```

---

## What ECS Can Learn from SlapOS

### 1. Promises as the Evidence Primitive

SlapOS Promises are the most mature open-source implementation of evidence
by construction in the cloud substrate space. ECS IALP defines the same
property from a regulatory/governance angle. These should be aligned.

A future ECS workstream could define a Promise-compatible evidence interface
as a reference implementation of Core10-05 (Evidence Event Model).

### 2. Autonomous Node Convergence as CRP Reference

SlapOS Node's autonomous convergence toward Master-defined state is the
reference implementation of CRP-3 (Control-Plane Independence) and CRP-6
(Deterministic Degradation). The Master defines the desired state.
The Node converges toward it. If Master is unreachable, the Node holds
last known state deterministically.

ECS CRP should reference this pattern explicitly as a proven implementation model.

### 3. Re6st as Sovereign Network Fabric

Re6st is an IPv6 overlay that maintains mesh connectivity across backbone
failures. For ECS deployments requiring network sovereignty under partition,
Re6st is a production-grade reference implementation of the network continuity
requirement in CRP-4 and CRP-6.

### 4. The Tactical Cloud Bubble

SlapOS explicitly supports "tactical cloud bubble" — a sovereign, disconnected,
self-managing deployment. This is the most extreme CRP scenario: complete
disconnection from upstream infrastructure while maintaining governance and
evidence integrity. SlapOS runs it in production.

---

## Related ECS Documents

- `docs/mappings/cross-geo-sovereignty-minimum.md` — M1–M7 normative extraction
- `docs/mappings/jurisdictional-fragmentation.md` — contractual vs architectural sovereignty
- `docs/positioning/regulated-ops-gap.md` — institutional blindness pattern
- `crp/README.md` — Crisis Resilience Profile
- `VISION.md` — IALP and Core10 invariants

---

## Sources

- SlapOS homepage: https://slapos.nexedi.com
- Nexedi SA: https://www.nexedi.com
- FOSDEM 2013 talk: https://archive.fosdem.org/2013/schedule/event/slapos/
- Cloudwatt offer (French): https://www.nexedi.com/news-SlapOS.For.France
- Government deployment (30,000 users): https://www.nexedi.com/news/P-IMT-Press.Success.Case.Anouncement
- 12 years of Edge Computing (2021): https://www.nexedi.com/NXD-SlapOS.Experience
- Telecom Paris lecture: https://handbook.rapid.space/slapos-Lecture.Telecom.autumn.2022

---

*This mapping is non-normative. SlapOS is cited as architectural reference
and proof of implementability, not as a compliance target or certification scheme.*
