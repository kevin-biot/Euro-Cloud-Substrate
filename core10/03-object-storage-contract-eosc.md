# Euro Object Storage Contract (EOSC) — Placeholder

## Intent
S3-compatible surface with governance metadata requirements for portability and auditability.

## Scope and assumptions
- Applies to object storage interfaces that claim EOSC compatibility.
- Does not mandate a specific S3 provider; requires compatible surface and governance semantics.
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Governance metadata: jurisdiction, classification, retention/TTL, evidence pointer, integrity hash.
- Compliance-relevant object: objects containing regulated data or used in governed workflows.
- Evidence pointer: URI/hashlink referencing immutable evidence for the operation.

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

## Required metadata (draft)
- `x-ecs-jurisdiction` (ISO country/region)
- `x-ecs-classification` (classification ceiling)
- `x-ecs-retention` (RFC 3339 duration or policy id)
- `x-ecs-integrity` (sha256 hash of object payload)
- `x-ecs-evidence` (evidence pointer for write)

## EOSC API expectations (draft)
- Compatible with S3 object CRUD operations (PUT/GET/HEAD/DELETE).
- Required governance headers MUST be enforced on PUT; missing headers MUST be refused.
- Governance headers MUST be preserved on GET/HEAD and included in exports.
- Copy operations MUST preserve governance metadata unless explicitly reauthorized.

## Immutability and retention (draft)
- Retention/immutability flags MUST be enforced by storage backend (DATA-05).
- Early deletion attempts MUST be refused and evidenced.
- Retention changes MUST be time-bounded, authorized, and evidenced.

## Evidence events (draft)
- Object write/read/delete MUST emit evidence with governance metadata and integrity hash.
- Evidence pointers MUST be returned on compliance-relevant operations.

## Invariants (draft)
- Writes MUST require governance metadata (jurisdiction, retention/TTL, integrity).
- Governance metadata MUST persist and travel with the object across providers.
- Immutability/retention flags MUST be enforced and auditable.
- Evidence pointers MUST be generated for compliance-relevant objects/operations.

## Conformance outline (draft)
- Declare selected evidence profile for EOSC evidence exports.
- PUT without required governance headers MUST be refused with evidence.
- PUT/GET/HEAD MUST round-trip governance metadata and integrity hash.
- Retention enforcement MUST block early deletion and log refusal evidence.
- Export MUST preserve governance metadata and integrity proofs.

## Next steps
- Align with `ws2-eosc/spec.md` governance header definitions.
- Define conformance checks for metadata enforcement and integrity.
