# Cross-Jurisdictional Sovereignty Minimum — Normative Extraction (Draft)

**Status:** Draft v0.1
**Purpose:** Normative, not merely descriptive.

---

## 1. The Problem This Document Solves

Every major jurisdiction is independently defining "digital sovereignty."
Each definition uses different terminology, different scoring, different legal instruments.
But underneath the variation, every framework is trying to enforce the same small set
of architectural properties.

This document extracts that minimum common set — the properties that, if a substrate
provides them verifiably, satisfy the sovereignty intent of every geo's framework
simultaneously.

This is not a mapping of one framework to ECS. It is a **normative extraction** across
frameworks, producing a minimum substrate contract that is jurisdiction-agnostic by design.

**The claim:** any cloud substrate that satisfies these N minimum properties satisfies
the sovereignty intent of EU, French IRN, GCC, California, Colorado, and Chinese
frameworks — because these properties are what those frameworks are each trying
to enforce, expressed in their own vocabulary.

---

## 2. Source Frameworks Examined

| Geo | Framework(s) | Primary instrument |
|---|---|---|
| European Union | AI Act, NIS2, DORA, EUCS, EC CSF v1.2.1 | Regulation / certification scheme |
| France | IRN (aDRI), HDS, SecNumCloud | Scoring grid / certification |
| GCC | PDPL variants, SAMA CSF, UAE IA Regulations | National regulation / sector frameworks |
| California (USA) | CCPA/CPRA, SB 1047, AB 2013 | State law / proposed regulation |
| Colorado (USA) | Colorado AI Act (SB 205), CPA | State law |
| China | PIPL, Data Security Law, MLPS 2.0, CAC AI regs | National law / standards |

**Observation:** These frameworks share no common legal basis, no common vocabulary,
and no common enforcement mechanism. Yet when their technical requirements are
extracted and reduced, they converge on the same substrate properties.

---

## 3. Extraction Method

For each framework, the following question was applied to each requirement:

> *What substrate property must be true for this requirement to be satisfiable,
> independent of contractual claims, vendor assertions, or audit opinions?*

This yields an **architectural minimum** — the property the substrate must provide
for the framework's intent to be enforceable. Contractual wrappers, certifications,
and audit opinions are layered above this minimum. The minimum is what makes them
non-trivial.

---

## 4. The Minimum Common Properties

After extraction across all six geos, seven minimum properties emerge.
Every geo's framework requires all seven, named differently.

---

### M1 — Locatable Authority

**What it means:** At every execution decision, there must be an identifiable,
locatable authority — a human, institution, or policy — that permitted the action.
Anonymous or unattributed execution is not permitted.

| Geo | How they name it |
|---|---|
| EU AI Act | Art. 9 risk management, Art. 13 transparency, Art. 14 human oversight |
| EU NIS2 | Art. 20 governance — management body accountability |
| France IRN | RES-1.1 localisation de l'autorité décisionnelle |
| GCC (SAMA CSF) | Governance domain — accountability and ownership |
| California SB 1047 | Developer/deployer accountability obligations |
| Colorado SB 205 | Developer/deployer risk management, impact assessments |
| China PIPL | Art. 51 processor accountability; Art. 58 important processor obligations |

**ECS mapping:** Core10-01 (Authority Before Execution), Core10-04 (Policy & Authority Interface)
**Minimum substrate requirement:** Every execution decision references a declared,
verifiable authority identity. Undeclared authority = refusal.

---

### M2 — Policy at Execution Time

**What it means:** The policy under which an action was taken must be captured
at the moment of execution — not reconstructed afterward. The exact policy,
rubric, and constraint set active at decision time must be addressable.

| Geo | How they name it |
|---|---|
| EU AI Act | Art. 12 record-keeping, Art. 9 risk management system |
| EU DORA | Art. 8 ICT risk management — documented and versioned |
| France IRN | RES-2.1 conformité UE — versioned policy artifacts |
| GCC (UAE IA) | Control documentation and version management |
| California AB 2013 | Training data and policy documentation requirements |
| Colorado SB 205 | Risk management documentation obligations |
| China CAC AI regs | Algorithm transparency and documentation requirements |

**ECS mapping:** Core10-04 (Policy & Authority Interface), IALP-2 (Policy Snapshot Log)
**Minimum substrate requirement:** Policy snapshot captured and addressable per
execution event. Post-hoc policy reconstruction is insufficient.

