# Compliance Fail-Closed Profile — Placeholder

## Intent
Define conditions that must block execution for compliance-critical flows.

## To cover
- Preconditions for execution; refusal semantics.
- Evidence requirements before/after execution.
- Exception handling and escalation paths.

## Invariants (draft)
- Execution of governed workloads MUST fail closed if authority, policy, or evidence prerequisites are unmet.
- Exceptions MUST be explicit, time-bound, and evidence-backed.
- Refusal and escalation outcomes MUST be recorded as first-class evidence events.

## Next steps
- Enumerate fail-closed triggers with rationale.
- Define verification and test cases.
