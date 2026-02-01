# EOSC Neutral Interop (Draft)

Goal: define a semi-standard, interoperable EOSC service that providers can implement.

## Minimal interoperable surface
- S3-compatible API subset: PUT, GET, DELETE, LIST, multipart, versioning, object lock/immutability.
- Governance metadata headers (required):
  - `x-eosc-jurisdiction` (ISO 3166)
  - `x-eosc-retention-ttl` (ISO 8601 duration or RFC 3339 timestamp)
  - `x-eosc-integrity` (algo:value)
  - `x-eosc-classification` (provider-declared vocabulary)
  - `x-eosc-evidence-pointer` (evidence URI)
- Error semantics: deterministic metadata validation errors with machine-readable codes.

## Interop expectations
- Metadata must be preserved on copy/move/replication across regions/providers.
- Jurisdiction enforcement must block non-permitted placements; failures emit evidence.
- Integrity must be enforced on write; optional verify-on-read mode.
- Evidence events must be generated for governed operations (aligned with WS5).

## Optional/extension points
- Presigned URLs (if supported, must enforce metadata requirements).
- Additional metadata fields allowed but MUST NOT weaken required governance fields.

## Notes
- This is a draft interop view for EOSC; align with `ws2-eosc/spec.md` for full semantics.