---

### M3 — Evidence by Construction

**What it means:** Compliance-relevant evidence must be emitted as part of the
execution path itself. It cannot be reconstructed from operational logs after
the fact. The evidence must be tamper-evident and independently verifiable.

| Geo | How they name it |
|---|---|
| EU AI Act | Art. 12 automatic logging for high-risk AI |
| EU NIS2 | Art. 23 incident reporting — structured, timely, evidenced |
| EU DORA | Art. 17 ICT-related incident management — documented evidence |
| France IRN | RES-2.5 contrôle régional SOC/journaux — integrity of evidence |
| GCC (SAMA CSF) | Audit and logging controls — integrity requirements |
| California CCPA | Audit and accountability for data processing |
| China DSL | Art. 27 data security monitoring and incident evidence |

**ECS mapping:** Core10-05 (Evidence Event Model), Core10-06 (Audit Chain), IALP
**Minimum substrate requirement:** Evidence emitted at execution time.
Log-only implementations do not satisfy this property.

---

### M4 — Data Jurisdiction Enforcement

**What it means:** The jurisdiction in which data is stored and processed must be
enforceable at the substrate level — not merely declared in a contract. The
substrate must be capable of refusing operations that would violate declared
jurisdictional constraints.

| Geo | How they name it |
|---|---|
| EU GDPR / AI Act | Data localisation, transfer restrictions (Chapter V GDPR) |
| EU EC CSF | SOV-2 Legal & Jurisdictional, SOV-3 Data & AI |
| France SecNumCloud | Data hosted and processed in France, no extraterritorial exposure |
| GCC PDPL variants | Data residency requirements — country-specific |
| California CCPA | Consumer data rights — state resident data |
| China PIPL | Art. 40 cross-border transfer restrictions; MLPS data classification |

**ECS mapping:** Core10-03 (EOSC Metadata Spec), CRP-4 (Data Residency Enforcement),
`docs/domains/federation.md`
**Minimum substrate requirement:** Jurisdiction metadata travels with data.
Routing decisions are refusable based on jurisdiction policy. Enforcement
is architectural, not contractual.

---

### M5 — Refusal as First-Class Outcome

**What it means:** When a required authority, policy, or jurisdictional constraint
cannot be satisfied, the system must refuse execution and record the refusal as
a valid, evidenced outcome — not an error. Refusal evidence must be as rigorous
as execution evidence.

| Geo | How they name it |
|---|---|
| EU AI Act | Art. 5 prohibited AI practices — non-execution requirement |
| EU NIS2 | Fail-safe controls — non-execution under unacceptable risk |
| France IRN | CRP-7 — explicit refusal semantics |
| GCC (UAE IA) | Mandatory stop conditions for non-compliant processing |
| California SB 1047 | Unsafe capability refusal obligations |
| Colorado SB 205 | High-risk AI — refusal / human review obligations |
| China CAC AI regs | Prohibited content/action non-execution |

**ECS mapping:** Core10-02 (Fail-Closed Semantics), IALP-6 (Refusal & Escalation Log),
CRP-7 (Explicit Refusal Semantics)
**Minimum substrate requirement:** Refusal is a valid execution outcome.
Refusal events are logged with the same rigour as execution events.
Best-effort execution past a compliance boundary is prohibited.

---

### M6 — Crisis Continuity Under Partition

**What it means:** For designated critical workloads, the substrate must continue
operating with governance intact under conditions of degraded or severed
connectivity, legal injunction, or provider unavailability. Continuity is a
governance property, not merely an availability property.

| Geo | How they name it |
|---|---|
| EU NIS2 | Art. 21 business continuity — critical infrastructure |
| EU DORA | Art. 11 ICT business continuity policy |
| France IRN | RES-4.1 autonomie opérationnelle, RES-4.3 continuité face à arrêt forcé |
| GCC (SAMA CSF) | Business continuity and resilience domain |
| California (critical infrastructure) | Implicit in sector-specific continuity requirements |
| China DSL | Art. 21 critical data infrastructure continuity obligations |

