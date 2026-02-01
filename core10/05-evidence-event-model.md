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
