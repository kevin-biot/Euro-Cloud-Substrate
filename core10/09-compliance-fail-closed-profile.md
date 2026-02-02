# Compliance Fail-Closed Profile — Placeholder

## Intent
Define conditions that must block execution for compliance-critical flows.

## Scope and assumptions
- Applies to governed actions where policy, authority, or evidence prerequisites are required.
- Fail-closed is mandatory under uncertainty; exceptions are explicit and evidenced.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Fail-closed: default denial when prerequisites cannot be verified.
- Preconditions: authority validity, policy validity, evidence sink availability, integrity checks.
- Recovery: explicit re-validation that prerequisites are restored.

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

## Fail-closed triggers (draft)
- Authority invalid/expired or scope mismatch.
- Policy missing/stale/invalid or deterministic evaluation unavailable.
- Evidence sink unavailable for governed actions that require evidence.
- Integrity check failure for critical artifacts (policy, envelope, export package).
- Partition or dependency unavailability on critical path.

## Requirements (draft)
- Governed actions MUST fail closed on: missing/invalid authority, stale/invalid policy, unavailable evidence sink (for governed actions), integrity verification failure on critical artifacts.
- Fail-closed conditions MUST be explicitly defined and documented.
- Refusals MUST emit evidence with reason, authority/policy context, and timestamp.
- Exception workflows MUST require explicit approval with time bounds and evidence (per Core10-04).
- Recovery from fail-closed state MUST be evidenced.

## Buffering and reconciliation (draft)
- If evidence sink is unavailable, actions requiring evidence MUST refuse by default.
- If buffering is allowed by policy, buffer MUST be integrity-protected and time-bounded; expiry MUST refuse.
- Reconciliation MUST emit evidence for buffered events and any refusals.

## Scenarios (draft)
- Authority expired mid-request: request MUST be refused; evidence reason `authority_expired`; recovery by refreshing authority binding.
- Evidence sink unavailable: configurable behavior (`hard_fail` refuse immediately; `buffered` buffer with integrity then refuse on timeout); log sink unavailability and buffered/flush outcomes.
- Policy validation failure: deny all governed actions until valid policy restored; evidence for policy integrity failure and subsequent refusals.

## Conformance outline (draft)
- Test fail-closed behavior on each trigger condition.
- Verify refusal evidence includes context and reason.
- Validate exception workflow produces time-bounded approval evidence.
- Confirm recovery actions are evidenced.

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
