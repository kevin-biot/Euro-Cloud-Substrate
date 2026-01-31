# Invariant Coverage Matrix (Draft)

Structural view of how invariant families relate to ECS artifacts. This is not per-invariant mapping.

| Invariant family | Core10 | CRP | IRN (mechanism support) |
|---|---|---|---|
| AUTH | Policy & Authority Interface | CRP-1, CRP-7 | RES-1.1, RES-2.x |
| POL | Policy & Authority Interface; Fail-Closed | CRP-2, CRP-7 | RES-2.x |
| EXEC | Execution Envelopes | CRP-3, CRP-6 | RES-4.x |
| DATA | EOSC | CRP-4 | RES-3.x |
| EVID | Evidence Event Model; Audit Chain | CRP-5 | RES-2.x |
| INT | Interop API Surface | — | RES-6.1 |
| EXIT | Migration Baseline | — | RES-6.2 |
| DEP | Dependency invariants | — | RES-2.3/2.4 |
| SUP | Supply-chain invariants | — | RES-5.1 |
| OPS | (planned) | — | Meta/OPS (tbd) |
| PHY | Connectivity invariants | CRP-6 | RES-4.4 |

Notes:
- IRN column is mechanism support, not compliance mapping.
- OPS remains to be defined; meta/governance items stay out-of-scope for ECS.***
