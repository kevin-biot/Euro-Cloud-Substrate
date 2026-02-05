# Immutable AI Workload Log Primitives (IALP) — Diagram

## Authorization flow (IALP)
```mermaid
flowchart TD
    Input[Inputs and context]
    Auth[Authority snapshot vN]
    Policy[Policy snapshot vN]
    Cache[Policy cache state]
    PDP[Policy decision]
    Admit[Admission gate]
    Execute[Execute or route]
    Refuse[Refuse or escalate]
    Evidence[Evidence event]
    Chain[Hash chain]
    Export[Provider-neutral export]

    Input --> Auth
    Auth --> PDP
    Policy --> Cache
    Cache --> PDP
    PDP --> Admit
    Admit --> Execute
    Admit --> Refuse
    Execute --> Evidence
    Refuse --> Evidence
    Evidence --> Chain
    Chain --> Export
```

Notes:
- Authority and policy snapshots are versioned and referenced in each decision event.
- Cache state influences whether decisions proceed or fail closed.
- Refusals are first-class outcomes with evidence, not silent failures.

### Walkthrough (aligned with VISION.md)
1. **Inputs & context** arrive at the admission gate with a correlation id.
2. **Authority snapshot vN** is resolved (who can act) and bound to the decision.
3. **Policy snapshot vN** is resolved (what is allowed), with **cache state** checked for freshness.
4. The **policy decision** yields accept/refuse; refusal is a valid outcome with explicit evidence.
5. **Evidence events** are emitted and chained for integrity, then exported via provider‑neutral bundles.

## Primitives
```mermaid
flowchart TD
    Auth[Authority Assertion Log]
    Policy[Policy Snapshot Log]
    Input[Input & Context Hash Log]
    Decision[Execution Decision Log]
    Output[Output Commitment Log]
    Refusal[Refusal & Escalation Log]
    Order[Temporal Ordering Log]

    Auth --> Order
    Policy --> Order
    Input --> Order
    Decision --> Order
    Output --> Order
    Refusal --> Order

    Order --> Chain[Hash Chain / Integrity]
    Chain --> Export[Provider-neutral Export]
```

Notes:
- All primitives feed a monotonic, tamper-evident ordering log.
- Exports MUST preserve ordering and integrity proofs.
