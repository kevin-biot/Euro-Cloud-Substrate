# WS5 Conformance Outline (Draft)

## Evidence profile selection
- Declare `evidence_profile_id` and default `hash_profile_id` in export manifests.
- Validate emitted events and verifier checks against the selected evidence profile.

## Event schema and completeness
- Validate required fields (who/what/when/why/outcome, policy snapshot, authority context) are present.
- Ensure refusal/escalation outcomes are emitted as first-class events.

## Integrity and chaining
- Verify hash chaining for compliance-critical flows; detect tampering on replay.
- Confirm time-ordering is monotonic and auditable.

## Storage and retention
- Test durable storage and retention enforcement for evidence streams.
- Validate partition-tolerant buffering (CRP) and later reconciliation to the main chain.

## CRP scenarios
- Under simulated partition, ensure evidence persists locally with integrity protection and no loss on restart.
- After restoring connectivity, verify reconciliation preserves ordering and integrity proofs.

## Query and export
- Audit queries MUST preserve ordering and integrity proofs.
- Exports MUST be in a documented, provider-neutral format suitable for regulators/customers.
