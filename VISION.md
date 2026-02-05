# Euro Cloud Substrate (ECS)
Architecture Definition v0.2

- **Status:** Draft v0.2 (Architecture + Invariants)
- **Scope:** Architectural definition only. No vendor selection. No geopolitics. No implementation mandates.

---

## 1. Purpose of v0.2

This revision adds three concrete elements requested by early reviewers:
1. A single conceptual architecture diagram (described textually) that anchors discussion.
2. The first cut of Core 10 Invariants, written as enforceable MUST/SHALL statements.
3. A fundability and consortium rationale aligned with EU industrial and digital infrastructure programmes.

This document remains intentionally non-implementational. Its goal is to define the execution contract that enables interoperability, portability, and governance-by-design across European cloud providers.

ECS standardizes **verifiable governance and portability**, not the commercial layer. Conformance is a minimum contract; providers still compete on performance, managed services, UX, pricing, and regional specialization.

If ECS gains traction, a **separate Cloud API standard** could define common service interfaces.  
ECS would remain the **contract layer**, while the API standard defines the **interface layer**; vendors compete above both.

For regulatory context and how ECS primitives map to EU obligations, see `docs/mappings/reg-mapping.md`. For the French IRN “what” versus ECS “how” crosswalk, see `docs/mappings/irn-mapping.md`.

### External context (aDRI)
aDRI is a non-profit organization founded to promote technological independence and digital sovereignty for European companies. Its mission is to provide free, transparent, and scientifically rigorous assessment tools to help organizations identify their vulnerabilities and regain control over their digital infrastructure.

Website: https://thedigitalresilience.org

---

## 2. Conceptual Architecture (Textual Diagram)

The ECS architecture is composed of four planes, with explicit data and control flows. The planes are layered but not hierarchical; governance signals flow before execution.

```
┌──────────────────────────────────────────────────────────────┐
│                     Plane A: Authority & Identity             │
│  - Tenant / Org / Project identity                             │
│  - Human & institutional authority binding                     │
│  - Explicit decision rights                                    │
└───────────────▲───────────────────────────▲──────────────────┘
                │                           │
                │ Authority check           │ Ownership
                │ (pre-execution)           │ attribution
                │                           │
┌───────────────┴───────────────────────────┴──────────────────┐
│                   Plane B: Control Plane / Landing Zone        │
│  - Network & egress baseline                                   │
│  - Policy enforcement & refusal semantics                      │
│  - Audit & evidence event emission                             │
│  - Deterministic routing                                       │
└───────────────▲───────────────────────────▲──────────────────┘
                │                           │
                │ Route / refuse            │ Evidence events
                │                           │
┌───────────────┴───────────────────────────┴──────────────────┐
│                   Plane C: Execution Envelopes                 │
│  - Kubernetes workload envelope                                │
│  - VM-class envelope (regulated / long-lived)                  │
│  - Explicit lifecycle boundaries                               │
└───────────────▲───────────────────────────▲──────────────────┘
                │                           │
                │ Read/write data           │ Integrity hashes
                │                           │
┌───────────────┴───────────────────────────┴──────────────────┐
│                   Plane D: Data & Evidence Substrate          │
│  - Object storage (S3-like surface)                           │
│  - Governance metadata (jurisdiction, retention, integrity)   │
│  - Immutable evidence chains                                  │
└──────────────────────────────────────────────────────────────┘
```

**Key architectural principle:** Execution cannot occur unless authority and policy evaluation in Plane A/B succeeds. Evidence is produced as a consequence of execution, not reconstructed later.

---

## 3. Core 10 Invariants (Draft)

These invariants define the minimum properties an ECS-compliant platform MUST provide. They are technology-neutral and testable.

**Invariant 1 — Authority Before Execution**  
The system MUST verify explicit human or institutional authority before executing any non-trivial action. If authority cannot be established, the system MUST refuse to act.

**Invariant 2 — Fail-Closed Semantics**  
All compliance-critical execution paths MUST fail closed. Best-effort execution is prohibited for regulated or safety-impacting workloads.

**Invariant 3 — Deterministic Routing**  
Execution routing decisions MUST be deterministic given the same policy snapshot and inputs. This enables replay, audit, and legal defensibility.

**Invariant 4 — Evidence by Construction**  
Compliance-relevant evidence MUST be emitted as part of the execution path itself. Post-hoc reconstruction from logs alone is insufficient.

**Invariant 5 — Explicit Ownership**  
Every governed workload MUST have a named accountable owner. Anonymous or unowned execution is not permitted.

**Invariant 6 — Temporal Integrity**  
Decision-time state MUST be preserved and addressable. The system MUST be able to show what policies, data, and authority were in force at the moment of execution.

**Invariant 7 — Execution Envelope Clarity**  
Workloads MUST declare their required execution envelope (container or VM). Envelope selection is a governance decision, not an optimisation.

**Invariant 8 — Data Governance Metadata**  
All governed data objects MUST carry jurisdiction, retention, and integrity metadata. This metadata MUST travel with the object across providers.

