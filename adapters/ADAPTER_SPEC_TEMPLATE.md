# ECS Adapter Spec Template (Draft)

## 1. Overview
- **Adapter name:**
- **Target system:**
- **Purpose:** What governance/evidence gap does this adapter close?
- **Scope:** What it does and does not do.

## 2. ECS alignment
- **Core10 references:** (e.g., Core10‑05 Evidence Event Model)
- **Invariant families:** AUTH / POL / EVID / DATA / EXEC / INT / EXIT / DEP / SUP
- **Evidence profile(s):** baseline / admissible / regulated‑ML / NCP (as applicable)

## 3. Inputs
- Required inputs (e.g., policy_snapshot_id, authority_snapshot_id)
- Optional inputs (e.g., hash_profile_id, jurisdiction, classification)
- Configuration sources (env vars, annotations, config file)

## 4. Evidence emission
- **Event types** (enumerate)
- **Required fields** (Core10‑05 + adapter‑specific)
- **Refusal semantics** (what causes refusal; how it’s evidenced)
- **Correlation model** (correlation_id, delegation_id, session_id)
- **Artifacts** (what snapshots or proofs are referenced)

## 5. Export behavior
- **Export format:** evidence bundle + manifest + verifier inputs
- **Integrity:** chain_id, event_hash, prev_hash
- **Evidence pointer contract:** immutability, tenant scoping, retrievability

## 6. Security & trust
- Authentication/authorization expectations
- Trust anchors / authority snapshots
- Delegation controls (TTL, scope, revocation)

## 7. Deployment & ops
- Deployment model (sidecar, webhook, daemonset, service)
- Failure modes (fail‑closed vs fail‑open)
- Performance considerations

## 8. Minimal examples
- **Request/trigger** example
- **Evidence event** example
- **Refusal event** example

## 9. Conformance checklist
- Must emit Core10‑05 envelope
- Must export evidence bundle
- Must declare evidence profile
- Must emit refusal evidence

## 10. Non‑goals
- Explicitly list what this adapter will not handle
