# Reference Architecture (Skeleton)

## Planes
- **Plane A — Identity, Tenancy, Authority:** tenant model, identity binding, explicit authority points, accountable ownership.
- **Plane B — Control Plane & Landing Zone:** network/policy baseline, observability baseline, audit baseline, admission gates.
- **Plane C — Execution Envelopes:** container orchestration baseline (Kubernetes), VM/TEE envelope profiles for stronger isolation.
- **Plane D — Data & Evidence Substrate:** EOSC object storage, governance metadata, evidence chain persistence.
- **Plane E — Interop & Portability:** versioned interop APIs, export/import flows, migration validation gates.

See `docs/architecture/control-plane.md` for control-plane capability definitions (policy engine, admission gate, evidence hooks).

## Diagram convention
- Mermaid is the baseline for diagrams in this repo.

## Conceptual diagram (Mermaid)
```mermaid
flowchart TB
    subgraph A["Plane A: Authority & Identity"]
      A1["Org/Tenant/Project Identity"]
      A2["Authority Binding (Human/Institutional)"]
      A3["Decision Rights"]
    end

    subgraph B["Plane B: Control Plane / Landing Zone"]
      B1["Network & Egress Baseline"]
      B2["Policy Enforcement & Refusal"]
      B3["Audit & Evidence Emission"]
      B4["Deterministic Routing"]
    end

    subgraph C["Plane C: Execution Envelopes"]
      C1["Kubernetes Envelope"]
      C2["VM-class Envelope"]
      C3["Lifecycle Boundaries"]
    end

    subgraph D["Plane D: Data & Evidence Substrate"]
      D1["EOSC Object Storage"]
      D2["Governance Metadata"]
      D3["Immutable Evidence Chains"]
    end

    subgraph E["Plane E: Interop & Portability"]
      E1["Interop API Surface"]
      E2["Export/Import Jobs"]
      E3["Migration Validation"]
    end

    A -->|Authority check| B
    A -->|Ownership attribution| B
    B -->|Route / refuse| C
    B -->|Evidence events| D
    C -->|Read/write data| D
    C -->|Integrity hashes| D
    B -->|Interop API| E
    D -->|Evidence export| E
```

## Plane boundaries and flows (Mermaid)
```mermaid
flowchart TB
    subgraph A["Plane A: Identity & Authority"]
      A0["Authority Binding Registry"]
    end
    subgraph B["Plane B: Control Plane"]
      B0["Admission Gate"]
      B1["Policy Engine"]
      B2["Control Plane API"]
    end
    subgraph C["Plane C: Execution"]
      C0["Runtime Envelopes"]
    end
    subgraph D["Plane D: Data & Evidence"]
      D0["EOSC Storage"]
      D1["Evidence Chain"]
    end
    subgraph E["Plane E: Interop & Portability"]
      E0["Interop API"]
      E1["Export/Import"]
    end

    A0 -->|Control: authority check| B0
    B2 -->|Control: governed action| B0
    B0 -->|Control: allow/refuse| B2
    B0 -->|Evidence: admission decision| D1
    B2 -->|Control: start/stop workloads| C0
    C0 -->|Data: read/write| D0
    D1 -->|Evidence: export/verify| E1
    B2 -->|Interop: API surface| E0
```

## Core10-to-plane mapping (draft)
| Core10 component | Primary plane(s) | Cross-plane dependencies |
|---|---|---|
| 01 Open Landing Zone | A, B | D (evidence) |
| 02 Tenant Isolation | C | B (admission), D (evidence) |
| 03 EOSC Object Storage | D | E (export), B (policy) |
| 04 Policy & Authority | A, B | D (evidence) |
| 05 Evidence Event Model | D | B/C (emitters), E (export) |
| 06 Audit Chain Baseline | D | B/C (evidence sources) |
| 07 Execution Envelopes | C | B (admission), D (evidence) |
| 08 Interop API Surface | E | A/B (authz), D (evidence) |
| 09 Fail-Closed Profile | B | A (authority), D (evidence) |
| 10 Migration Baseline | E | D (evidence), B (policy), A (authority) |

## Stack view for archetypes (non-normative)
The IPCEI‑CIS reference architecture uses a layered stack (Application → Data → AI → Service Orchestration → Cloud‑Edge Platform → Virtualization → Network → Physical). ECS can map archetypes to that stack without prescribing a platform.

