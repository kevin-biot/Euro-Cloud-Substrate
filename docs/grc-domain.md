# GRC Domain (Draft, Non‑Normative)

## Purpose
Define Governance, Risk & Compliance (GRC) expectations across the cloud‑edge continuum, focusing on **policy governance, auditability, and evidence portability** without prescribing a specific GRC toolchain.

## Capabilities (baseline)
- **Security policy management** (policy snapshots, versioning, approvals)
- **Risk assessments** (registered, time‑bound, auditable)
- **Compliance mapping** (ISO/NIST/GDPR/sectoral requirements)
- **Audit logging & forensic readiness** (immutable logs, retention, integrity proofs)

## ECS mapping (no new semantics)
- **Core10‑04 Policy & Authority** — policy snapshot binding, decision evidence.
- **Core10‑05 Evidence Event Model** — canonical evidence envelope.
- **Core10‑06 Audit Chain Baseline** — tamper‑evident chains + export.
- **Core10‑09 Fail‑Closed Profile** — refusal evidence on missing/invalid policy.
- **Conformance model + evidence profiles** — profile claims, verifier checks.
- **Regulatory mapping** — `docs/reg-mapping.md`, `docs/compliance-pattern-library.md`.

## Evidence expectations (GRC‑grade)
- **Policy snapshots**: versioned, immutable, referenced in decisions.
- **Risk assessment artifacts**: recorded, time‑bounded, linked to decisions.
- **Audit chain**: hash‑linked events with exportable bundles.
- **Forensic readiness**: retention + integrity proofs and exportability.

## Notes
ECS defines **the evidence contract**, not the governance process or audit tooling. Partners may implement different GRC stacks as long as the required evidence is portable and verifiable.
