# Interim Coherence Report (Draft)

Date: 2026-02-28

## Purpose
This report tracks the current ECS position against the primary adoption blocker:
EU cloud alternatives are available, but buyers still choose AWS for operating coherence (one consistent model across identity, deployment, observability, and automation).

## Current maturity snapshot

### 1) Contract and architecture maturity: **Strong**
- Core contract shape is now clear (Core10 + profiles + evidence export/verifier).
- Deployment portability baseline exists: `docs/deployment-profile.md`.
- Federation and refusal-evidence expectations are documented.

### 2) Provider comparison maturity: **Medium**
- EU provider selection matrix is in place with weighted criteria and must-pass gates:
  `docs/mappings/eu-cloud-provider-selection-matrix.md`.
- Ops parity extension (DNS/certs/observability/LB/OpenShift/network) is defined.
- Current scores are mostly docs-based and low confidence until PoC artifacts are collected.

### 3) Automation maturity (agent/operator UX): **Medium-Low**
- A provider-by-provider CLI/API/IaC surface has been documented.
- A v0 non-interactive smoke-test command set exists for auth + k8s + object storage + logging.
- Execution harness and repeatable score capture are not yet implemented as scripts/pipeline.

### 4) Procurement narrative maturity: **Strong**
- RFP and checklist materials exist and are aligned to evidence profiles.
- Positioning now explains that ECS is a substrate contract, not a cloud platform.

## Top 3 risks (next 30 days)

### R1 — Identity and workload-auth coherence gap
Even where CLI/API exists, workload identity patterns are inconsistent across providers.
This is the largest practical gap versus AWS-style operator experience.

Impact:
- Non-interactive automation can stall.
- Cross-provider deployment profile reproducibility degrades.

### R2 — Ops parity gap in DNS/certs/LB/observability integration
Feature presence is not enough; teams need one coherent operational loop.
Partial parity here drives fallback to AWS despite sovereign intent.

Impact:
- Higher operational toil.
- Slower incident response and reduced confidence in migration.

### R3 — Evidence path drift under managed-service differences
Without strict test artifacts, providers can look equivalent on paper but differ in evidence export, retention, and refusal traceability behavior.

Impact:
- Audit/procurement claims become weak.
- Exit and verification guarantees are harder to prove.

## 30-day execution plan (coherence-first)

### Week 1 — Build runnable PoC harness
Actions:
- Convert matrix smoke tests into versioned scripts (`scripts/poc/`), one runner per provider.
- Standardize output artifact structure under:
  `artifacts/provider-poc/<provider>/<date>/`.
- Add a simple score-capture template linked to artifact paths.

Pass criteria:
- Every provider has runnable auth/k8s/object-storage/logging checks with non-interactive auth.
- Each check writes machine-readable output and exit status.

Fail criteria:
- Any provider cannot run non-interactively for core checks.
- Outputs are not reproducible across two consecutive runs.

### Week 2 — Validate ops parity critical path (O1/O2/O4 first)
Actions:
- Execute DNS/traffic, certificate lifecycle, and LB/ingress checks first.
- Run one controlled refusal scenario (jurisdiction/policy-driven deny) and capture evidence.

Pass criteria:
- For each shortlisted provider, O1/O2/O4 all score >= 3 with test artifacts.
- At least one provider reaches O1/O2/O4 >= 4 on two of three dimensions.

Fail criteria:
- Missing automation path for DNS or cert lifecycle.
- No reproducible refusal evidence at ingress/routing boundary.

### Week 3 — Evidence and export verification loop
Actions:
- Run ECS evidence generation and export bundle flow on shortlisted providers.
- Validate verifier input completeness and chain continuity on exported bundle.

Pass criteria:
- Export bundle validates without provider-internal dependencies.
- Profile claim + hash/profile metadata + verifier inputs are complete.

Fail criteria:
- Bundle requires provider-specific hidden context to verify.
- Chain/pointer/profile artifacts are incomplete.

### Week 4 — Selection decision and risk controls
Actions:
- Final scoring pass with artifact-backed C1-C7 and O1-O6.
- Publish decision record with known gaps and compensating controls.
- Define quarterly re-test cadence.

Pass criteria:
- One primary provider satisfies must-pass gates.
- `substrate_total >= 75`, `ops_total >= 70`, and no critical fail in O1/O2/O4.

Fail criteria:
- No provider meets threshold with evidence-backed scores.
- Decision cannot be justified with reproducible artifacts.

## Decision framing (recommended)
Use a two-lane operating model:
- **Production lane:** one EU primary provider chosen by coherence + evidence criteria.
- **Velocity lane:** AWS allowed for rapid dev/test, but with mandatory ECS export portability checks.

This keeps delivery speed while preventing lock-in and preserving sovereign controls.

## Immediate next actions
1. Implement `scripts/poc/` automation harness from the smoke-test section.
2. Run Week 1 checks for three shortlisted providers first.
3. Publish first artifact-backed scorecard update within 7 days.
