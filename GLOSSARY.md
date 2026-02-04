# Glossary (Draft)

- **Execution Envelope:** Declared runtime profile (e.g., container, VM) with defined controls and evidence expectations (EXEC-01..05).
- **Authority Binding:** Association of actions/resources with explicit authority (AUTH-01/02/04/05) and refusal semantics.
- **Policy Snapshot:** Versioned policy artifact with provenance (POL-01/02/04/05) used for deterministic evaluation.
- **Fail-Closed:** Execute only when prerequisites (authority/policy/data) are satisfied; otherwise refuse (POL-04, AUTH-04).
- **Evidence Event:** Canonical event with authority/policy/execution context, ordered and tamper-evident (EVID-01..05).
- **Audit Chain:** Hash-linked evidence stream providing tamper evidence and exportability (Core10-06, EVID-03/04/05).
- **CRP:** Crisis Resilience Profile; a profile over invariants for partition/rupture tolerance.
- **Profile:** A subset/tightening of invariants; references invariant IDs; no new semantics (see `docs/profiles/`).
- **IRN Crosswalk:** Non-normative mapping of IRN “what” to ECS “how” via invariants/evidence (docs/mappings/irn-mapping.md).
