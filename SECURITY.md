# Security Policy (Draft)

## Threat model
- Adversarial providers or compromised control planes.
- Untrusted networks and partitions.
- Misconfigured or stale policy/authority caches.
- Malicious or flawed workloads seeking to bypass governance.

## Invariant enforcement
- **Authority-before-execution:** Prevents execution without explicit, validated authority (refusal/escalation are first-class).
- **CRP isolation:** Local authority/policy evaluation and control-plane independence during partition; deterministic degradation.
- **IALP evidence:** Immutable, ordered logs (authority, policy snapshot, inputs, decisions, outputs, refusals).
- **Governance metadata:** EOSC ensures jurisdiction/retention/integrity travel with data.

## Vulnerability reporting
Report suspected security issues privately to: security@lane2.tech

Please include: affected components/files, reproduction steps, and impact assessment if known. We will acknowledge receipt and coordinate a fix/response.
