# EU Regulatory Mapping (Context, Non-Normative)

ECS does not encode specific regulations. It provides enforceable primitives (authority-before-execution, fail-closed posture, evidence-by-construction, isolation, data governance, CRP resilience) that help satisfy multiple EU obligations. This mapping is indicative and should be maintained as regulations evolve.

## AI Act (traceability, risk, refusal)
- Traceability/logging: IALP primitives (authority assertion, policy snapshot, input/context hashes, decision/refusal logs, temporal ordering).
- Refusal semantics: Core invariant (fail-closed) + CRP-7 explicit refusal.
- Governance: Authority-before-execution and policy determinism.

## NIS2 / DORA (resilience, evidence)
- Resilience/continuity: CRP (local authority/policy, control-plane independence, deterministic degradation).
- Evidence: WS5 (evidence/audit), hash chaining, provider-neutral exports.
- Isolation and segmentation: WS1/WS3 + Tenant Isolation Contract.

## PSD3 (authority, auditability)
- Strong authority/authentication: Authority-before-execution, Policy & Authority Interface.
- Evidence of decisions: IALP decision logs, audit chain.
- Network/policy controls: OLZ-EU baseline and fail-closed posture.

## Data governance / sovereignty
- Data residency and metadata: EOSC metadata (jurisdiction/retention/integrity), CRP-4 for in-jurisdiction continuity.
- Portability: Migration baseline and Interop API Surface.

## Notes
- Use this as context for spec authors; do not turn regulations into invariants.
- Keep mappings updated as regulations and guidance evolve.
- IRN crosswalk (draft): see `docs/irn-mapping.md`.
