# Minimal Metrics (Draft)

These metrics provide a compact, repeatable way to quantify DEP/SUP/OPS/PHY posture. They are intended for trend monitoring and cross‑provider comparison, not certification.

## DEP (Dependency)
- **Critical path concentration (%)**: share of critical services dependent on a single actor.
- **Non‑substitutable count**: number of dependencies marked non‑substitutable.
- **Exception rate**: number of exclusivity exceptions per period.

## SUP (Supply‑chain)
- **SBOM coverage (%)**: critical components with SBOM entries.
- **Provenance coverage (%)**: critical artifacts with verifiable provenance.
- **Upstream disclosure rate (%)**: N‑tier dependencies disclosed for critical paths.

## OPS (Operations)
- **Runbook coverage (%)**: critical services with current runbooks.
- **Role redundancy index**: ratio of critical operations with >=2 qualified roles.
- **Drill frequency**: number of operational drills per year.

## PHY (Connectivity)
- **Single‑path exposure (%)**: critical services with single‑path/operator dependency.
- **Partition test frequency**: number of partition drills per year.
- **Connectivity evidence freshness**: age of last topology snapshot or test.
