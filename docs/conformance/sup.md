# SUP Conformance Checklist (Draft)

## Required evidence
- SBOMs or equivalent inventories for critical components.
- Provenance attestations for builds and artifacts.
- N‑tier dependency disclosure for critical paths.

## Minimal tests (pass/fail)
1. **SBOM coverage:** critical components have SBOM entries.
2. **Provenance verifiable:** attestation exists for critical artifacts.
3. **Opaque dependency fails:** missing upstream disclosure fails conformance.
4. **Exportable evidence:** SBOM/provenance artifacts are exportable.
5. **Change tracking:** supply‑chain updates generate evidence events.
