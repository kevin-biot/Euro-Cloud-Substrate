# EUDI Wallet Integration (Draft, Non-Normative)

## Intent
Describe minimum platform capabilities for integrating with EUDI wallets without prescribing specific vendors or device roots of trust.

## Scope
- Applies to identity/authority verification for governed actions.
- Covers both human users and delegated agentic workloads.
- Root of trust is implementation‑agnostic (device SE, eSIM, hardware token, HSM).

See `docs/domains/iam.md` for the broader IAM domain mapping and baseline capabilities.
See `docs/guides/agent-delegation.md` for delegation concepts, identifiers, and evidence guidance.

## Minimum platform capabilities
- **Credential verification interface**: verify credential signatures and validity.
- **Proof‑of‑possession validation**: ensure credential holder controls the presented key.
- **Revocation/validity checks**: offline/online checks with evidence.
- **Evidence emission**: emit events that bind credential verification to policy snapshots.
- **Exportability**: evidence events must be exportable per `docs/evidence/export-schema.md`.

## Evidence fields (draft)
- `credential_id` or hash
- `proof_type` (device_se | esim | token | hsm | other)
- `policy_snapshot_id`
- `authority_snapshot_id`
- `outcome` (accepted/refused/failed)
- `evidence_pointer`

## Delegation for agentic workloads (draft)
- Support **organizational wallets** and **delegated credentials** for agents.
- Delegation MUST be time‑bounded, scoped, and evidenced.
- Delegation SHOULD bind to the delegator’s intent (purpose/intent reference) and be revocable without delegator participation.
- Agent actions MUST bind to delegated credential proofs and policy snapshots.
- Delegation credentials MAY be Verifiable Credentials (DID/VC) presented via OAuth/OIDC token exchange (on‑behalf‑of).
 - vLEI credentials MAY be used to prove organizational identity and roles for delegation.

## Agentic delegation and payment binding (draft)
- Delegation SHOULD include scope, time window, and permitted payment/usage policies.
- Usage receipts SHOULD bind to delegated credential id and payment reference.
- Evidence MUST be exportable to show who acted, under what authority, and under what payment terms.

## Notes
- This document does not prescribe wallet vendors or device implementations.
- ECS requires evidence, not a specific root of trust.
