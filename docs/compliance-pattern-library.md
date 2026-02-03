# EU Compliance Pattern Library (Draft, Non-Normative)

Supporting reference patterns for translating legal obligations into runtime-enforceable, evidence-generating design primitives. This draft is intended to guide architecture review and future standardisation work; it is not a binding standard.

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

---

## Pattern 2 — Cryptographic Evidence Bundle Pattern (CEBP)
**Legal norm:** AI Act Arts. 12, 16, 20, 50; DORA; PSD3 auditability.

**Purpose:** Generate a deterministic cryptographic record of every regulated system action.

**Inputs:** Execution context, model/agent output, consent/intent token, policy snapshot.

**Outputs:** Merkle-rooted evidence bundle.

**Runtime artefact:** Hash chains, signature chain, audit replay metadata.

**Evidence:** Produces regulator-verifiable artefact.

**Applicable across:** AI Act, PSD3/PSR, DORA, NIS2, GDPR (Art. 30).

**ECS alignment:** Bundles MUST conform to `docs/evidence-export-schema.md`.

---

## Pattern 3 — Policy Snapshot Pattern (PSP)
**Legal norm:** AI Act high-risk requirements; GDPR accountability; PSD3 oversight.

**Purpose:** Provide deterministic evidence of rules applied during execution.

**Inputs:** Policy bundle version, legal requirement mapping.

**Outputs:** Policy snapshot ID.

**Runtime artefact:** Snapshot ID attached to all decision envelopes.

**Evidence:** Snapshot referenced in evidence bundles.

**Applicable across:** AI Act, PSD3/PSR, NIS2, GDPR, eIDAS2.

---

## Pattern 4 — Risk Rubric Pattern (RRP)
**Legal norm:** AI Act Annex III (high-risk), DORA operational risk, PSD3 fraud risk.

**Purpose:** Turn legal risk factors into weighted, machine-evaluated rubric.

**Inputs:** Risk factors, weighted criteria, thresholds.

**Outputs:** Risk score.

**Runtime artefact:** Included in execution envelope; fail-closed when thresholds unmet.

**Evidence:** Rubric calculations included in evidence for post-market monitoring.

**Applicable across:** AI Act, DORA, PSD3/PSR, NIS2.

---

## Pattern 5 — Jurisdictional Routing Pattern (SCRP)
**Legal norm:** GDPR cross-border transfer rules; AI Act Art. 10; PSD3 jurisdiction.

**Purpose:** Ensure operations occur only through legally compliant routes.

**Inputs:** Jurisdiction token, corridor matrix, agent identity.

**Outputs:** Route approval or denial.

**Runtime artefact:** Jurisdiction token reference, corridor ID.

**Evidence:** Evidence bundle contains corridor proof.

**Applicable across:** GDPR transfers, PSD3, AI Act, DSA, Data Act.

---

## Pattern 6 — Duty Propagation Pattern (MDPP)
**Legal norm:** AI Act value chain obligations; PSD3 multi-party duties; DORA outsourcing.

**Purpose:** Split and track compliance duties across parties.

**Inputs:** Party list, duty weights, threshold crypto.

**Outputs:** Joint liability token.

**Runtime artefact:** Bound to execution envelope.

**Evidence:** Duty signatures included in evidence bundle.

**Applicable across:** AI Act, PSD3/PSR, DORA, NIS2.

---

## Pattern 7 — Evidence-Delta Pattern (EDP)
**Legal norm:** AI Act "substantial modification"; DORA change management; PSD3 updates.

**Purpose:** Provide cryptographic differences between policy/model versions.

**Inputs:** Old version, new version.

**Outputs:** Delta proof.

**Runtime artefact:** Version-delta record.

**Evidence:** Included in post-modification bundles.

**Applicable across:** AI Act, DORA, NIS2, cybersecurity.

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
