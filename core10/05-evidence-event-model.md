# Evidence Event Model — Placeholder

## Intent
Standard event types for authorization, execution, refusal, escalation, policy snapshot, retention duty, etc.

## Scope and assumptions
- Applies to all governed actions across planes; evidence is first-class output.
- Evidence events are exported in provider-neutral formats.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Evidence event: immutable record of a governed action or system state change.
- Event envelope: minimal set of fields required for integrity, ordering, and audit.
- Evidence pointer: URI/hashlink to immutable evidence artifact or log segment.

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
- Export bundles MUST follow `docs/evidence-export-schema.md`.

Core10-05 defines the canonical event envelope and is profile-agnostic. Additional integrity, chaining, and domain-specific requirements are applied via Evidence Profiles (`docs/profiles/evidence-profiles.md`). Implementers MUST select an evidence profile and ensure emitted events satisfy both Core10-05 and the selected profile.

## Evidence pointer contract (draft)
Evidence pointers MUST be trustworthy, not just present:
- **Immutability:** pointer resolves to content‑addressed artifacts (hash‑based).
- **Retrievability class:** online / nearline / archive indicated in metadata.
- **Tenant scoping:** pointers must not be dereferenceable across tenants.
- **Retention & legal hold:** TTL/hold flags are enforced, not merely declared.
- **Verification:** independent verifier can validate integrity without trusting the emitter.

## EU AI Act alignment (non-normative)
- Evidence for governed actions MUST be generated contemporaneously with the action (pre-hoc), and retained for post-market monitoring and audit. Logging capability is a design-time requirement and logs must be preserved for the required retention period.

## Event envelope (draft)
- Required fields:
  - `id` (uuid)
  - `event_type` (string)
  - `occurred_at` (RFC 3339)
  - `tenant_id`
  - `actor` (subject or system)
  - `outcome` (accepted/refused/failed)
  - `evidence_pointer`
  - `sequence` (monotonic per stream)
- Required for governed actions:
  - `correlation_id` (shared across all events for a governed action)
- Optional integrity fields:
  - `chain_id` (evidence chain identifier)
  - `event_hash` (hash of canonical event payload)
  - `prev_hash` (hash chain)
  - `evidence_hash` (hash of canonical payload)
  - `monotonic_time_ns` (monotonic clock value for local ordering)

## Admissible evidence profile (draft)
For legal admissibility or subpoena‑resilience, providers SHOULD emit:
- `chain_id`, `event_hash`, and `prev_hash` for each event.
- Export bundles anchored to qualified archiving when applicable.

## Canonical event types (draft)
- `authority.check` / `authority.refusal`
- `policy.evaluate` / `policy.refusal`
- `workload.admit` / `workload.refuse` / `workload.terminate`
- `storage.write` / `storage.read` / `storage.delete`
- `evidence.export` / `evidence.reconcile`
- `audit.chain.verify`

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
    "id": { "type": "string", "format": "uuid" },
    "event_type": { "type": "string" },
    "occurred_at": { "type": "string", "format": "date-time" },
    "actor": { "type": "string" },
    "actor_details": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "type": { "type": "string", "enum": ["human", "service", "delegate"] },
        "org_id": { "type": "string" },
        "credential_ref": { "type": "string" },
        "jurisdiction": { "type": "string" }
      }
    },
    "tenant_id": { "type": "string" },
    "resource_id": { "type": "string" },
    "action": { "type": "string" },
    "correlation_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "context": { "type": "object" },
    "outcome": { "type": "string", "enum": ["accepted", "refused", "failed"] },
    "refusal_reason": { "type": "string" },
    "evidence_pointer": { "type": "string" },
    "sequence": { "type": "integer" },
    "chain_id": { "type": "string" },
    "event_hash": { "type": "string" },
    "prev_hash": { "type": "string" },
    "evidence_hash": { "type": "string" },
    "monotonic_time_ns": { "type": "integer" }
  },
  "required": ["id", "event_type", "occurred_at", "actor", "tenant_id", "outcome", "evidence_pointer", "sequence"]
}
```

## Conformance outline (draft)
- Declare the selected evidence profile and validate events against its requirements.
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
