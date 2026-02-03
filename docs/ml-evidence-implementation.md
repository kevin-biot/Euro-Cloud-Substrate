# ML Evidence Implementation Gap (Draft)

## Intent
Document the practical gap between regulatory evidence requirements (AI Act–aligned) and current cloud ML service capabilities, and define where ECS evidence requirements can be feasibly interposed.

## Why this matters (AI Act context)
High‑risk and regulated AI systems require **traceable, verifiable evidence** of decisions, model lineage, and policy/authority context. In practice, most cloud ML services do not emit portable, deterministic evidence for inference or training by default. This gap impacts **providers** and **users** (deployers) who must demonstrate compliance.

## The gap in today’s platforms (summary)
- **Inference evidence** is often limited to application logs; it lacks standardized, portable records of model version, policy snapshot, and refusal semantics.
- **Training evidence** is fragmented across pipeline tools; dataset provenance and checkpoint lineage are not deterministically captured.
- **Evidence export** is inconsistent; cloud logs are not portable compliance artifacts.

## Interposition points (where evidence can be captured)

### Inference (moderate difficulty)
**Where to hook:**
- API gateway or service mesh sidecar (request/response boundary).
- Model server wrapper (decision point).
- Admission controller for model deployments (policy snapshot binding).

**What to capture:**
- `model_id`, `model_sbom_ref`
- `input_hash` / `context_hash`
- `hash_profile_id` (canonicalization rules)
- `output_ref` (subject to data policy and evidence pointer contract)
- `policy_snapshot_id` / `authority_snapshot_id`
- `outcome` (accepted/refused/failed) + evidence pointer

### Training (higher difficulty)
**Where to hook:**
- Pipeline orchestration layer (e.g., training job submission).
- Artifact store (checkpoint/model output).
- Data access layer (dataset hash and references).

**What to capture:**
- `dataset_refs` + hashes
- `code_version`, `hyperparameters_hash`
- `hash_profile_id` (canonicalization rules)
- `checkpoint_hash` events
- `policy_snapshot_id` + evidence pointer

## Why this impacts deployers
If you consume a managed ML service for an **agentic workload**, you are still responsible for evidence of compliance. Without standardized evidence outputs from the provider, deployers must create their own wrappers or accept compliance gaps.

## How ECS helps
ECS defines:
- A **canonical evidence envelope** (Core10-05).
- A **portable export schema** (`docs/evidence-export-schema.md`).
- **ML inference/training event shapes** (`docs/evidence-catalog.md`).

These provide the minimum contract vendors can implement and deployers can request.

## Hashing profile guidance (draft)
Hashes are only portable if their canonicalization rules are explicit. Providers SHOULD emit a `hash_profile_id` (e.g., `ecs-hash-v1`) and document what is included/excluded, how PII is handled, and how hashes are recomputed.

## Recommended next steps (non-normative)
- Providers: publish evidence hooks and export packages for ML endpoints.
- Deployers: require evidence export clauses in ML service contracts.
- OSS communities: build adapters for common ML stacks (K8s, Kubeflow, model servers, managed-ML wrappers).
- Ensure evidence bundles can be timestamped/sealed by qualified trust services where required for legal admissibility.

## OSS adapter guide (draft)
This guide outlines a practical path for open source maintainers to close the evidence gap without redesigning ML platforms.

### Minimal adapter deliverables
- **Evidence emitter**: library or sidecar that emits Core10-05 envelope events.
- **Policy snapshot binder**: resolves and attaches policy snapshot ids at admission or inference time.
- **Consent/purpose binder**: attaches CITP references where required.
- **Evidence exporter**: bundles events and artifacts per `docs/evidence-export-schema.md`.

### Kubernetes/OpenShift insertion points
- **Admission webhook**: enforce policy snapshot binding and attach correlation ids.
- **Ingress gateway / service mesh**: capture inference request/response hashes.
- **Sidecar or model server plugin**: emit inference evidence events with model version metadata.
- **Jobs/Pipelines**: emit training evidence events at start/checkpoint/complete.

