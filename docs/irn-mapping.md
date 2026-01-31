# IRN ↔ ECS Crosswalk (Draft, Non-Normative)

**Status:** draft / non-normative  
**Purpose:** map the IRN grid (“what”) to ECS (“how” via invariants and evidence).  
**Non-goals:** does not reproduce IRN scoring; no compliance scoring. Links IRN criteria to ECS controls/invariants and evidence.

## How to read this
- **IRN criterion:** IRN matrix item (e.g., Meta-1, RES-2.2).
- **ECS invariant families:** v0.3 taxonomy (AUTH/POL/EXEC/DATA/EVID/INT/EXIT/DEP/SUP/OPS/PHY).
- **ECS references:** Core10 / CRP / workstreams implementing the intent.
- **Evidence expectations:** auditable evidence if alignment is claimed.
- **Status:** `covered`, `partially-covered`, `gap`, `tbd`, or `out-of-scope (ECS)`.

## Starter crosswalk table

| IRN criterion | Intent (short) | ECS invariant families | ECS references (current) | Evidence expectations (examples) | Status |
|---|---|---|---|---|---|
| Meta-1 — sponsoring exécutif dépendance numérique | Executive sponsorship for digital dependency | GOV (outside ECS) + DEP + EVID | No direct ECS control; ECS can supply dependency/evidence exports | Board/COMEX decisions, dependency reports, KPIs, risk arbitration records | **out-of-scope (ECS)** |
| RES-1.1 — localisation de l’autorité décisionnelle | Acceptable jurisdiction for decision locus/service entity | AUTH + DEP + SUP | Core10-04 (Policy & Authority Interface); CRP-1/3/7 | Declared authority boundary; supplier/legal entity declaration; control-plane dependency graph | **partially-covered** |
| RES-2.1 — conformité UE (NIS2/DORA/GDPR) | Demonstrable, maintained compliance | POL + EVID + OPS | Core10-05 (Evidence Event Model); Core10-06 (Audit Chain); Core10-09 (Fail-Closed) | Policy artifacts + versions; audit chain; evidence completeness baseline; change logs | **covered (mechanism), mapping tbd** |
| RES-2.2 — exposition extraterritoriale | Reduce exposure to non-EU compelled access | AUTH + DATA + EXEC + CRP + EVID | CRP-1/2/3/4/5/7; Core10-04; Core10-09 | Local authority satisfiable; local policy snapshot; data residency enforcement; refusal semantics; evidence under partition | **covered (core)** |
| RES-2.3 — concentration dépenses fournisseur | Avoid economic dependency on one supplier | DEP + EVID | DEP family not yet specified | Critical-path identification; concentration telemetry; declared non-substitutable dependencies; mitigation records | **gap (needs DEP workstream)** |
| RES-2.4 — concentration dépenses opérateur | Avoid dependency on single operator | DEP + PHY + EVID | DEP/PHY not yet specified | Network/operator dependency declaration; single-path detection; spend/usage concentration telemetry | **gap (needs DEP/PHY)** |
| RES-2.5 — contrôle régional SOC/journaux | SOC/logs controlled in required region; timely access | DATA + EVID + OPS | Core10-05/06; CRP-5; (future) SOC/log control profile | Log residency statement; retention + integrity; access control evidence; extraction SLAs; audit results | **partially-covered** |
| RES-2.6 — pouvoir de négociation contractuelle | Impose key clauses (audit, reversibility, change of control) | EXIT + EVID + DEP | Core10-10 (Migration); Core10-06 | Exit path declaration; exercised exit validation; contract variance register (outside ECS); evidence of tested reversibility | **partially-covered** |
| RES-3.1 — localisation des données/traitements | Control where data is stored/processed | DATA + POL + EVID + CRP | CRP-4; Core10-09; Core10-05/06 | Declared residency boundary; enforced placement constraints; transfer exceptions logged; auditable locality proof | **covered (core)** |
| RES-4.1 — autonomie opérationnelle | Operate without blocking dependency (people/tech/vendor) | EXEC + OPS + CRP + EVID | CRP-1/3/6/7; Core10-07; (future) OPS profile | Runbooks; drills; admin access independence; deterministic degraded modes; evidence of autonomy exercises | **partially-covered** |
| RES-4.3 — continuité face à arrêt forcé | Resist forced stop; recover/switch | EXEC + EXIT + CRP + EVID | CRP-3/6/7; Core10-10; Core10-09 | Exit plan + drills; deterministic degraded modes; partition evidence; documented RTO/RPO assumptions | **partially-covered** |
| RES-4.4 — résilience télécom/connectivité | Stay accessible despite telecom failures | PHY + CRP + EVID | CRP-6; PHY-01/02/03/04 | Declared connectivity dependencies; single-path detection; partition scenarios; test evidence | **covered (mechanism)** |
| RES-5.1 — dépendance supply chain extra-territoriale | Reduce exposed supply chain dependencies | SUP + EVID | SUP family not yet specified | SBOM; build provenance; upstream disclosure; opaque dependency fails conformance | **gap (needs SUP workstream)** |
| RES-6.1 — interopérabilité & standards ouverts | Avoid lock-in; enable integration | INT + DEP + EXIT | Core10-08 (Interop API Surface) | Interface conformance; documented formats; critical-path extension bans; portability evidence | **partially-covered** |
| RES-6.2 — portabilité des workloads | Migrate/extract/erase with bounded impact | EXIT + INT + EVID | Core10-10 (Migration baseline) | Exit path + bounds; executed exit validation; export/erasure proof; dependency declarations | **partially-covered** |

## Notes & roadmap hooks
- Strongest alignment today: rupture tolerance (CRP) and evidence/auditability (Core10-05/06/09).
- Biggest gaps vs IRN: DEP (concentration/exclusivity), SUP (supply chain disclosure), OPS (human dependency), PHY (connectivity dependencies).
- Treat this as guidance; full alignment work belongs in Phase 1 compliance mappings.
