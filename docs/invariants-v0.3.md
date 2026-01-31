# Core Invariants (v0.3 Draft Taxonomy)

Draft classification of ECS invariants. This is non-normative until merged into the next spec revision.

## 1. Authority Invariants (AUTH)
- **AUTH-01 — Local Authority Satisfiability:** All authority decisions required for execution MUST be satisfiable locally using cached or locally authoritative data.
- **AUTH-02 — No Hard Upstream Authority Dependency:** Execution MUST NOT depend on real-time availability of upstream identity, policy, or authorization services.
- **AUTH-03 — Authority Plane Separation:** Loss of central orchestration or management services MUST NOT immediately prevent continued execution of already-authorised workloads.
- **AUTH-04 — Explicit Authority Refusal:** If authority validity cannot be established locally, the system MUST refuse execution rather than infer or approximate.
- **AUTH-05 — Authority Boundary Declaration:** Each ECS deployment MUST declare its authority boundary (jurisdictional, organizational, cryptographic).

## 2. Policy Invariants (POL)
- **POL-01 — Policy as Versioned Artifact:** All enforceable policies MUST exist as versioned, immutable artifacts with provenance.
- **POL-02 — Deterministic Policy Evaluation:** Given identical inputs, policy evaluation MUST produce identical outcomes.
- **POL-03 — Complete Enforcement Coverage:** All execution paths MUST pass through at least one declared policy enforcement point.
- **POL-04 — Fail-Closed on Policy Uncertainty:** If policy validity or applicability cannot be determined, execution MUST fail closed.
- **POL-05 — Last-Known-Good Policy Fallback:** Where continuity is permitted, the system MAY operate using the last validated policy snapshot, with evidence.

## 3. Execution Invariants (EXEC)
- **EXEC-01 — Execution Envelope Declaration:** Every workload MUST conform to a declared execution envelope profile.
- **EXEC-02 — No Undeclared Runtime Dependencies:** Workloads MUST NOT invoke runtime dependencies that are not explicitly declared in their envelope.
- **EXEC-03 — Control-Plane Independence:** Loss of upstream scheduling, orchestration, or vendor control planes MUST NOT immediately halt execution.
- **EXEC-04 — Deterministic Degradation Modes:** Under degraded conditions, the system MUST enter predefined reduced-capability modes.
- **EXEC-05 — Execution Behaviour Auditability:** Execution state transitions MUST be observable and reconstructible from evidence.

## 4. Data Invariants (DATA)
- **DATA-01 — Data Residency Enforceability:** Data MUST NOT be stored or processed outside its declared residency boundary.
- **DATA-02 — Data Class Declaration:** All data MUST be classified according to sensitivity and regulatory impact.
- **DATA-03 — Cryptographic Authority Control:** Encryption keys controlling protected data MUST be under declared authority control.
- **DATA-04 — Data Lineage Traceability:** The origin, transformation, and movement of data MUST be traceable.
- **DATA-05 — Enforceable Erasure and Export:** Data MUST be erasable and exportable within declared time and scope bounds.

## 5. Evidence Invariants (EVID)
- **EVID-01 — Evidence as First-Class Output:** Security, compliance, and control events MUST produce evidence events by default.
- **EVID-02 — Local Evidence Persistence:** Evidence MUST be recorded durably locally, including during network partition.
- **EVID-03 — Evidence Integrity Guarantees:** Evidence MUST be tamper-evident and integrity-verifiable.
- **EVID-04 — Evidence Completeness Baseline:** A minimum required evidence set MUST be defined per invariant family.
- **EVID-05 — Deferred Evidence Synchronisation:** Evidence MUST be synchronisable once connectivity is restored.

## 6. Interoperability Invariants (INT)
- **INT-01 — Standardised Interface Exposure:** Critical interfaces MUST use documented, open or standardised formats where available.
- **INT-02 — No Proprietary Critical-Path Extensions:** Proprietary extensions MUST NOT exist on declared critical paths.
- **INT-03 — Interop Profile Declaration:** Each ECS component MUST declare the interoperability profile it conforms to.

## 7. Portability & Exit Invariants (EXIT)
- **EXIT-01 — Exit Path Declaration:** Each critical workload MUST declare an exit path or an alternative steady-state architecture.
- **EXIT-02 — Bounded Exit Feasibility:** Exit MUST have measurable time, cost, and dependency bounds.
- **EXIT-03 — Executed Exit Validation:** Exit or migration MUST be exercised periodically, producing evidence.
- **EXIT-04 — Irreversibility Compensation:** Where direct portability is impossible, architectural compensation MUST be explicit and validated.

## 8. Dependency Invariants (DEP)
- **DEP-01 — Critical Path Identification:** All critical services MUST identify their critical dependency paths.
- **DEP-02 — Non-Substitutable Dependency Declaration:** Any non-substitutable dependency MUST be explicitly declared.
- **DEP-03 — Exclusivity Constraint:** A single actor MUST NOT control a non-substitutable critical path unless formally accepted and compensated.
- **DEP-04 — Dependency Evidence Exposure:** Dependency structure MUST be observable and auditable.

## 9. Supply-Chain Invariants (SUP)
- **SUP-01 — Software Bill of Materials Availability:** All software artifacts MUST have a declared SBOM.
- **SUP-02 — Build Provenance Verifiability:** Artifact origin and build process MUST be verifiable.
- **SUP-03 — Upstream Dependency Disclosure:** Critical upstream dependencies MUST be declared, including support location.
- **SUP-04 — Unknown Supply Chain Fails Conformance:** Undeclared or opaque dependencies MUST fail conformance.

## 10. Human & Operations Invariants (OPS)
- **OPS-01 — Operational Runbook Availability:** All critical services MUST have documented runbooks.
- **OPS-02 — Role Redundancy:** No critical operation MAY depend on a single named role or individual.
- **OPS-03 — Operator Access Independence:** Administrative access MUST NOT be exclusively controlled by a vendor.
- **OPS-04 — Operational Capability Evidence:** Operational readiness MUST be evidenced (drills, incidents, metrics).

## 11. Physical Connectivity Invariants (PHY)
- **PHY-01 — Connectivity Dependency Declaration:** Network and telecom dependencies MUST be explicitly declared.
- **PHY-02 — Single-Path Detection:** Single-operator or single-path connectivity MUST be detectable.
- **PHY-03 — Partition Scenario Consideration:** Declared partition scenarios MUST exist for critical services.

---

## Mapping to existing specs (initial)
- AUTH/POL/EXEC: WS1 (OLZ-EU), WS3 (Execution Envelopes), CRP; Policy & Authority Interface.
- DATA/EVID: WS2 (EOSC), WS5 (Evidence & Audit), IALP.
- INT/EXIT: WS4 (Interop APIs), WS6 (Migration & Portability).
- DEP/SUP/OPS/PHY: Governance, CRP, and cross-cutting operational requirements (to be integrated).

## Notes
- This is a draft; alignment with v0.2 Core 10/CRP invariants will occur in the next revision.
- Use this taxonomy to classify gaps and future conformance tests.
