# Crisis Resilience Profile (CRP) — Diagram

```mermaid
flowchart LR
    A[Normal Mode] -->|Connectivity loss| B[Partition Mode]
    B -->|Local policy/authority evaluation| B
    B -->|Connectivity restored| C[Recovery Mode]
    C -->|Reconcile evidence & state| A

    subgraph Partition Controls
      B1[Local Authority Cache]
      B2[Local Policy Snapshot]
      B3[Local Evidence Buffer]
      B4[Deterministic Degradation Modes]
    end

    A --> B1
    A --> B2
    A --> B3
    B --> B4
    B3 --> C
```

Key notes:
- Partition Mode relies on local authority/policy snapshots; fail closed if unsatisfied.
- Evidence is buffered locally and reconciled in Recovery Mode.
- Degradation modes are deterministic and auditable.
