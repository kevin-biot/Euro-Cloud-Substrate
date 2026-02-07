# EU Compliance Pattern Library (Draft, Non-Normative)

Supporting reference patterns for translating legal obligations into runtime-enforceable, evidence-generating design primitives. This draft is intended to guide architecture review and future standardisation work; it is not a binding standard.
See `docs/domains/grc.md` for the GRC domain overview and evidence expectations.
See `docs/domains/privacy.md` for privacy-by-design, consent, and minimization expectations.

## Purpose
- Provide reusable, deterministic compliance patterns for EU regulations.
- Enable pre-hoc compliance and regulator-verifiable evidence.
- Reduce fragmentation by offering shared technical building blocks.

## Pattern structure (draft)
Each pattern includes:
- Legal norm (atomic obligation)
- Pattern name and purpose
- Inputs/Outputs
- Runtime artefacts
- Evidence requirements
- Cross-regulation applicability

---

## Pattern 1 — Consent / Intent Token Pattern (CITP)
**Legal norm:** GDPR Art. 6–7, AI Act Art. 10, PSD3 transparency obligations. Processing requires explicit, informed, purpose-bound consent or authority.

**Purpose:** Externalise consent/intent as machine-readable artefacts, not UI interactions.

**Inputs:** Identity assertion, purpose taxonomy ID, validity period, legal basis.

**Outputs:** Signed consent token; included in execution envelope.

**Runtime artefact:** Token includes purpose, TTL, jurisdiction, policy snapshot hash.

**Evidence:** Token hash included in evidence bundle.

**Applicable across:** GDPR, PSD3/PSR, AI Act (transparency), eIDAS2, Data Act.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "token_id": { "type": "string" },
    "issuer": { "type": "string" },
    "subject": { "type": "string" },
    "purpose_id": { "type": "string" },
    "legal_basis": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "valid_from": { "type": "string", "format": "date-time" },
    "valid_to": { "type": "string", "format": "date-time" },
    "policy_snapshot_id": { "type": "string" },
    "signature": { "type": "string" }
  },
  "required": ["token_id", "issuer", "subject", "purpose_id", "legal_basis", "valid_from", "valid_to", "policy_snapshot_id", "signature"]
}
```

---

## Pattern 2 — Cryptographic Evidence Bundle Pattern (CEBP)
**Legal norm:** AI Act Arts. 12, 16, 20, 50; DORA; PSD3 auditability.

**Purpose:** Generate a deterministic cryptographic record of every regulated system action.

**Inputs:** Execution context, model/agent output, consent/intent token, policy snapshot.

**Outputs:** Merkle-rooted evidence bundle.

**Runtime artefact:** Hash chains, signature chain, audit replay metadata.

**Evidence:** Produces regulator-verifiable artefact.

**Applicable across:** AI Act, PSD3/PSR, DORA, NIS2, GDPR (Art. 30).

**ECS alignment:** Bundles MUST conform to `docs/evidence/export-schema.md`.

---

## Pattern 3 — Policy Snapshot Pattern (PSP)
**Legal norm:** AI Act high-risk requirements; GDPR accountability; PSD3 oversight.

**Purpose:** Provide deterministic evidence of rules applied during execution.

**Inputs:** Policy bundle version, legal requirement mapping.

**Outputs:** Policy snapshot ID.

**Runtime artefact:** Snapshot ID attached to all decision envelopes.

**Evidence:** Snapshot referenced in evidence bundles.

**Applicable across:** AI Act, PSD3/PSR, NIS2, GDPR, eIDAS2.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "policy_snapshot_id": { "type": "string" },
    "version": { "type": "string" },
    "hash": { "type": "string" },
    "issued_at": { "type": "string", "format": "date-time" },
    "issuer": { "type": "string" },
    "scope": { "type": "array", "items": { "type": "string" } },
    "ruleset_ref": { "type": "string" },
    "signature": { "type": "string" }
  },
  "required": ["policy_snapshot_id", "version", "hash", "issued_at", "issuer", "ruleset_ref", "signature"]
}
```

---

## Pattern 4 — Risk Rubric Pattern (RRP)
**Legal norm:** AI Act Annex III (high-risk), DORA operational risk, PSD3 fraud risk.

**Purpose:** Turn legal risk factors into weighted, machine-evaluated rubric.

**Inputs:** Risk factors, weighted criteria, thresholds.

**Outputs:** Risk score.

**Runtime artefact:** Included in execution envelope; fail-closed when thresholds unmet.

**Evidence:** Rubric calculations included in evidence for post-market monitoring.

**Applicable across:** AI Act, DORA, PSD3/PSR, NIS2.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "rubric_id": { "type": "string" },
    "version": { "type": "string" },
    "criteria": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "factor": { "type": "string" },
          "weight": { "type": "number" },
          "threshold": { "type": "number" }
        },
        "required": ["factor", "weight"]
      }
    },
    "score": { "type": "number" },
    "outcome": { "type": "string", "enum": ["accepted", "refused", "failed"] },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["rubric_id", "version", "criteria", "score", "outcome", "evidence_pointer"]
}
```

---

## Pattern 5 — Jurisdictional Routing Pattern (SCRP)
**Legal norm:** GDPR cross-border transfer rules; AI Act Art. 10; PSD3 jurisdiction.

**Purpose:** Ensure operations occur only through legally compliant routes.

**Inputs:** Jurisdiction token, corridor matrix, agent identity.

**Outputs:** Route approval or denial.

**Runtime artefact:** Jurisdiction token reference, corridor ID.

**Evidence:** Evidence bundle contains corridor proof.

**Applicable across:** GDPR transfers, PSD3, AI Act, DSA, Data Act.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "corridor_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "route": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "approval": { "type": "string", "enum": ["approved", "denied"] },
    "evidence_pointer": { "type": "string" },
    "signature": { "type": "string" }
  },
  "required": ["corridor_id", "jurisdiction", "route", "policy_snapshot_id", "approval", "evidence_pointer", "signature"]
}
```

