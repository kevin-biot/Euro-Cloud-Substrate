# Data Act as Architecture Constraint (Draft, Non‑Normative)

## Intent
Use the EU Data Act as a **design forcing function** to validate ECS architecture choices, not as a compliance checklist.

## Non‑negotiable architectural principles (draft)
1. **Structural portability** — data and workloads can move without provider‑specific re‑engineering.
2. **Continuous portability** — exportability is continuous, not an end‑of‑life ritual.
3. **Symmetric switching** — exit is feasible without disproportionate cost, latency, or downtime.
4. **Control‑plane neutrality** — governance and control are not hard‑bound to a single provider.
5. **Evidence by default** — portability and exit are evidenced, not assumed.
6. **Dependency transparency** — critical dependencies are declared and exportable.
7. **Failure‑tolerant exit** — exit and portability still work under degraded conditions.

## Where ECS already aligns
- **Exit & portability**: Core10‑10, INT/EXIT invariants, evidence export schema.
- **Evidence by default**: Core10‑05/06, evidence catalog, export bundles.
- **Control‑plane neutrality**: plane separation + interop API surface.
- **Dependency transparency**: DEP/SUP deep‑dives + metrics/checklists.

## Where ECS still assumes provider good behavior
- **Switching economics**: ECS defines technical exit but not economic symmetry (egress fees).
- **Operational ergonomics**: portability is possible but not necessarily “boringly usable.”
- **Managed service opacity**: evidence hooks for managed ML services are not guaranteed.

## Stress‑test example: switching semantics
**Question:** Can a workload migrate with minimal downtime and preserved evidence?  
**ECS response:**  
- Requires export package (Core10‑10) + evidence export schema.  
- Requires interoperable APIs (Core10‑08) and declared dependencies (DEP).  
**Risk:** If provider refuses to emit evidence or charges punitive egress, exit is *technically* possible but *economically* constrained.

## Implication
ECS should treat the Data Act as validation: if these constraints became mandatory, ECS already provides the reference “how.” The remaining work is operationalization and evidence hooks in real platforms.
