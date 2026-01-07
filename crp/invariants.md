# CRP Invariants (Draft)

- **CRP-1 — Local Authority Continuity:** Authority verification MUST be satisfiable using locally cached or locally authoritative identity and policy data. Execution MUST NOT depend on real-time upstream validation.
- **CRP-2 — Local Policy Evaluation:** Policy and rubric evaluation MUST be executable locally using the last valid policy snapshot. If policy validity cannot be established, the system MUST fail closed.
- **CRP-3 — Control-Plane Independence:** Execution MUST continue in the absence of upstream orchestration or scheduling services. Central control-plane availability MUST NOT be a hard dependency.
- **CRP-4 — Data Residency Enforcement:** All data required for continued operation MUST remain within the local jurisdictional boundary. Cross-border replication MAY occur only when connectivity and policy allow.
- **CRP-5 — Evidence Persistence Under Partition:** Evidence events MUST be recorded locally and durably during connectivity loss and MUST be synchronisable once connectivity is restored.
- **CRP-6 — Deterministic Degradation:** Under degraded conditions, the system MUST enter predefined reduced-capability modes. Behaviour under degradation MUST be deterministic and auditable.
- **CRP-7 — Explicit Refusal Semantics:** If a required authority, policy, or data dependency cannot be satisfied locally, the system MUST refuse execution rather than attempt inference or approximation.