---

## Pattern 6 — Duty Propagation Pattern (MDPP)
**Legal norm:** AI Act value chain obligations; PSD3 multi-party duties; DORA outsourcing.

**Purpose:** Split and track compliance duties across parties.

**Inputs:** Party list, duty weights, threshold crypto.

**Outputs:** Joint liability token.

**Runtime artefact:** Bound to execution envelope.

**Evidence:** Duty signatures included in evidence bundle.

**Applicable across:** AI Act, PSD3/PSR, DORA, NIS2.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "duty_token_id": { "type": "string" },
    "parties": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "party_id": { "type": "string" },
          "role": { "type": "string" },
          "duty_weight": { "type": "number" },
          "signature": { "type": "string" }
        },
        "required": ["party_id", "role", "duty_weight", "signature"]
      }
    },
    "threshold": { "type": "number" },
    "policy_snapshot_id": { "type": "string" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["duty_token_id", "parties", "threshold", "policy_snapshot_id", "evidence_pointer"]
}
```

---

## Pattern 7 — Witness Signature Pattern (optional)
**Legal norm:** High‑assurance auditability, disputed transactions, multi‑party attestations.

**Purpose:** Allow independent parties (witnesses/notaries) to co‑sign critical evidence bundles.

**Inputs:** Evidence bundle hash, witness identity, timestamp.

**Outputs:** Witness signature artifact linked to the bundle.

**Runtime artefact:** Additional signature records; does not alter primary evidence chain.

**Evidence:** Witness signatures included as optional artifacts in the export manifest.

---

## Pattern 7 — Evidence-Delta Pattern (EDP)
**Legal norm:** AI Act "substantial modification"; DORA change management; PSD3 updates.

**Purpose:** Provide cryptographic differences between policy/model versions.

**Inputs:** Old version, new version.

**Outputs:** Delta proof.

**Runtime artefact:** Version-delta record.

**Evidence:** Included in post-modification bundles.

**Applicable across:** AI Act, DORA, NIS2, cybersecurity.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "delta_id": { "type": "string" },
    "old_version": { "type": "string" },
    "new_version": { "type": "string" },
    "old_hash": { "type": "string" },
    "new_hash": { "type": "string" },
    "delta_hash": { "type": "string" },
    "artifact_type": { "type": "string", "enum": ["model", "policy", "dataset", "runtime"] },
    "issued_at": { "type": "string", "format": "date-time" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["delta_id", "old_version", "new_version", "old_hash", "new_hash", "delta_hash", "artifact_type", "issued_at", "evidence_pointer"]
}
```

---

## Pattern 8 — Usage Receipt Pattern (URP)
**Legal norm (contextual):** Data Act access conditions; PSD3 transparency; GDPR accountability (for lawful access records).

**Purpose:** Provide a neutral, evidence-grade usage record that can support billing, attribution, or revenue sharing without prescribing a business model.

**Inputs:** data product id, consumer id, purpose id, policy snapshot id, consent token ref.

**Outputs:** Usage receipt record.

**Runtime artefact:** Receipt bound to evidence bundle for the access event.

**Evidence:** Receipt included in evidence export bundles.

**Applicable across:** Data Act, GDPR accountability, sectoral data-space schemes.

**JSON schema snippet (draft):**
```json
{
  "type": "object",
  "properties": {
    "receipt_id": { "type": "string" },
    "data_product_id": { "type": "string" },
    "consumer_id": { "type": "string" },
    "purpose_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "consent_token_ref": { "type": "string" },
    "usage_quantity": { "type": "number" },
    "usage_unit": { "type": "string" },
    "occurred_at": { "type": "string", "format": "date-time" },
    "evidence_pointer": { "type": "string" }
  },
  "required": ["receipt_id", "data_product_id", "consumer_id", "purpose_id", "policy_snapshot_id", "occurred_at", "evidence_pointer"]
}
```

---

## Pattern → Invariant mapping (draft)
| Pattern | Primary invariant families | Evidence artifacts |
|---|---|---|
| CITP (Consent/Intent) | AUTH, POL, EVID, DATA | Consent token, token hash in bundle |
| CEBP (Evidence Bundle) | EVID, AUTH/POL, EXEC | Bundle manifest, chain segment, signatures |
| PSP (Policy Snapshot) | POL, AUTH, EVID | Policy snapshot id, snapshot artifact |
| RRP (Risk Rubric) | POL, EXEC, EVID | Risk rubric, score evidence |
| SCRP (Routing) | DATA, PHY, DEP, EVID | Corridor proof, jurisdiction token |
| MDPP (Duty Propagation) | AUTH, DEP, SUP, EVID | Duty token, joint signatures |
| EDP (Evidence-Delta) | EVID, SUP, EXEC | Delta proof, version hashes |

## Notes
- This library is a draft reference; patterns will evolve with delegated acts and standards work.
- Implementations SHOULD align to ECS invariants and evidence export schema.

## Versioning & governance (draft)
- **Host institutions:** DG CONNECT (policy alignment), JRC (technical stewardship), ENISA (security & integrity), optionally an EDIC.
- **Standardisation anchors:** CEN/CENELEC, ETSI, ISO/IEC, W3C, eIDAS expert groups.
- **Versioning model:** major versions align to new regulations; minor versions align to delegated acts; patch versions align to security/operational updates.
- **Conformance:** each pattern includes schema validation, evidence reproducibility, security/provenance checks, and cross‑law semantic consistency.
