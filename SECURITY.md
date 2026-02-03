# Security Policy (Draft)

## Threat model
- Adversarial providers or compromised control planes.
- Untrusted networks and partitions.
- Misconfigured or stale policy/authority caches.
- Malicious or flawed workloads seeking to bypass governance.

## Scope
In scope:
- Security issues in specifications, reference contracts, and evidence requirements that could enable bypass, forgery, or integrity failures.
- Vulnerabilities in scripts or tooling under `scripts/`.

Out of scope:
- Third‑party implementations not maintained in this repository.
- Operational incidents at external providers.

## Invariant enforcement
- **Authority-before-execution:** Prevents execution without explicit, validated authority (refusal/escalation are first-class).
- **CRP isolation:** Local authority/policy evaluation and control-plane independence during partition; deterministic degradation.
- **IALP evidence:** Immutable, ordered logs (authority, policy snapshot, inputs, decisions, outputs, refusals).
- **Governance metadata:** EOSC ensures jurisdiction/retention/integrity travel with data.

## Response expectations
- Acknowledge within 5 business days.
- Provide a remediation plan or status update within 20 business days, where feasible.

## Evidence handling
- If you provide evidence or proof‑of‑concept data, avoid submitting sensitive personal data.
- Evidence artifacts may be referenced in this project’s evidence model; we will treat submissions as confidential until disclosure is agreed.

## Vulnerability reporting
Report suspected security issues via GitHub Security Advisories (preferred for private disclosure). If you cannot use advisories, open a GitHub issue and label it `security`.

Please include: affected components/files, reproduction steps, and impact assessment if known. We will acknowledge receipt and coordinate a fix/response.
