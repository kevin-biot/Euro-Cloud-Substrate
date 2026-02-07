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
    "owner_id": { "type": "string" },
    "data_space_id": { "type": "string" },
    "version": { "type": "string" },
    "schema_ref": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "retention": { "type": "string" },
    "usage_policy_snapshot_id": { "type": "string" },
    "purpose_id": { "type": "string" },
    "consent_token_ref": { "type": "string" },
    "obligations_ref": { "type": "string" },
    "lineage_ref": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["data_product_id", "provider_id", "owner_id", "jurisdiction", "classification", "usage_policy_snapshot_id", "evidence_pointer"]
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
- Export bundles per `docs/evidence/export-schema.md`.

## Obligations enforcement (draft)
Policy is only real if it is enforced **at execution time**. For governed data:
- **Obligations MUST be evaluated pre‑hoc** (before access/use), not after the fact.
- **Refusal evidence** is required when obligations cannot be satisfied.
- Obligations should include **purpose binding**, **retention**, **residency**, and **no‑onward‑transfer** constraints where applicable.

## Owner‑rooted trust (non‑normative)
ECS allows **owner‑rooted trust** models where authority keys originate with the data owner (not the platform).  
Such systems are compatible as long as authority snapshots and evidence bundles are exportable and verifiable.

Self‑certifying identifiers (e.g., DID:web or micro‑ledger‑backed identifiers) MAY be used as trust anchors when their verification proofs are exportable.

## Deterministic evidence export (draft)
- Data access events and lineage MUST be exportable as evidence bundles.
- Evidence MUST be generated contemporaneously with access decisions (pre-hoc), not reconstructed later.

## Privacy-by-design evidence (draft)
- Consent and purpose binding evidence SHOULD be emitted for governed data access.
- Minimization/redaction decisions SHOULD be evidenced where applicable.
See `docs/domains/privacy.md` for privacy domain expectations.

## Interoperability & portability (draft)
- Governed data sharing MUST include standardized metadata and exportable bundles (INT/EXIT).
- Export packages MUST preserve classification, residency, and policy bindings.

## Jurisdiction‑aware routing (non‑normative)
ECS requires **jurisdiction‑aware routing** for governed data flows, with refusal evidence when a route violates policy.  
Specific routing standards (e.g., AARP‑class protocols) can implement that capability.  
ECS does not prescribe the routing protocol, only the **evidence/contract expectations**.

## Usage metering evidence (draft)
- Governed data access SHOULD emit a usage receipt record suitable for attribution or billing, without prescribing pricing.
- Usage receipts MUST be exportable as evidence bundles and tied to policy/consent references.

## Non-goals
- No mandated encryption algorithm or KMS vendor.
- No data governance policy beyond enforceable controls.
