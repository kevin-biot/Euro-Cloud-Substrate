# Euro Object Storage Contract (EOSC) — Placeholder

## Intent
S3-compatible surface with governance metadata requirements for portability and auditability.

## Invariant families (refs)
- DATA (residency, classification)
- EVID (evidence pointers, integrity)
- SUP (inventory, provenance)
- EXIT/INT (portability)

## Applicable invariant IDs
- DATA-01/02/05, EVID-01/03/04, SUP-01/02/03/04, INT-01/03, EXIT-01/02/03

## Evidence expectations
- Metadata enforcement (jurisdiction, retention/TTL, integrity) on write/read.
- Evidence pointers and hash integrity; SBOM/provenance for storage stack.
- Portability/export interfaces with evidence of success/refusal.

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
