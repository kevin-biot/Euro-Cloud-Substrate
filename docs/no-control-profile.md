# No‑Control Profile (NCP) — Draft (Non‑Normative)

## Intent
Define a portable profile for integrators or service partners to demonstrate **absence of possession, custody, or control** over customer systems and data.

## Context
This profile is particularly relevant where integrators or managed‑service partners may be subject to **non‑EU judicial or administrative orders** (e.g., foreign subpoenas or intelligence requests). The goal is to demonstrate **operational inability**, not contractual refusal.

## Core conditions (system invariants)
1. **No possession** — the integrator does not hold customer data at rest or in transit outside customer‑controlled execution envelopes.
2. **No custody** — the integrator cannot administer or operate without explicit, time‑bound delegation.
3. **No control** — the integrator cannot reconfigure, redeploy, or extract data via control‑plane APIs.

## Required evidence artifacts (examples)
- **Authority graph**: machine‑checkable mapping of who can assume which roles and how.
- **Key custody proof**: artifact showing keys are generated and controlled outside integrator reach.
- **Control‑plane ownership**: artifact proving root identities and policy snapshots are customer‑owned.
- **Telemetry exclusion**: audited egress map showing absence of out‑of‑band replication or “phone‑home” control paths.
- **Delegation logs**: all integrator access is time‑bounded, scoped, and revocable.

## Evidence events (examples)
- `authority.graph.publish`
- `key.custody.declare`
- `controlplane.ownership.declare`
- `telemetry.path.audit`
- `delegation.access.grant` / `delegation.access.revoke`

Each “declare”/“publish” event is expected to **reference a verifiable artifact** (e.g., authority graph, custody model, ownership map, telemetry egress map) via an artifact reference and hash, not just a statement.

### NCP event example (snippet)
```json
{
  "event_type": "authority.graph.publish",
  "subject_id": "integrator-123",
  "artifact_type": "authority_graph",
  "artifact_ref": "eosc://artifacts/authority-graph-001",
  "artifact_hash": "sha256:...",
  "evidence_pointer": "eosc://evidence/evt-123"
}
```
Export bundles that contain NCP events MUST declare `evidence_profile_id: ecs-evidence-ncp` in their manifest.

## Subpoena pressure‑test (illustrative)
**Scenario:** A foreign subpoena demands customer data from an integrator.  
**Expected outcome:** The integrator demonstrates **inability** (not refusal) using ECS evidence:
- No storage endpoints under integrator authority.
- No key custody or escrow.
- No control‑plane privilege or escalation path.
- Delegation required for any access, with revocation independent of integrator.

## Notes
This profile is non‑normative and may be adopted by any integrator to demonstrate structural inability to access or control customer data.
