# Open Source Alignment Targets (Draft, Non‑Normative)

## Intent
Provide a non‑normative list of open‑source projects that could align to ECS via overlays and adapters. This is not an endorsement, certification, or procurement list.

## How to use this list
- Treat these as **candidate alignment targets**.
- Alignment means adding **evidence emission**, **policy snapshot binding**, and **exportability** per ECS.
- Implementations remain vendor‑neutral; ECS defines the contract, not the product.

## Candidate targets by plane (illustrative)

### Plane A — Identity & Authority
- **Keycloak** (OIDC/SAML IAM) as a candidate authority/identity system; requires evidence event emission and policy snapshot binding.

### Plane B — Control Plane & Policy
- **OKD** (community Kubernetes distribution) as an OpenShift‑adjacent control plane target.
- **OPA** (general‑purpose policy engine) and **Kyverno** (Kubernetes policy engine) as policy evaluation/admission targets.

### Plane C — Execution Envelopes
- **Kubernetes/OKD** runtime with policy‑driven envelope selection and evidence hooks.
- VM envelope options can be layered via compatible runtimes (implementation‑specific).

### Plane D — Data & Evidence Substrate
- **Ceph** (object, block, file) as a unified storage substrate; align governance metadata and evidence export.
- **MinIO** as S3‑compatible object storage; align EOSC metadata and evidence events.
- **Longhorn** and **OpenEBS** as block storage targets; align block‑evidence events and export manifests.

### Plane E — Interop & Portability
- Interop API exposure and evidence export adapters layered on top of the above systems.

## Example “OpenShift‑alternative” stack (non‑normative)
- Control plane: OKD
- Identity: Keycloak
- Policy: OPA/Kyverno
- Storage: Ceph (object/block/file) + EOSC metadata overlays
- Evidence: ECS evidence export schema + chain anchoring adapter

## Alignment guidance (high level)
1. **Expose governance metadata** at write/admission time.
2. **Emit evidence events** with policy snapshot and authority bindings.
3. **Export evidence bundles** using `docs/evidence-export-schema.md`.
4. **Implement usage receipts** for governed data access.
5. **Optionally anchor chains** to qualified archiving services.
