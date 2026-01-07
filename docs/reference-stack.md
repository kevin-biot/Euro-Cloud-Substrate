# Reference Stack Blueprint (Placeholder)

Non-normative. To be developed in Phase 2 after specs are stable. Purpose: show one OSS-based way to satisfy ECS invariants while allowing component swaps.

## Goals
- Map Core 10, CRP, and IALP invariants to OSS components and configurations.
- Provide swappable building blocks; avoid lock-in to specific vendors.
- Demonstrate manifests/policies that pass conformance tests.

## Candidate components (illustrative, not mandated)
- Control/landing: Kubernetes baseline with admission controls (e.g., Gatekeeper/Kyverno), network policy/egress controls.
- GitOps: ArgoCD or equivalent for declarative drift detection and signed manifests.
- CI/CD: Tekton or equivalent for pipeline enforcement and evidence capture.
- Execution envelopes: Kubernetes for containers; KubeVirt or equivalent for VM envelopes.
- Object storage: S3-compatible backend (e.g., MinIO, ceph-rgw) implementing EOSC metadata and immutability.
- Policy/authority: OPA-like policy engine; explicit authority binding and refusal semantics.
- Evidence/audit: Hash-chained evidence store with export; aligns to WS5 and IALP.

## Deliverables (later)
- Blueprint doc mapping invariants to components/configs.
- Sample manifests/policies demonstrating OLZ-EU, EOSC governance metadata, admission gates, evidence hooks, CRP partition behavior.
- Conformance harness to validate the reference stack against ECS tests.
