# Evidence Event Model — Placeholder

## Intent
Standard event types for authorization, execution, refusal, escalation, policy snapshot, retention duty, etc.

## Invariant families (refs)
- EVID (evidence schema, integrity, completeness)
- AUTH/POL (authority/policy context in events)
- EXEC (execution lifecycle events)

## Applicable invariant IDs
- EVID-01/02/03/04/05, AUTH-01/02/04, POL-01/02/03/04/05, EXEC-05

## Evidence expectations
- Canonical schemas with required fields; hash/integrity mechanisms.
- Inclusion of authority/policy snapshot IDs and execution context.
- Ordered, tamper-evident streams with reconciliation support.

## Requirements (draft)
- Evidence events MUST follow a canonical schema with required fields (who/what/when/why/outcome).
- Events MUST include policy snapshot and authority context for governed actions.
- Streams MUST be ordered and tamper-evident; must support reconciliation (EVID-02/03/05).
- Refusal/escalation MUST be first-class outcomes.
- Evidence MUST be exportable in a provider-neutral format (EVID-04).

## Canonical schema (draft JSON)
```json
{
  "type": "object",
  "properties": {
    "event_type": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "actor": { "type": "string" },
    "tenant_id": { "type": "string" },
    "resource_id": { "type": "string" },
    "action": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "context": { "type": "object" },
    "outcome": { "type": "string", "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "integrity": { "type": "string" }
  },
  "required": ["event_type", "timestamp", "actor", "outcome"]
}
```

## Conformance outline (draft)
- Validate required fields and inclusion of authority/policy context for governed events.
- Verify ordering/tamper evidence (e.g., hash chaining) and reconciliation behavior.
- Confirm exportability and integrity of exported evidence.
- Ensure refusals/escalations are captured as first-class outcomes.

## To cover
- Canonical event schema and types.
- Required fields for evidence-grade logging.
- Integrity and ordering expectations.

## Invariants (draft)
- Evidence events MUST follow a canonical schema with required fields (who/what/when/why/outcome).
- Events MUST include policy snapshot identifiers and authority context.
- Evidence streams MUST be ordered and tamper-evident.

## Next steps
- Draft event catalog and schemas.
- Map to Audit Chain Baseline and Interop APIs.
