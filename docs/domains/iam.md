# IAM Domain (Draft, Non‑Normative)

## Purpose
Define the Identity & Access Management (IAM) domain across the cloud‑edge continuum, focusing on **who can act**, **under what authority**, and **with what proof**—without prescribing a specific IAM product.

## Capabilities (baseline)
- **Decentralized identity (DID)** and verifiable credentials
- **Verifiable Legal Entity Identifier (vLEI)** credentials for organizational identity (optional)
- **Role‑based access control (RBAC)** and least‑privilege scoping
- **Zero Trust Architecture (ZTA)** posture (verify explicitly, fail closed)
- **Multi‑factor authentication (MFA)** / biometrics (credential strength signals)
- **Identity federation** (OAuth 2.0 / OpenID Connect)

## Authentication vs authorization (clarification)
- **Authentication (authn)** verifies *who* is acting (credential proof, signature, issuer).
- **Authorization (authz)** decides *what* the actor may do (policy + authority scope).
- Delegated actions MUST be both authenticated (delegation proof) and authorized (policy + scope).

## Token‑based federation (OAuth/OIDC/JWT)
- **Required baseline claims**: `iss`, `sub`, `aud`, `exp`, `iat`.
- **Recommended claims**: `org_id`, `tenant_id`, `roles`/`groups`, `jurisdiction`.
- **Validation evidence** MUST record signature validation, issuer allowlist, audience, and expiry checks.
- **Delegation context** for agents MUST be time‑bounded and scoped:
  - include `delegation_id`, `scope`, and expiry (`exp`/`valid_to`);
  - include `actor_type=delegate` and **intent/purpose reference** when governed actions require explicit intent.
  - include `agent_class_id`, `agent_instance_id`, and `session_id` for large‑scale agent deployments.

OAuth/OIDC is the baseline for API access; DID/VC‑based credentials MAY be used as proof of authority or identity without mandating a specific DID method.

## ECS mapping (no new semantics)
- **Core10‑04 Policy & Authority Interface** — authority binding, policy evaluation, refusal evidence.
- **Core10‑01 OLZ‑EU** — tenant authority binding, default‑deny posture at landing zone.
- **Core10‑09 Fail‑Closed Profile** — explicit refusal on missing/invalid authority or policy.
- **WS4 Interop API** — OIDC/mTLS expectations for federation and authn/z.
- **EUDI wallet integration note** — credential verification, delegation, evidence hooks.

## Evidence expectations (IAM‑grade)
- **Authority snapshots** referenced in every governed action.
- **Policy decisions** logged with outcome + snapshot id.
- **Credential verification events** (e.g., wallet.credential.verify) with proof type and evidence pointers.
- **Delegation events** (issue/revoke) for agent or service delegation.
- **Delegation scope + time bounds** MUST be evidenced; intent/purpose references SHOULD be captured when applicable.
 - vLEI credentials MAY be used as authority‑binding proofs for organizational identity.

## Notes
ECS defines **the contract** (evidence + authority binding), not the IAM implementation. Partners can adopt different IAM stacks as long as they emit the required evidence and support federation requirements.
