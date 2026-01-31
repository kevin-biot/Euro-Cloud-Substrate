# CRP Invariants (Draft)

- **CRP-1 — Local Authority Continuity:** Authority verification MUST be satisfiable using locally cached or locally authoritative identity and policy data. Execution MUST NOT depend on real-time upstream validation. (Refs: AUTH-01, AUTH-02)
- **CRP-2 — Local Policy Evaluation:** Policy and rubric evaluation MUST be executable locally using the last valid policy snapshot. If policy validity cannot be established, the system MUST fail closed. (Refs: POL-05, POL-04)
- **CRP-3 — Control-Plane Independence:** Execution MUST continue in the absence of upstream orchestration or scheduling services. Central control-plane availability MUST NOT be a hard dependency. (Refs: EXEC-03)
- **CRP-4 — Data Residency Enforcement:** All data required for continued operation MUST remain within the local jurisdictional boundary. Cross-border replication MAY occur only when connectivity and policy allow. (Refs: DATA-01)
- **CRP-5 — Evidence Persistence Under Partition:** Evidence events MUST be recorded locally and durably during connectivity loss and MUST be synchronisable once connectivity is restored. (Refs: EVID-02, EVID-05, EVID-03)
- **CRP-6 — Deterministic Degradation:** Under degraded conditions, the system MUST enter predefined reduced-capability modes. Behaviour under degradation MUST be deterministic and auditable. (Refs: EXEC-04)
- **CRP-7 — Explicit Refusal Semantics:** If a required authority, policy, or data dependency cannot be satisfied locally, the system MUST refuse execution rather than attempt inference or approximation. (Refs: AUTH-04, POL-04)
