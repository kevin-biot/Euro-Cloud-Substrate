# Sovereignty Assurance Surface (Draft, Non-Normative)

## Purpose
Define a minimal assurance surface for "sovereignty" claims so implementations can be audited on enforceable control, not marketing language.

This note does not add new ECS semantics. It clarifies what evidence should be present when providers claim sovereign operation.

## Five assurance surfaces

### 1) Legal authority chain
Implementations should be able to show who has legal authority over data and control actions at each layer:
- controller/processor/subprocessor mapping
- governing law and dispute venue references
- authority boundaries by tenant and jurisdiction

Expected evidence:
- authority map artifact (versioned, immutable reference)
- policy snapshot references used at decision time

### 2) Compelled disclosure handling
Implementations should show how legal demand events are handled and constrained:
- what classes of request can be accepted or refused
- what disclosures are technically possible
- what refusals are enforced when policy or jurisdiction disallows action

Expected evidence:
- legal-demand handling artifact (decision classes + constraints)
- refusal events with policy/authority snapshot references

### 3) Trust-root provenance
Implementations should declare where trust originates for identity, certificates, and keys:
- IdP ownership and jurisdiction
- CA/KMS ownership and key custody model
- control holders for break-glass or emergency override paths

Expected evidence:
- trust-root declaration artifact
- key custody artifact (especially for NCP claims)
- telemetry/audit trail for trust-root and key lifecycle changes

### 4) Non-human identity and delegation controls
Implementations should treat service and agent identities as first-class governed actors:
- delegation must be scoped, time-bounded, revocable
- actor class vs actor instance should be distinguishable
- delegated actions should remain attributable to delegator and delegate

Expected evidence:
- delegation issue/revoke events
- delegated execution events with scope and expiry context
- refusal events when delegation is missing, expired, or out of scope

### 5) Commercial/control-plane ownership metadata
Implementations should make control-relevant ownership visible:
- contract/control-plane ownership declarations
- billing/operating entity references where authority is impacted
- explicit distinction between hosting location and control location

Expected evidence:
- control-plane ownership declaration artifact
- dependency/exit artifacts showing who operates critical control paths

## Profile and conformance integration
- Evidence profile selection remains mandatory in exports/manifests (`evidence_profile_id`).
- Stronger profiles (for example NCP or regulated-ML) should tighten required evidence for one or more assurance surfaces.
- Conformance claims should reference which assurance artifacts are provided and where they can be independently verified.

See:
- `docs/profiles/evidence-profiles.md`
- `docs/profiles/no-control-profile.md`
- `docs/conformance/model.md`
- `docs/evidence/verifier-responsibilities.md`

## Verifier expectations (minimum)
An independent verifier should be able to:
- resolve declared authority/trust artifacts without provider-private access
- confirm immutability/integrity of referenced artifacts
- validate refusals and decisions against declared policy/authority snapshots
- detect mismatches between declared profile and emitted evidence

## Non-goals
- No certification regime is defined here.
- No specific IAM/KMS/vendor product is mandated.
- No legal opinion is provided; this is an evidence and architecture clarity aid.
