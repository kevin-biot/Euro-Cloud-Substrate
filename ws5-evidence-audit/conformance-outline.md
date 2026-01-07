# WS5 Conformance Outline (Draft)

## Event schema and completeness
- Validate required fields (who/what/when/why/outcome, policy snapshot, authority context) are present.
- Ensure refusal/escalation outcomes are emitted as first-class events.

## Integrity and chaining
- Verify hash chaining for compliance-critical flows; detect tampering on replay.
- Confirm time-ordering is monotonic and auditable.

## Storage and retention
- Test durable storage and retention enforcement for evidence streams.
- Validate partition-tolerant buffering (for CRP) and later reconciliation.

## Query and export
- Audit queries MUST preserve ordering and integrity proofs.
- Exports MUST be in a documented, provider-neutral format suitable for regulators/customers.
