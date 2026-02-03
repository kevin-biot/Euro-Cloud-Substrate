# Execution Invariants (EXEC) — Draft

## Scope
- Applies to workload execution, envelopes, and runtime dependencies.
- Covers admission, control-plane independence, and auditability.

## Invariants
- **EXEC-01 — Execution Envelope Declaration**  
  Workloads MUST declare an execution envelope before admission.
- **EXEC-02 — No Undeclared Runtime Dependencies**  
  Runtime dependencies MUST be declared and evidenced.
- **EXEC-03 — Control-Plane Independence**  
  Execution MUST tolerate control-plane unavailability within defined modes.
- **EXEC-04 — Deterministic Degradation Modes**  
  Degraded behavior MUST be deterministic and auditable.
- **EXEC-05 — Execution Behaviour Auditability**  
  Execution decisions and outcomes MUST be evidence-backed.

## Evidence expectations
- Envelope declarations and admission decisions.
- Dependency manifests for runtime components.
- Degradation mode evidence and execution lifecycle events.

## Non-goals
- No mandate on orchestrator or runtime technology.
- No performance or scheduling policy requirements.
