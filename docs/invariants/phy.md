# Physical / Connectivity Invariants (PHY) — Draft

## Scope
- Applies to network and connectivity dependencies required for execution, authority, policy, data, and evidence paths.
- Covers operator, path, and topology assumptions; excludes performance tuning and telco SLAs.
- All PHY invariants are required (none are optional in the Core list).

## Invariants
- **PHY-01 — Connectivity Dependency Declaration**  
  All critical services MUST declare their required network and telecom dependencies.
- **PHY-02 — Single-Path / Single-Operator Detectability**  
  Single-path or single-operator dependencies MUST be detectable from declared connectivity state.
- **PHY-03 — Partition Scenario Consideration**  
  At least one network partition scenario MUST be declared for each critical service.
- **PHY-04 — Connectivity Assumption Evidence**  
  Connectivity assumptions MUST be supported by observable evidence (tests, topology snapshots).

## Evidence expectations
- Connectivity dependency graphs (operator, path, topology).
- Operator/path declarations and ownership.
- Single-path detection results.
- Declared partition scenarios and exercise records.

## Non-goals
- No telco SLAs.
- No performance guarantees.
- No provider mandates.