### Kubeflow / pipeline tooling
- **Pipeline step wrappers**: compute dataset hashes, capture code version, record hyperparameter hashes.
- **Artifact store hooks**: emit checkpoint evidence on artifact write.
- **Metadata store sync**: map pipeline metadata to evidence export bundles.

### Managed ML wrappers (client-side)
- **Request proxy**: client wrapper that captures input/context hashes and binds policy snapshot id.
- **Response recorder**: records model output refs and outcome evidence.
- **Contract helper**: attaches usage receipts for governed access.

### Suggested initial artifacts
- Reference adapter for K8s model servers (e.g., Triton, TF Serving).
- Kubeflow pipeline component templates with evidence emission.
- Exporter tool that generates evidence bundles from logs + metadata stores.

### Messaging to vendors and customers
- This is not a replacement for vendor features; it is a **minimal evidence substrate** customers can demand.
- The goal is portability: evidence should be exportable and verifiable across providers.

## Deployer checklist (draft)
Use this as a minimum checklist when consuming managed ML services or deploying on a cloud platform.
1. **Policy snapshot binding**: evidence includes policy snapshot id for each governed action.
2. **Authority binding**: evidence includes authority snapshot id or binding reference.
3. **Inference evidence**: input/context hashes, model version/SBOM ref, outcome, evidence pointer.
4. **Training evidence**: dataset hashes, code version, hyperparameter hash, checkpoint hashes.
5. **Hashing profile**: evidence includes `hash_profile_id` so hashes can be recomputed deterministically.
6. **Usage receipts**: data access and sharing events emit usage receipts (URP).
7. **Exportability**: evidence bundles can be exported via `docs/evidence-export-schema.md`.
8. **Integrity**: evidence is hash‑chained with sequence/prev_hash continuity.
9. **Retention**: evidence retained for required period; export is available on request.

## Regulatory risk if evidence is missing (draft)
- **AI Act:** inability to demonstrate decision traceability, model version lineage, or post‑market monitoring can trigger non‑compliance findings.
- **GDPR:** lack of lawful basis evidence and purpose binding weakens accountability and auditability.
- **DORA / NIS2:** missing operational evidence undermines resilience and audit obligations.
- **Commercial impact:** procurement requirements and regulated customers may reject platforms without portable evidence exports.

## Deployer risk note (non-normative)
When deployers consume managed LLM services, liability for outputs often remains with the deployer, while evidence for provenance or policy enforcement may be unavailable. Without portable evidence bundles, deployers can be left in a weak position in copyright or liability disputes. This is a key reason to require evidence export clauses and standardized evidence outputs in service contracts.

## Copyright/IP note (non-normative)
While not the primary focus here, the same evidence substrate (training provenance, policy snapshots, usage receipts) can help demonstrate rights and provenance for model training and inference, which may be useful in copyright or IP disputes.

## Minimal evidence SDK proposal (draft)
An open‑source SDK to standardize evidence emission across ML stacks.

### SDK responsibilities
- Emit Core10‑05 envelope events.
- Bind policy/authority snapshot ids and consent/usage references.
- Compute input/context hashes and attach model version metadata.
- Package and export bundles per `docs/evidence-export-schema.md`.
- Support optional chain anchoring to qualified archive services (evidence admissibility).

### SDK interfaces (sketch)
```json
{
  "emit_inference_event": {
    "model_id": "model-123",
    "model_sbom_ref": "eosc://sbom/model-123",
    "input_hash": "sha256:...",
    "context_hash": "sha256:...",
    "hash_profile_id": "ecs-hash-v1",
    "output_ref": "eosc://output/obj-123",
    "policy_snapshot_id": "pol-001",
    "authority_snapshot_id": "auth-789",
    "outcome": "accepted",
    "evidence_pointer": "eosc://evidence/evt-123"
  }
}
```

### Packaging and export
- `export_bundle(from_sequence, to_sequence)` → evidence bundle + manifest.
- Optional: `sign_bundle(key_id)` for non‑repudiation.
