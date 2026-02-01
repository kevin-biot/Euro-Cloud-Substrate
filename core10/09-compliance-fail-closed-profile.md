# Compliance Fail-Closed Profile — Placeholder

## Intent
Define conditions that must block execution for compliance-critical flows.

## Invariant families (refs)
- POL (fail-closed semantics)
- AUTH (authority refusal)
- EVID (refusal/escalation evidence)
- CRP ties: AUTH-04/POL-04 in partition

## Applicable invariant IDs
- POL-04/05, AUTH-04, EVID-01/04, POL-01/02/03, AUTH-01/02/05

## Evidence expectations
- Preconditions and refusal/escalation events captured with authority/policy context.
- Exception approvals (time-bound) and audit trail.
- Proof of fail-closed behavior under uncertainty/partition.

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
