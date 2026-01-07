# Evidence Event Model — Placeholder

## Intent
Standard event types for authorization, execution, refusal, escalation, policy snapshot, retention duty, etc.

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
