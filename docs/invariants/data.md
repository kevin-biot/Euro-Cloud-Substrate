# Data Invariants (DATA) — Draft

## Scope
- Applies to data residency, classification, lineage, and portability.
- Covers cryptographic authority control and enforceable erasure/export.

## Data-space artifacts (draft)
- **Data product descriptor:** minimum metadata for governed data sharing.
- **Usage policy binding:** explicit link to policy snapshot id (POL/EVID).
- **Purpose/consent reference:** link to consent/intent token (CITP).
- **Evidence pointer:** link to evidence bundle for access/transfer decisions.

### Data product descriptor (draft JSON)
```json
{
  "type": "object",
  "properties": {
    "data_product_id": { "type": "string" },
    "provider_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "retention": { "type": "string" },
    "usage_policy_snapshot_id": { "type": "string" },
    "consent_token_ref": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["data_product_id", "provider_id", "jurisdiction", "classification", "usage_policy_snapshot_id", "evidence_pointer"]
}
```

## Invariants
- **DATA-01 — Data Residency Enforceability**  
  Residency requirements MUST be enforced and evidenced.
- **DATA-02 — Data Class Declaration**  
  Data classification MUST be declared and enforced.
- **DATA-03 — Cryptographic Authority Control**  
  Key control MUST align to declared authority boundaries.
- **DATA-04 — Data Lineage Traceability**  
  Lineage for governed data MUST be traceable and auditable.
- **DATA-05 — Enforceable Erasure and Export**  
  Erasure and export MUST be enforceable and evidenced.

## Evidence expectations
- Residency declarations and enforcement evidence.
- Classification tags and policy bindings.
- Key custody proofs and authority mapping.
- Lineage records and export/erasure evidence.
- Data product descriptors and usage policy binding (POL/EVID).
- Consent/intent token references for governed access (CITP).
- Export bundles per `docs/evidence-export-schema.md`.

## Deterministic evidence export (draft)
- Data access events and lineage MUST be exportable as evidence bundles.
- Evidence MUST be generated contemporaneously with access decisions (pre-hoc), not reconstructed later.

## Privacy-by-design evidence (draft)
- Consent and purpose binding evidence SHOULD be emitted for governed data access.
- Minimization/redaction decisions SHOULD be evidenced where applicable.
See `docs/privacy-domain.md` for privacy domain expectations.

## Interoperability & portability (draft)
- Governed data sharing MUST include standardized metadata and exportable bundles (INT/EXIT).
- Export packages MUST preserve classification, residency, and policy bindings.

## Usage metering evidence (draft)
- Governed data access SHOULD emit a usage receipt record suitable for attribution or billing, without prescribing pricing.
- Usage receipts MUST be exportable as evidence bundles and tied to policy/consent references.

## Non-goals
- No mandated encryption algorithm or KMS vendor.
- No data governance policy beyond enforceable controls.
