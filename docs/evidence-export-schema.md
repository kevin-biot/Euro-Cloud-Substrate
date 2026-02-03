# Evidence Export Schema (Normative)

## Intent
Define a portable, deterministic export package for compliance evidence, aligned to pre-hoc evidence generation and post-market monitoring requirements.

## Scope and assumptions
- Applies to governed actions and their evidence across ECS planes.
- Evidence MUST be generated contemporaneously with actions (pre-hoc) and retained for audit/export.
- This schema is normative; implementations may vary but MUST preserve semantics and integrity rules.

## Core terms
- **Evidence bundle:** cryptographically verifiable package of events + artifacts.
- **Chain segment:** ordered subset of evidence events with integrity proofs.
- **Artifact:** referenced item such as policy snapshot, consent token, risk rubric, duty token, corridor proof, SBOM, or delta proof.

## Package structure (normative)
An export package MUST include:
1. **Manifest** (required)
2. **Chain segment(s)** (required)
3. **Evidence events** (required)
4. **Referenced artifacts** (required for governed actions)

## Manifest schema (draft JSON)
```json
{
  "schema_version": "1.0",
  "export_id": "exp-001",
  "created_at": "2025-01-01T00:00:00Z",
  "provider_id": "provider-A",
  "tenant_id": "tenant-123",
  "scope": {
    "from_sequence": 100,
    "to_sequence": 200
  },
  "chain_segment_ref": "eosc://evidence/chain/seg-001",
  "bundle_hash": "sha256:...",
  "artifacts": {
    "policy_snapshots": ["eosc://policy/pol-001"],
    "authority_bindings": ["eosc://authority/auth-789"],
    "consent_tokens": ["eosc://consent/citp-001"],
    "risk_rubrics": ["eosc://risk/rrp-001"],
    "duty_tokens": ["eosc://duty/mdpp-001"],
    "corridor_proofs": ["eosc://routing/scrp-001"],
    "evidence_deltas": ["eosc://delta/edp-001"],
    "sbom_refs": ["eosc://sbom/model-001"]
  },
  "signatures": [
    { "key_id": "key-001", "signature": "base64..." }
  ]
}
```

## Evidence event requirements
- Evidence events MUST conform to the Core10-05 envelope (id, occurred_at, sequence, outcome, tenant_id, evidence_pointer, correlation_id for governed actions).
- Outcome values MUST be `accepted`, `refused`, or `failed`.
- Evidence events MUST reference relevant artifacts (policy snapshot, authority binding, consent token, duty token, corridor proof, risk rubric) when applicable.

## Integrity rules (normative)
- `bundle_hash` MUST be a Merkle root over the ordered evidence event hashes.
- Each event MUST include `prev_hash` to support chain continuity checks.
- Chain segments MUST be exportable and independently verifiable (see Core10-06).
- Signatures are OPTIONAL but, if present, MUST cover the manifest and bundle hash.

## AI/agent extension (non-normative)
AI/agent workloads MAY include an extension object:
```json
{
  "ai_extension": {
    "model_sbom_ref": "eosc://sbom/model-001",
    "input_hash": "sha256:...",
    "context_hash": "sha256:...",
    "output_ref": "eosc://output/obj-123"
  }
}
```

## Conformance checks (draft)
- Manifest schema validation and required artifacts present.
- Deterministic recomputation of `bundle_hash` from event hashes.
- Chain continuity validation (`prev_hash`, sequence).
- Artifact resolution and integrity verification.
