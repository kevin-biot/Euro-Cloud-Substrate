# Core 10 Components (Draft v1)

Each component will gain a spec, invariants, and a conformance outline. Invariants reference the authoritative list in `docs/invariants/v0.3.md`; no new semantics are defined here.

1. `01-open-landing-zone-profile.md` — tenant bootstrap flow, authority binding, default-deny posture, network/egress controls, evidence requirements.
2. `02-tenant-isolation-contract.md` — isolation domains (compute/storage/network/logs), cross-tenant access policy, and verification evidence.
3. `03-object-storage-contract-eosc.md` — EOSC governance metadata, retention/immutability rules, and evidence for object operations.
4. `04-policy-and-authority-interface.md` — minimal policy/authority interfaces, schemas, refusal taxonomy, and decision event fields.
5. `05-evidence-event-model.md` — event envelope, canonical event types, schema fields, export expectations, EU AI Act alignment.
6. `06-audit-chain-baseline.md` — hash-linked chain model, segment schema, verification steps, EU AI Act alignment.
7. `07-execution-envelope-profiles.md` — envelope selection rules and container/VM/TEE control expectations with attestation evidence.
8. `08-interop-api-surface.md` — minimum resources, auth model, error format, versioning, and pagination rules.
9. `09-compliance-fail-closed-profile.md` — fail-closed triggers, buffering/reconciliation rules, and recovery evidence.
10. `10-migration-baseline.md` — migration phases, export/import validation gates, and package/evidence expectations.
