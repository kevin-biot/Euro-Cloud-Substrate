# Euro Object Storage Contract (EOSC) — Placeholder

## Intent
S3-compatible surface with governance metadata requirements for portability and auditability.

## Invariant families (refs)
- DATA (residency, classification)
- EVID (evidence pointers, integrity)
- SUP (inventory, provenance)
- EXIT/INT (portability)

## To cover
- API surface and compatibility expectations.
- Metadata contract: jurisdiction tags, retention/TTL, evidence pointers, integrity hashes.
- Immutability and selective retention semantics.

## Invariants (draft)
- Writes MUST require governance metadata (jurisdiction, retention/TTL, integrity).
- Governance metadata MUST persist and travel with the object across providers.
- Immutability/retention flags MUST be enforced and auditable.
- Evidence pointers MUST be generated for compliance-relevant objects/operations.

## Next steps
- Draft spec and invariants.
- Define conformance checks for metadata enforcement and integrity.