| Archetype | ICRA layer emphasis | ECS focus (contract layer) |
|---|---|---|
| OpenShift‑like | Service Orchestration + Cloud‑Edge Platform + Virtualization | OLZ‑EU baseline, admission evidence, execution envelopes, export bundles |
| VM‑first | Virtualization + Network + Physical | VM envelope profile, data governance metadata, evidence export/migration |
| Managed‑platform | Application + Service Orchestration + Data/AI | Interop API surface, evidence profiles, regulated‑ML evidence exports |

This provides a neutral “stack view” so vendors can self‑place while implementing the same ECS contract layer.

## Architecture upgrade roadmap (draft)
1. **Baseline clarity:** finalize plane boundaries, control/evidence interfaces, and glossary alignment.
2. **Control plane hardening:** specify policy engine and admission gate requirements with conformance tests.
3. **Evidence chain maturity:** define canonical event types, chain verification format, and export schema.
4. **Interop/API hardening:** publish minimal OpenAPI/AsyncAPI surfaces with error and auth semantics.
5. **Portability at scale:** define migration workflows, validation gates, and reference export package format.
6. **Archetype validation:** map OpenShift/VM/Managed/SlapOS stacks to the planes and highlight gaps.

## Evidence and control flows (fail-closed + escalation)
```mermaid
sequenceDiagram
    participant Caller as "Caller"
    participant Admission as "Admission Gate"
    participant Policy as "Policy Engine"
    participant Authority as "Authority Binding"
    participant Evidence as "Evidence Store"
    participant Escalation as "Escalation Path"

    Caller->>Admission: Request governed action
    Admission->>Authority: Validate authority binding
    Authority-->>Admission: Valid/Invalid
    Admission->>Policy: Evaluate policy snapshot
    Policy-->>Admission: Allow/Refuse/Uncertain
    alt Allow
        Admission->>Evidence: Emit allow decision (with snapshots)
        Admission-->>Caller: Permit with evidence pointer
    else Refuse
        Admission->>Evidence: Emit refusal decision (reason + snapshots)
        Admission-->>Caller: Refuse with evidence pointer
    else Uncertain
        Admission->>Evidence: Emit fail-closed decision
        Admission-->>Caller: Refuse (fail-closed)
        Admission->>Escalation: Optional escalation workflow
    end
```

## Deliverables map (Mermaid)
```mermaid
flowchart LR
    Invariants[Invariants v0.3<br/>docs/invariants/v0.3.md]
    Profiles[Profiles<br/>crp/, docs/profiles/]
    Core10[Core10<br/>core10/]
    WS[Workstreams<br/>ws*/]
    Arch[Architecture pack<br/>docs/architecture/]
    Gov[Governance & Process<br/>GOVERNANCE.md, CONTRIBUTING.md, decisions/]
    Conf[Conformance Model<br/>docs/conformance/model.md]

    Invariants --> Profiles
    Invariants --> Core10
    Invariants --> WS
    Core10 --> Arch
    WS --> Arch
    Profiles --> Arch
    Invariants --> Conf
    Profiles --> Conf
    Core10 --> Conf
    WS --> Conf
    Gov --> Conf
```

## Invariants-to-components overview (Mermaid)
```mermaid
flowchart TB
    Inv[Invariants v0.3<br/>docs/invariants/v0.3.md]
    Core10[Core10 Components<br/>core10/]
    WS[Workstreams<br/>ws*/]
    Profiles[Profiles<br/>crp/]

    Inv --> Core10
    Inv --> WS
    Inv --> Profiles
    Profiles --> WS
```

## Archetypes (non-normative)
These archetypes map the ECS planes to common provider architectures so vendors can align existing stacks to ECS without prescribing a single universal design.

- OpenShift/Kubernetes-based: `docs/architecture/archetypes/openshift.md`
- VM-first / IaaS-centric: `docs/architecture/archetypes/iaas-vm.md`
- Managed platform competitor: `docs/architecture/archetypes/managed-platform.md`
- SlapOS (master/compute, partitions): `docs/architecture/archetypes/slapos.md`

## Compliance pattern library (draft)
- `docs/compliance/pattern-library.md` (non-normative)
