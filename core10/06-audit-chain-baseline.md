# Audit Chain Baseline — Placeholder

## Intent
Hash-linked log requirements for compliance-critical flows.

## Invariant families (refs)
- EVID (integrity, chaining)
- AUTH/POL/EXEC (context carried in audit chain)

## Applicable invariant IDs
- EVID-03/04/05, AUTH-01/02/04, POL-01/02/03/04/05, EXEC-05

## Evidence expectations
- Hash-linked chains for compliance-critical events.
- Exportable, verifiable chain state.
- Inclusion of authority/policy/execution context.

## Requirements (draft)
- Compliance-critical evidence MUST be hash-linked to provide tamper evidence (EVID-03).
- Chains MUST include authority/policy/execution context from evidence events (Core10-05 Evidence Event Model).
- Chain state MUST be exportable and independently verifiable (EVID-04).
- Retention MUST be enforced and auditable.
- Reconciliation MUST detect gaps/tampering; detection events MUST be logged.

## Chain model (draft)
- Integrity: hash chaining using approved algorithms (e.g., sha256) over ordered events.
- Ordering: monotonic ordering with sequence numbers/timestamps; ordering preserved in export.
- Integrity field in events SHOULD include link/hash to prior event for chaining.

## Export/verification
- Provide export of chain segments with necessary proofs (hashes, signatures if used).
- Verification MUST allow independent re-computation of chain integrity.

## Conformance outline (draft)
- Validate hash chaining over compliance-critical events; detect tampering on replay.
- Verify inclusion of context (authority/policy/execution) in chain records.
- Test export and independent verification of chain segments.
- Confirm retention enforcement and logging of reconciliation/tamper detection.

## To cover
- Chaining model, integrity proofs, and retention expectations.
- How evidence events are included and verified.
- Interfaces for audit queries and export.

## Invariants (draft)
- Compliance-critical evidence MUST be hash-linked to provide tamper evidence.
- Chain state MUST be exportable and independently verifiable.
- Retention periods MUST be enforced and auditable.

## Next steps
- Define conformance requirements and verification approach.
- Align with Evidence Event Model and Interop APIs.
