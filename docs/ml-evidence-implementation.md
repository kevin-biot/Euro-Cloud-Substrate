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

## Recommended next steps (non-normative)
- Providers: publish evidence hooks and export packages for ML endpoints.
- Deployers: require evidence export clauses in ML service contracts.
- OSS communities: build adapters for common ML stacks (K8s, Kubeflow, model servers, managed-ML wrappers).

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