**ECS mapping:** CRP (Crisis Resilience Profile) — all seven CRP invariants,
three operational modes (Normal / Partition / Recovery)
**Minimum substrate requirement:** Defined partition mode with local authority
evaluation, local evidence persistence, and deterministic degradation.
Continuity dependent on upstream provider availability is not sufficient
for critical workloads.

---

### M7 — Portable, Provider-Neutral Audit

**What it means:** Audit evidence and compliance artifacts must be exportable
through a standard, provider-neutral interface. Customers must be able to
verify compliance and exercise their rights without requiring provider-specific
tooling, provider cooperation, or provider access.

| Geo | How they name it |
|---|---|
| EU AI Act | Art. 12 log accessibility, Art. 72 market surveillance access |
| EU EC CSF | SOV-4 Operational — portability; SOV-7 Security — independent audit |
| France IRN | RES-6.2 portabilité des workloads, RES-4.3 continuité |
| GCC (SAMA CSF) | Audit rights and third-party access |
| California CCPA | Consumer right to access — enforceable data portability |
| China PIPL | Art. 45 personal information portability rights |

**ECS mapping:** Core10-10 (Portable Audit Surface), `docs/evidence/export-schema.md`,
`docs/evidence/verifier-responsibilities.md`
**Minimum substrate requirement:** Evidence bundle exportable via standard interface
without provider-specific tooling. Verifier can run checks independently.
Provider cannot make audit access contingent on commercial relationship.

---

## 5. The Minimum Common Substrate Contract

A substrate that provides M1–M7 verifiably satisfies the sovereignty intent of
all source frameworks. This is the normative minimum.

| Property | ECS primary mechanism | Verifiable? | Without provider cooperation? |
|---|---|---|---|
| M1 Locatable Authority | Core10-01, Core10-04, IALP-1 | Yes | Yes |
| M2 Policy at Execution Time | Core10-04, IALP-2 | Yes | Yes |
| M3 Evidence by Construction | Core10-05, Core10-06, IALP | Yes | Yes |
| M4 Data Jurisdiction Enforcement | Core10-03, CRP-4 | Yes | Yes |
| M5 Refusal as First-Class Outcome | Core10-02, IALP-6, CRP-7 | Yes | Yes |
| M6 Crisis Continuity Under Partition | CRP (all) | Yes — via declared modes and evidence | Partially (requires local infrastructure) |
| M7 Portable Provider-Neutral Audit | Core10-10, export schema | Yes | Yes |

**Every cell in the "Verifiable without provider cooperation" column must be Yes.**
If any property requires the provider's cooperation to verify, it is not a substrate
property — it is a contractual claim.

---

## 6. What This Enables

### For operators
A single conformance baseline that satisfies multiple regulatory regimes simultaneously.
No per-jurisdiction stack fragmentation. Jurisdiction-aware routing above a common substrate.

### For regulators
A substrate reference that translates their framework's intent into verifiable
architectural properties. Procurement criteria that go beyond contractual assertions.

### For standards bodies
A minimal normative common ground that geo-specific frameworks can reference
without requiring harmonisation of their legal instruments.

### For ECS
M1–M7 are the normative core of ECS. Every Core10 invariant, CRP invariant,
and IALP primitive maps to one or more of these properties.
ECS is the implementation specification. This document is the extraction proof.

---

## 7. What This Does NOT Do

- Does not claim legal equivalence between frameworks.
- Does not eliminate the need for jurisdiction-specific compliance work above the substrate.
- Does not define certification criteria for any specific scheme.
- Does not address commercial, political, or geopolitical sovereignty claims.

The substrate contract is necessary but not sufficient for full compliance
with any specific framework. It is the architectural floor, not the ceiling.

---

## Related ECS Documents
- `VISION.md` — Core10 invariants, CRP, IALP
- `docs/mappings/reg-mapping.md` — EU regulatory mapping
- `docs/mappings/irn-mapping.md` — French IRN crosswalk
- `docs/mappings/ec-cloud-sovereignty-framework-mapping.md` — EC CSF mapping
- `docs/mappings/jurisdictional-fragmentation.md` — fragmentation problem statement
- `crp/README.md` — Crisis Resilience Profile
- `docs/evidence/export-schema.md` — portable evidence bundle

---

*This document is normative in intent and draft in status.
Geo-specific framework citations are indicative and subject to change as
frameworks evolve. Legal interpretation requires qualified counsel per jurisdiction.*
