# Core Invariants (v0.3 Draft, Authoritative List)

Status values: `defined` | `placeholder` | `planned`

## Authority (AUTH)
- AUTH-01 Local Authority Satisfiability — defined
- AUTH-02 No Hard Upstream Authority Dependency — defined
- AUTH-03 Authority Plane Separation — defined
- AUTH-04 Explicit Authority Refusal — defined
- AUTH-05 Authority Boundary Declaration — defined

## Policy (POL)
- POL-01 Policy as Versioned Artifact — defined
- POL-02 Deterministic Policy Evaluation — defined
- POL-03 Complete Enforcement Coverage — defined
- POL-04 Fail-Closed on Policy Uncertainty — defined
- POL-05 Last-Known-Good Policy Fallback — defined

## Execution (EXEC)
- EXEC-01 Execution Envelope Declaration — defined
- EXEC-02 No Undeclared Runtime Dependencies — defined
- EXEC-03 Control-Plane Independence — defined
- EXEC-04 Deterministic Degradation Modes — defined
- EXEC-05 Execution Behaviour Auditability — defined

## Data (DATA)
- DATA-01 Data Residency Enforceability — defined
- DATA-02 Data Class Declaration — defined
- DATA-03 Cryptographic Authority Control — defined
- DATA-04 Data Lineage Traceability — defined
- DATA-05 Enforceable Erasure and Export — defined

## Evidence (EVID)
- EVID-01 Evidence as First-Class Output — defined
- EVID-02 Local Evidence Persistence — defined
- EVID-03 Evidence Integrity Guarantees — defined
- EVID-04 Evidence Completeness Baseline — defined
- EVID-05 Deferred Evidence Synchronisation — defined

## Interoperability (INT)
- INT-01 Standardised Interface Exposure — defined
- INT-02 No Proprietary Critical-Path Extensions — defined
- INT-03 Interop Profile Declaration — defined

## Portability & Exit (EXIT)
- EXIT-01 Exit Path Declaration — defined
- EXIT-02 Bounded Exit Feasibility — defined
- EXIT-03 Executed Exit Validation — defined
- EXIT-04 Irreversibility Compensation — defined

## Dependency (DEP)
- DEP-01 Critical Path Identification — defined
- DEP-02 Non-Substitutable Dependency Declaration — defined
- DEP-03 Exclusivity Constraint — defined
- DEP-04 Dependency Evidence Exposure — defined

## Supply Chain (SUP)
- SUP-01 Declared Supply-Chain Inventory — defined
- SUP-02 Provenance Verifiability — defined
- SUP-03 Upstream Dependency Disclosure — defined
- SUP-04 Opaque Supply Chain Fails Conformance — defined

## Human & Operations (OPS)
- OPS-01 Operational Runbook Availability — planned
- OPS-02 Role Redundancy — planned
- OPS-03 Operator Access Independence — planned
- OPS-04 Operational Capability Evidence — planned

## Physical Connectivity (PHY)
- PHY-01 Connectivity Dependency Declaration — planned
- PHY-02 Single-Path Detection — planned
- PHY-03 Partition Scenario Consideration — planned

---

## Evidence artifact hints (non-normative)
- AUTH/POL: authority/policy artifacts with versions/provenance; refusal/escalation evidence.
- EXEC: envelope declarations; admission outcomes; degraded-mode evidence.
- DATA: residency/classification declarations; key ownership; lineage traces.
- EVID: event schemas; hash-chained logs; local buffers and reconciliation records.
- INT/EXIT: API/interface docs; portability/exit plans; exercised exit evidence.
- DEP: dependency graphs; concentration metrics; non-substitutable declarations.
- SUP: SBOMs; provenance attestations; upstream disclosures (planned).
- OPS: runbooks; drills; access independence proofs (planned).
- PHY: connectivity dependency declarations; single-path detection tests (planned).
