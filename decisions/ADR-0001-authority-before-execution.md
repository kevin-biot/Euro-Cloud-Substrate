# ADR-0001: Authority Before Execution

## Status
Accepted

## Context
ECS aims to provide enforceable governance. Early reviewers highlighted the need to codify that governed actions cannot proceed without explicit authority validation.

## Decision
All governed actions MUST validate explicit human or institutional authority before execution. If authority cannot be established, the system MUST refuse execution (fail closed). Refusal and escalation are first-class outcomes and MUST be recorded as evidence events.

## Consequences
- Control planes MUST incorporate authority checks before resource creation/update/delete.
- Execution envelopes MUST fail closed if authority evidence is absent or stale.
- Evidence/audit models MUST capture authority context and refusal/escalation events.
- API and UX flows MUST surface refusal and escalation as governed, not error, states.