**Invariant 9 — Escalation as First-Class**  
Escalation to human or institutional authority MUST be a first-class execution outcome. Escalation is not an error; it is a valid state.

**Invariant 10 — Portable Audit Surface**  
Audit and evidence access MUST be exposed through a standard, provider-neutral interface. Customers MUST be able to export evidence without provider-specific tooling.

---

## 4. Mandatory Substrate Components (v0.2 Recap)

ECS v1.0 will specify at minimum:
1. Open Landing Zone (OLZ-EU)
2. Tenant Isolation Contract
3. Euro Object Storage Contract (EOSC)
4. Policy & Authority Interface
5. Evidence Event Model
6. Audit Chain Baseline
7. Execution Envelope Profiles
8. Interoperability API Surface
9. Compliance Fail-Closed Profile
10. Migration Baseline

Each component will be defined by:
- Required invariants
- Observable behaviours
- Conformance test criteria

---

## 5. Fundability & Consortium Rationale

### 5.1 Why this is fundable
ECS directly addresses recognised European gaps:
- Strategic dependency reduction without vendor bans
- SME and regional provider competitiveness
- Regulated-sector cloud adoption (finance, health, energy)
- Insurability and audit readiness for autonomous systems

Unlike prior initiatives, ECS is execution-focused, not policy-only.

### 5.2 Why consortia work here
- No single provider can define the substrate credibly
- Architecture definition benefits from diversity
- Providers can compete above the substrate
- Regulators gain a concrete reference model

### 5.3 Alignment signals (non-exhaustive)
- EU Digital Decade objectives
- NIS2 / DORA execution expectations
- Sovereign cloud and data space initiatives
- Industrial cloud programmes

---

## 6. Contribution Model (Phase 1)

We invite contributors to claim a workstream:
- WS1: Open Landing Zone
- WS2: Object Storage Contract
- WS3: Execution Envelopes
- WS4: Interop APIs
- WS5: Evidence & Audit Plane
- WS6: Migration & Portability

Each workstream delivers:
- A draft specification
- A set of invariants
- A conformance outline
- Reference diagrams

---

## 7. What Happens Next

Immediate next steps:
1. Publish v0.2
2. Open public repo and issue tracker
3. Recruit 6–8 senior European architects as workstream leads
4. Begin Phase 1 architecture drafting

This project succeeds by staying architectural, minimal, and enforceable.

---

## 8. Crisis Resilience Profile (CRP)

### 8.1 Purpose
The Crisis Resilience Profile (CRP) defines a mandatory execution posture for critical workloads that must continue operating under conditions of degraded or severed connectivity, geopolitical disruption, or upstream control-plane unavailability.

CRP is not an optimisation profile. It is a continuity and survivability profile designed for sectors where service interruption has unacceptable social, economic, or safety consequences.

### 8.2 Threat Model Assumptions
CRP explicitly assumes the following conditions may occur without warning:
- Partial or total loss of upstream network connectivity
- Loss of access to global control planes or identity providers
- Jurisdictional blocking or legal injunctions affecting cross-border traffic
- Sanctions, counter-sanctions, or politically induced service restrictions
- Cloud account suspension, credential revocation, or provider unavailability
- Physical infrastructure outages affecting backbone networks

CRP does not assume malicious behaviour by the execution substrate itself. It assumes coordination failure.

### 8.3 Core Crisis Invariants
For workloads designated as CRP-compliant, the following invariants apply in addition to the Core 10:

- **CRP-1 — Local Authority Continuity:** Authority verification MUST be satisfiable using locally cached or locally authoritative identity and policy data. Execution MUST NOT depend on real-time upstream validation.
- **CRP-2 — Local Policy Evaluation:** Policy and rubric evaluation MUST be executable locally using the last valid policy snapshot. If policy validity cannot be established, the system MUST fail closed.
- **CRP-3 — Control-Plane Independence:** Execution MUST continue in the absence of upstream orchestration or scheduling services. Central control-plane availability MUST NOT be a hard dependency.
- **CRP-4 — Data Residency Enforcement:** All data required for continued operation MUST remain within the local jurisdictional boundary. Cross-border replication MAY occur only when connectivity and policy allow.
- **CRP-5 — Evidence Persistence Under Partition:** Evidence events MUST be recorded locally and durably during connectivity loss and MUST be synchronisable once connectivity is restored.
- **CRP-6 — Deterministic Degradation:** Under degraded conditions, the system MUST enter predefined reduced-capability modes. Behaviour under degradation MUST be deterministic and auditable.
- **CRP-7 — Explicit Refusal Semantics:** If a required authority, policy, or data dependency cannot be satisfied locally, the system MUST refuse execution rather than attempt inference or approximation.

### 8.4 Execution Envelope Requirements
CRP workloads MUST declare an execution envelope that supports:
- Local lifecycle management
- Persistent state across restarts
- Isolation from upstream control-plane failures

