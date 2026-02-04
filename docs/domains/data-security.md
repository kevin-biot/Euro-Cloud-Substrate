# Data Security Domain (Draft, Non‑Normative)

## Purpose
Define the Data Security domain across the cloud‑edge continuum, focusing on **confidentiality, integrity, and auditability** without prescribing a specific encryption stack.

## Capabilities (baseline)
- **End‑to‑end encryption (E2EE)**
- **At‑rest encryption**
- **In‑transit encryption**
- **In‑use protection** (confidential compute / TEEs)
- **Data loss prevention (DLP)** controls
- **Key management systems (KMS)** and custody models
- **Post‑quantum (PQ) readiness** (algorithm/profile declarations)

## ECS mapping (no new semantics)
- **Core10‑03 EOSC** — governance metadata for storage; evidence export for data handling.
- **DATA invariants** — residency, classification, export/erasure evidence.
- **EVID invariants** — evidence emission, integrity, and exportability.
- **Evidence catalog** — event shapes for encryption posture, key custody, and DLP decisions.

## Evidence expectations (security‑grade)
- **Encryption posture declarations** (at‑rest / in‑transit / in‑use) bound to policy snapshots.
- **Key custody evidence** (who controls keys, where keys live, break‑glass model).
- **DLP decisions** (allow/refuse with reasons + evidence pointers).
- **PQ readiness declarations** (supported profiles/algorithms, no mandate yet).

## Notes
ECS defines **the evidence contract**, not the cryptographic implementation. Providers may compete above the base as long as the evidence is portable and verifiable.
