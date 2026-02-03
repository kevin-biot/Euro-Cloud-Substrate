# No‑Control Profile (NCP) — Draft (Non‑Normative)

## Intent
Define a portable profile for integrators or service partners to demonstrate **absence of possession, custody, or control** over customer systems and data.

## Core conditions (system invariants)
1. **No possession** — the integrator does not hold customer data at rest or in transit outside customer‑controlled execution envelopes.
2. **No custody** — the integrator cannot administer or operate without explicit, time‑bound delegation.
3. **No control** — the integrator cannot reconfigure, redeploy, or extract data via control‑plane APIs.

## Required evidence artifacts (examples)
- **Authority graph**: explicit mapping of who can assume which roles and how.
- **Key custody proof**: evidence that keys are generated and controlled outside integrator reach.
- **Control‑plane ownership**: proof that root identities and policy snapshots are customer‑owned.
- **Telemetry exclusion**: evidence of absence of out‑of‑band replication or “phone‑home” control paths.
- **Delegation logs**: all integrator access is time‑bounded, scoped, and revocable.

## Evidence events (examples)
- `authority.graph.publish`
- `key.custody.declare`
- `controlplane.ownership.declare`
- `telemetry.path.audit`
- `delegation.access.grant` / `delegation.access.revoke`

## Subpoena pressure‑test (illustrative)
**Scenario:** A foreign subpoena demands customer data from an integrator.  
**Expected outcome:** The integrator demonstrates **inability** (not refusal) using ECS evidence:
- No storage endpoints under integrator authority.
- No key custody or escrow.
- No control‑plane privilege or escalation path.
- Delegation required for any access, with revocation independent of integrator.

## Notes
This profile is non‑normative and may be adopted by any integrator to demonstrate structural inability to access or control customer data.
