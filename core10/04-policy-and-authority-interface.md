# Policy & Authority Interface — Placeholder

## Intent
Explicit decision points, escalation hooks, refusal semantics, and authority tracing.

## Invariant families (refs)
- AUTH (authority verification, refusal)
- POL (policy artifacts, deterministic evaluation)
- EVID (evidence of decisions/refusals)

## Scope and assumptions
- Applies to governed actions across planes (identity/control/execution/data).
- Uses invariant IDs from `docs/invariants-v0.3.md`; no new semantics introduced.

## Definitions (draft)
- Authority binding: verifiable link between a subject and an authority scope (who can do what, when).
- Policy snapshot: immutable, versioned policy artifact used for deterministic evaluation.
- Decision event: evidence record of allow/refuse/escalate with authority/policy context.

## Minimal interface surface (draft)
- Policy registry:
  - Submit policy artifact with metadata (version, hash, scope).
  - Retrieve policy snapshot by id/hash.
  - Deprecate/replace policy versions with an audit trail.
- Decision interface:
  - Evaluate governed action with inputs + policy snapshot id.
  - Return outcome + evidence pointer + snapshot ids.
- Evidence emission:
  - Emit decision/refusal/escalation events with authority/policy context.

## Authority binding schema (draft JSON)
```json
{
  "issuer": "authority.example",
  "subject": "tenant-123",
  "scope": ["workload.deploy", "data.export"],
  "valid_from": "2025-01-01T00:00:00Z",
  "valid_to": "2026-01-01T00:00:00Z",
  "proof": "sig-or-attestation-ref"
}
```

## Policy snapshot schema (draft JSON)
```json
{
  "policy_id": "pol-001",
  "version": "v1.2.3",
  "hash": "sha256:...",
  "created_at": "2025-01-01T00:00:00Z",
  "issuer": "policy-authority",
  "scope": ["workload.deploy", "tenant.update"],
  "ruleset_ref": "registry://policies/pol-001@v1.2.3"
}
```

## Refusal reasons (draft)
- `authority_invalid` / `authority_expired`
- `policy_missing` / `policy_invalid` / `policy_uncertain`
- `input_incomplete` / `scope_mismatch`
- `evidence_unavailable` (when evidence sink is required for the action)

## Decision event fields (draft)
- `event_type`, `timestamp`, `actor`, `tenant_id`, `action`
- `authority_snapshot_id`, `policy_snapshot_id`
- `outcome` (accepted/refused/failed), `refusal_reason` (if refused)
- `evidence_pointer`, `integrity` (hash/chain ref)

## Applicable invariant IDs
- AUTH-01/02/04/05, POL-01/02/03/04/05, EVID-01/03/04

## Evidence expectations
- Policy artifacts (versioned, provenance), authority bindings.
- Decision/refusal/escalation events with policy snapshot IDs.
- Deterministic evaluation traces for repeatability.

## Requirements (draft)
- Policy artifacts MUST be versioned, immutable, and have provenance (POL-01).
- Policy evaluation MUST be deterministic; same inputs produce same outcomes (POL-02).
- Authority MUST be verified before governed actions; refusals are first-class (AUTH-01/02/04/05).
- Exceptions MUST be explicit, time-bound, and evidence-backed; approvals recorded with authority/policy context.
- Interfaces MUST emit evidence for decisions/refusals/escalations, including policy snapshot and authority binding.
- Evaluation MUST be able to fail-closed on policy uncertainty (POL-04) and log refusal with evidence.

## Policy expression examples (non-normative)

### OPA/Rego
```rego
package ecs.authority

default allow = false

allow {
    input.authority_binding != ""
    not authority_expired(input.authority_binding)
    input.action == "deploy"
}

authority_expired(binding) {
    binding.expires_at < time.now_ns()
}
```

### Kyverno (Kubernetes admission)
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: ecs-authority-binding
spec:
  validationFailureAction: enforce
  rules:
    - name: require-authority
      match:
        resources:
          kinds: [Deployment, Pod]
      validate:
        message: "Authority binding required"
        pattern:
          metadata:
            annotations:
              ecs.io/authority-binding: "?*"
```

Examples are illustrative; any policy engine may be used if deterministic and auditable.

## Conformance outline (draft)
- Verify policy artifacts are versioned and referenced in decisions/refusals.
- Confirm authority checks occur before governed actions; refusals are logged with evidence.
- Test exception workflow: explicit approval with time bound and evidence; ensure defaults fail closed.
- Replay determinism: given identical inputs/policy snapshot, outcomes are identical; evidence captures snapshot ID.

## To cover
- How policy is expressed, evaluated, and enforced.
- Who can approve exceptions; how approvals are recorded as evidence.
- Refusal semantics and fail-closed behavior.

## Invariants (draft)
- Authority MUST be verified before execution of governed actions.
- Policy evaluation MUST be deterministic given a policy snapshot and inputs.
- Refusals and escalations MUST be first-class outcomes and logged as evidence.
- Exception approvals MUST be explicit, time-bounded, and evidence-backed.

## Next steps
- Define minimum API/interface expectations.
- Align with Evidence Event Model and Audit Chain Baseline.
