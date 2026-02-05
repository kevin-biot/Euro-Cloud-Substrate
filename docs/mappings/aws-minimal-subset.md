# AWS Minimal Subset Mapping (Draft, Non‑Normative)

## Purpose
Provide a small, concrete mapping example that shows how ECS “contract” semantics (authority, policy, evidence, portability) can be layered over AWS’s **service‑specific APIs** without attempting to mirror the entire AWS surface.

This is **mechanism‑only**: it does not define compliance, certification, or endorsement.

## Scope (minimal subset)
- **IAM** (authority + policy)
- **STS** (delegation)
- **S3** (data/object operations)
- **CloudTrail** (audit/event source)

## Mapping summary (illustrative)
| AWS source | ECS mapping | Evidence expectation | Notes / gaps |
|---|---|---|---|
| IAM role + policy version | `authority_snapshot_id` | Authority snapshot artifact attached to evidence pointer | Portability limited: AWS policy model is provider‑specific |
| IAM policy evaluation | `policy_snapshot_id` + decision outcome | Evidence event must include policy snapshot and outcome | Policy semantics are not portable without a mapping layer |
| STS AssumeRole | `delegation_id`, `delegator_id`, `scope`, `expiry` | Emit delegation events + link to authority snapshot | Maps cleanly to ECS delegation expectations |
| S3 object ops | `object.put/delete/copy/replicate` events | Evidence must include governance metadata where available | Storage governance headers are AWS‑specific |
| CloudTrail events | Core10‑05 envelopes | Events transformed to ECS envelope; chain fields added | CloudTrail is post‑hoc; ECS prefers pre‑hoc evidence |

## Example transform (conceptual)
CloudTrail `PutObject` (success) →
```json
{
  "event_type": "object.put",
  "outcome": "accepted",
  "authority_snapshot_id": "iam:role/MediaWriter@v3",
  "policy_snapshot_id": "iam:policy/MediaPolicy@v7",
  "evidence_pointer": "cloudtrail://trail/region/event-id",
  "tenant_id": "tenant-123"
}
```

CloudTrail `PutObject` (AccessDenied) →
```json
{
  "event_type": "object.put",
  "outcome": "refused",
  "refusal_reason": "AccessDenied",
  "authority_snapshot_id": "iam:role/MediaWriter@v3",
  "policy_snapshot_id": "iam:policy/MediaPolicy@v7",
  "evidence_pointer": "cloudtrail://trail/region/event-id",
  "tenant_id": "tenant-123"
}
```

## Minimal export flow (ECS‑aligned)
1. Ingest CloudTrail events for the tenant scope.  
2. Transform each event to Core10‑05 envelope.  
3. Add chain fields (`chain_id`, `event_hash`, `prev_hash`) based on canonicalized JSON.  
4. Emit an evidence bundle with `evidence_profile_id` and verifier inputs.  

## Gaps ECS exposes (not AWS defects)
- **Post‑hoc evidence**: CloudTrail captures after the fact; ECS targets decision‑time evidence.
- **Policy portability**: IAM policy semantics are not portable; ECS requires a mapping layer.
- **Refusal semantics**: AccessDenied is coarse; ECS expects structured refusal reasons where possible.
- **Export contract**: AWS does not define an evidence export bundle; ECS provides the bundle schema.

## What ECS expects for stronger claims
To claim **ECS baseline**:
- Evidence bundle export with Core10‑05 envelopes.
- Declared `evidence_profile_id` in manifests.
- Refusal evidence mapped from AccessDenied events.

To claim **ECS admissible** (or stronger):
- Pre‑hoc decision evidence (policy/authority) where feasible.
- Chain integrity and verifier inputs.
- Evidence pointer guarantees (immutability, tenant scoping).

## Why this mapping matters
It demonstrates that ECS coherence can be built **on top of fragmented APIs** by:
- unifying authority + policy context,
- standardizing evidence semantics,
- and exporting portable bundles for audits and exits.
