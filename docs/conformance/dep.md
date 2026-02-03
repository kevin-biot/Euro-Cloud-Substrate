# DEP Conformance Checklist (Draft)

## Required evidence
- Dependency graph per critical service (with substitutable vs non‑substitutable tags).
- Declared critical path dependencies and ownership.
- Evidence of exceptions and compensating controls.

## Minimal tests (pass/fail)
1. **Critical path exists:** each critical service has a dependency graph.
2. **Non‑substitutable declared:** any non‑substitutable dependency is explicitly declared.
3. **Exclusivity mitigated:** single‑actor critical path has documented compensating control or exception.
4. **Exportable evidence:** dependency evidence is exportable in a machine‑readable format.
5. **Change tracking:** dependency changes generate evidence events.
