# SOC / Log Control Profile (Draft)

## Intent
Define minimum controls for log residency, access, integrity, and export to satisfy regional SOC and audit expectations.

## Scope
- Applies to security/audit logs and evidence streams for governed services.
- Focuses on residency, access control, and exportability; does not mandate a SIEM or vendor.

## Requirements (draft)
- **Log residency:** logs and evidence MUST be stored in declared jurisdictions.
- **Access control:** access to logs MUST be governed by policy/authority checks and least‑privilege.
- **Integrity:** logs MUST be integrity‑protected (hash chain and/or signatures).
- **Exportability:** logs and evidence MUST be exportable as bundles (`docs/evidence/export-schema.md`).
- **Timely access:** providers MUST supply access within stated SLAs for regulated workloads.
- **Retention:** retention periods MUST be enforced and evidenced.

## Evidence expectations
- Residency declarations and placement proof.
- Access control policies and audit trails.
- Integrity proofs (chain segments, anchor refs).
- Export bundles and retrieval logs.

## Conformance checklist (draft)
1. Logs stored within declared jurisdiction.
2. Access governed by policy snapshot and authority binding.
3. Integrity proofs available for log segments.
4. Export bundles produced on request.
5. Retention enforcement evidenced.
