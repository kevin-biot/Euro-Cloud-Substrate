# Agent Delegation (Draft)

## Purpose
Clarify how ECS treats agents, delegation, and accountability. This is meant to prevent “agent ID” confusion and encourage safe, auditable delegation practices.

## Core principle
**Agents are delegates, not legal principals.**  
Accountability remains with the delegator (human or organization). Agents do not “own” authority; they operate under a scoped, time‑bounded delegation.

## Access layer ≠ governance (context)
Making systems “accessible” to agents is not the same as **governed access**.  
ECS requires that every delegated action is bound to authority/policy snapshots and produces refusal evidence when obligations cannot be met.

## Minimal identity model
Use **four identifiers** to avoid ambiguity:
- **delegation_id** — the grant (who delegated, scope, time bounds, intent).
- **agent_class_id** — the logical agent type/capability (e.g., `invoice-processor-v3`).
- **agent_instance_id** — the runtime instance (e.g., container/worker id).
- **session_id** — a single execution session (rotates frequently).

**Why this matters:** one agent class may have thousands of instances, each with multiple sessions.

## Delegation proof (what must be evidenced)
Delegation proof should bind:
- **delegator_id** (human/org)
- **agent_class_id**
- **scope** (allowed actions)
- **valid_from / valid_to**
- **intent_ref / purpose_id** (when governed actions require explicit intent)
- **policy_snapshot_id / authority_snapshot_id**

Delegation MUST be **revocable**, and revocation should not require the delegator’s participation at runtime.

## Authentication vs authorization (agents)
- **Authentication**: the agent instance proves it is acting under a delegation (token/credential proof).
- **Authorization**: policy decides whether the delegated scope is allowed for the requested action.

Agents should not be issued “permanent” identities; delegation is always scoped and time‑bounded.

## Token expectations (portable baseline)
For OIDC/OAuth tokens used by agents, include:
- `delegation_id`
- `agent_class_id`
- `agent_instance_id`
- `session_id`
- `scope`
- `exp` (expiry)
- `actor_type=delegate`

## Evidence events (where it shows up)
Use delegation events to prove scope and intent:
- `wallet.delegation.issue`
- `wallet.delegation.revoke`

Event payloads SHOULD include the identifiers above, plus intent/purpose where applicable.

## Common failure modes (what to avoid)
- **Treating agents as legal principals** (“agent ID” without a delegator).
- **Permanent delegation** (no expiry or scope).
- **Missing instance/session identity** (no audit trail at runtime scale).
- **No intent binding** when actions require explicit purpose.

## Mapping to ECS docs
- IAM domain: `docs/domains/iam.md`
- EUDI wallet integration: `docs/domains/eudi-wallet-integration.md`
- Evidence catalog (delegation events): `docs/evidence/catalog.md`
