# ECS Architecture Overview (Draft)

**Status:** draft, non‑normative

## Purpose
Euro Cloud Substrate (ECS) defines a **contract layer** for a portable, governable European cloud substrate. It is **not** a platform product. It specifies the minimum architectural contracts and evidence requirements that enable portability, auditability, and sovereignty across providers and implementations.

ECS focuses on:
- **Authority and policy before execution**
- **Evidence‑by‑construction** (events, chains, export bundles)
- **Interop + migration with verifiable proofs**
- **Profiles** for context‑specific requirements (baseline, admissible, NCP, regulated‑ML)

## Scope (what ECS covers)
- Governance primitives: authority binding, policy snapshots, fail‑closed posture
- Evidence primitives: canonical events, audit chains, export bundles, verifier inputs
- Portability primitives: interop APIs and migration baseline with evidence
- Execution envelopes: container/VM classes with admission and evidence hooks
- Data governance: residency, classification, lineage, usage receipts

## Non‑goals (what ECS does *not* do)
- No mandated cloud platform or vendor stack
- No prescribed encryption algorithm or KMS vendor
- No centralized “federation broker” product
- No certification program or compliance scoring

---

## Architecture Model

### Planes (A–E)
ECS organizes system responsibilities into planes. This is an **architectural decomposition**, not a product taxonomy:

- **Plane A — Identity, Tenancy, Authority**
  - Who can act, under what authority
- **Plane B — Control Plane & Landing Zone**
  - Admission, policy enforcement, fail‑closed defaults
- **Plane C — Execution Envelopes**
  - Container or VM envelopes with explicit boundaries
- **Plane D — Data & Evidence Substrate**
  - Governance metadata + evidence chains
- **Plane E — Interop & Portability**
  - Versioned APIs + export/import validation

See `architecture/overview.md` for plane diagrams.

### Control & Evidence Flow (core loop)
1. **Authority binding** is checked (Plane A)
2. **Policy snapshot** is evaluated (Plane B)
3. **Admission** permits or refuses (Plane B)
4. **Execution** proceeds only on allow (Plane C)
5. **Evidence event** is emitted for every decision (Plane D)
6. **Export bundles** enable portability and verification (Plane E)

Fail‑closed behavior is required for governed actions if authority or policy is missing or invalid.

---

## Core10 Components (contract anchors)
ECS is built around ten mandatory components (“Core10”). Each is a contract surface, not an implementation:

1. **Open Landing Zone (Core10‑01)** — authority + policy binding at onboarding
2. **Tenant Isolation (Core10‑02)** — isolation boundaries with refusal evidence
3. **EOSC Object Storage (Core10‑03)** — governance metadata + evidence pointers
4. **Policy & Authority Interface (Core10‑04)** — decision events + refusal semantics
5. **Evidence Event Model (Core10‑05)** — canonical envelope + outcomes
6. **Audit Chain Baseline (Core10‑06)** — hash‑linked evidence + export
7. **Execution Envelopes (Core10‑07)** — container/VM profiles + admission evidence
8. **Interop API Surface (Core10‑08)** — versioned APIs, audit queries
9. **Fail‑Closed Profile (Core10‑09)** — deny on uncertainty with evidence
10. **Migration Baseline (Core10‑10)** — export/import with validation and evidence

---

## Evidence Architecture (ECS’s core differentiator)

### Canonical Envelope
All evidence events conform to Core10‑05. Events are **decision artifacts**, not logs.

### Evidence Profiles
Profiles define **what is required** for a given context:
- `ecs-evidence-baseline`
- `ecs-evidence-admissible`
- `ecs-evidence-ncp`
- `ecs-evidence-regulated-ml`

Profiles constrain required fields, chain requirements, hash profiles, and verifier checks. See `docs/profiles/evidence-profiles.md`.

### Evidence Bundles
A bundle is the **portable unit of audit**:
- manifest (with `evidence_profile_id`)
- event range (`events.jsonl`)
- chain segment
- verifier inputs
- referenced artifacts

See `docs/evidence/export-schema.md` and `docs/examples/evidence-bundles/`.

### Verifier Inputs
A third‑party verifier must be able to validate:
- chain continuity
- pointer integrity
- profile compliance
- artifact immutability

See `docs/evidence/verifier-responsibilities.md`.

---

## Federation & Portability

ECS treats federation as a **contract surface**, not a broker product.

### Federation Roles (ICRA → ECS)
- **Federation Manager** → interop + migration control plane (WS4/WS6)
- **Federation Broker** → discovery + profile claims + bundle examples

See `docs/domains/federation.md` and `docs/mappings/ipcei-cis-mapping.md`.

### Interop & Migration
- **WS4** defines minimal APIs for tenant/workload/storage/audit
- **WS6** defines export/import and validation
- Refusal evidence is mandatory when federation actions are denied

---

## Data, AI, and Privacy Governance

### Data Governance (EOSC)
- Governance metadata travels with data
- Residency/classification evidence is exportable

### Regulated ML
- ML evidence events require `hash_profile_id`
- Model lineage and training evidence are first‑class artifacts

### Privacy & User Control
- Consent and purpose binding are decision events
- Minimization evidence is required when applicable

See `docs/domains/privacy.md`, `docs/domains/data-security.md`, and `docs/guides/ml-evidence-implementation.md`.

---

## Archetype Stack View (Vendor‑neutral)
ECS enables multiple archetypes without a mandated stack:

| Archetype | Stack emphasis | ECS focus |
|---|---|---|
| OpenShift‑like | Orchestration + Platform + Virtualization | OLZ‑EU + admission evidence + envelopes |
| VM‑first | Virtualization + Network + Physical | VM envelope + data export + evidence |
| Managed platform | App + Orchestration + Data/AI | Interop APIs + evidence profiles |

See `architecture/overview.md` for a compact view.

---

## Adoption Path (engineers + procurement)

1. **Golden bundles** — `docs/examples/evidence-bundles/`
2. **Reference adapter** — `adapters/k8s-admission/`
3. **Demo flow** — `docs/examples/demo-flow.md`
4. **RFP guide** — `docs/procurement/rfp-guide.md`

This is the recommended “close the loop” path for first adopters.

---

## External Alignment

- **IRN**: ECS provides the “how” controls for IRN’s “what.” See `docs/mappings/irn-mapping.md`.
- **IPCEI‑CIS**: ECS supplies contract‑level evidence for ICRA’s conceptual layers. See `docs/mappings/ipcei-cis-mapping.md`.
- **EU regulations**: ECS maps to GDPR/NIS2/DORA/AI Act through evidence primitives. See `docs/mappings/reg-mapping.md`.

---

## Conformance & Claims
Conformance is **evidence‑driven**, not certification.

A vendor claims support by publishing:
- supported evidence profiles
- default profile
- hash profiles
- export endpoints
- verifier inputs supported

See `docs/conformance/model.md` for the claims template.

---

## Roadmap (near‑term)
- Expand interop API skeletons with real endpoints
- Add a second adapter (object storage or ML inference)
- Build a minimal verifier CLI for bundle validation
- Pilot procurement with profile‑based acceptance checks