VM-class envelopes or federated service-oriented execution backplanes (e.g., non-centralised schedulers) are RECOMMENDED for CRP workloads.

### 8.5 Operational Modes
CRP defines three operational modes:
- Normal Mode — Full connectivity; global coordination permitted.
- Partition Mode — Limited or no upstream connectivity; local execution only.
- Recovery Mode — Connectivity restored; evidence reconciliation and state validation.

Transitions between modes MUST be logged as first-class evidence events.

### 8.6 Sector Examples (Non-Exhaustive)
CRP is intended for workloads including but not limited to:
- Healthcare delivery systems
- Energy grid operations
- Emergency services coordination
- Payment clearing and settlement
- Telecommunications core services
- Public-sector service delivery

### 8.7 Relationship to Edge Computing
CRP formalises edge execution as a continuity requirement, not a latency optimisation.

The “edge” is defined as the last point at which lawful authority, operational control, and accountability remain intact. CRP ensures that this point can continue to function autonomously until coordination is restored.

See `docs/architecture/crp.md` for a diagram of CRP operational modes.

---

## 9. Immutable AI Workload Log Primitives (IALP)

### 9.1 Rationale
Current hyperscale cloud platforms provide extensive operational logging, but they do not provide immutable, execution-grade AI workload logs suitable for regulatory evidence, insurance underwriting, or court scrutiny. Operational logs are mutable, incomplete, or reconstructive.

For AI systems that execute decisions with real-world impact, logging must be a first-class execution primitive, not an afterthought.

IALP defines a mandatory set of immutable logging primitives that enable pre-hoc governed AI systems to meet insurability, regulatory, and liability requirements.

### 9.2 Scope of IALP
IALP applies to:
- Agentic workloads
- Automated decision systems
- AI-assisted execution pipelines
- Any workload where AI output can trigger state change, financial impact, or safety consequence

### 9.3 Required Log Primitives
ECS-compliant platforms MUST provide the following immutable log primitives:

- **IALP-1 — Authority Assertion Log:** Records the identity, role, and scope of authority under which execution is permitted.
- **IALP-2 — Policy Snapshot Log:** Records the exact policy, rubric, and constraint set active at execution time.
- **IALP-3 — Input & Context Hash Log:** Records cryptographic hashes of inputs and contextual data used for decision-making, without requiring full data duplication.
- **IALP-4 — Execution Decision Log:** Records whether execution was permitted, refused, or escalated, including rationale codes.
- **IALP-5 — Output Commitment Log:** Records any state change, action, or external effect resulting from execution.
- **IALP-6 — Refusal & Escalation Log:** Records explicit refusals and escalations as valid outcomes, not errors.
- **IALP-7 — Temporal Ordering Log:** Provides monotonic, tamper-evident ordering of all execution events.

### 9.4 Immutability Requirements
- Logs MUST be append-only.
- Logs MUST be cryptographically integrity-protected.
- Logs MUST be locally persistent under partition.
- Logs MUST be exportable via a standard, provider-neutral interface.

### 9.5 Relationship to Hyperscaler Services
IALP is explicitly orthogonal to hyperscaler logging services (e.g., CloudTrail, CloudWatch, Bedrock traces). These services MAY be used as inputs but are insufficient on their own.

Hyperscaler platforms may disclaim liability. ECS ensures customers can meet regulatory and insurance approval independently of provider disclaimers.

### 9.6 Regulatory and Insurance Alignment
IALP enables:
- Demonstrable decision-time accountability
- Evidence-grade audit trails
- Clear attribution of authority and intent
- Insurability of AI-driven workloads
- Reduced ambiguity in regulatory review

IALP transforms logging from observability into legal evidence infrastructure.

See `docs/architecture/ialp.md` for a diagram of IALP flows.

---

## 10. Closing Statement

Europe does not need another hyperscaler. It needs a shared execution substrate that providers can adopt and customers can trust — even when coordination fails and liability is tested.

The Euro Cloud Substrate, with its Crisis Resilience Profile and Immutable AI Workload Log Primitives, defines continuity, accountability, and evidence as design properties, not operational hopes.

---

### Regulatory drivers (context)
ECS is designed to make compliance feasible across evolving EU requirements (e.g., AI Act traceability and refusal semantics, NIS2/DORA resilience and evidence, PSD3 strong authority/authentication) by providing enforceable primitives: authority-before-execution, fail-closed posture, evidence-by-construction (IALP), isolation and data governance, and CRP for continuity under partition. ECS does not encode specific regulations; it provides the substrate controls and evidence needed to satisfy them across providers.

---

## Appendix — Proposed License (ECS Specification License)

Recommended license: Apache License 2.0 with an Architectural Integrity Addendum

### Rationale
- Apache 2.0 is widely accepted, EU-safe, business-friendly, and compatible with open standards.
- It allows implementation, commercial use, and redistribution.
- It provides patent protection.
- The addendum protects against spec capture and misrepresentation, not usage.

Below is the proposed LICENSE file content.
