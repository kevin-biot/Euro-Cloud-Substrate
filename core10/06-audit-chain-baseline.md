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
