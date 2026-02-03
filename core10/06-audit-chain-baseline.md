# Audit Chain Baseline — Placeholder

## Intent
Hash-linked log requirements for compliance-critical flows.

## Scope and assumptions
- Applies to compliance-critical events emitted under Core10-05.
- Chains are per-tenant or per-domain streams with monotonic ordering.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Audit chain: ordered, hash-linked sequence of evidence events.
- Chain segment: exportable subset of the audit chain with verification material.
- Integrity proof: hash chain linkage and optional signatures.

## Invariant families (refs)
- EVID (integrity, chaining)
- AUTH/POL/EXEC (context carried in audit chain)

## Applicable invariant IDs
- EVID-03/04/05, AUTH-01/02/04, POL-01/02/03/04/05, EXEC-05

## Evidence expectations
- Hash-linked chains for compliance-critical events.
- Exportable, verifiable chain state.
- Inclusion of authority/policy/execution context.
- Export bundles MUST follow `docs/evidence-export-schema.md`.

## EU AI Act alignment (non-normative)
- Evidence for governed actions MUST be generated contemporaneously with the action (pre-hoc), and retained for post-market monitoring and audit. Logging capability is a design-time requirement and logs must be preserved for the required retention period.

## Requirements (draft)
- Compliance-critical evidence MUST be hash-linked to provide tamper evidence (EVID-03).
- Chains MUST include authority/policy/execution context from evidence events (Core10-05 Evidence Event Model).
- Chain state MUST be exportable and independently verifiable (EVID-04).
- Retention MUST be enforced and auditable.
- Reconciliation MUST detect gaps/tampering; detection events MUST be logged.

## Chain model (draft)
- Integrity: hash chaining using approved algorithms (e.g., sha256) over ordered events.
- Ordering: monotonic ordering with required `sequence` and `occurred_at`; ordering preserved in export.
- Linkage: each event includes `prev_hash` referencing the prior event hash.
- Optional signing: chain segments MAY be signed by provider key for non-repudiation.

## Chain segment schema (draft JSON)
```json
{
  "segment_id": "seg-001",
  "tenant_id": "tenant-123",
  "from_sequence": 100,
  "to_sequence": 200,
  "algorithm": "sha256",
  "events": [
    {
      "id": "evt-101",
      "sequence": 101,
      "prev_hash": "sha256:prev...",
      "event_hash": "sha256:this...",
      "event_ref": "eosc://evidence/evt-101"
    }
  ],
  "segment_hash": "sha256:segment...",
  "signature": "optional-signature"
}
```

## Export/verification
- Provide export of chain segments with necessary proofs (hashes, signatures if used).
- Verification MUST allow independent re-computation of chain integrity.
- Verification steps (draft):
  1. Validate segment hash/signature (if present).
  2. Recompute event hashes and verify `prev_hash` continuity.
  3. Confirm sequence continuity and absence of gaps.
  4. Resolve evidence pointers for selected events and validate evidence hashes.

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
