# ECS ML Inference Sidecar Adapter (Draft)

## Intent
Provide a minimal reference sidecar that emits **Core10‑05 evidence** for ML inference calls, aligned to the regulated‑ML profile when required.

## Components (planned)
- `sidecar.py` — HTTP sidecar that wraps model inference.
- `evidence.py` — Core10‑05 event emission (mirrors `adapters/k8s-admission`).
- `exporter.py` — Evidence bundle exporter (mirrors `adapters/k8s-admission`).
- `example-manifest.yaml` — Deployment example (sidecar container + env).

## Quick start (local reference)
```bash
python3 sidecar.py \
  --store ./evidence-store \
  --profile ecs-evidence-baseline \
  --upstream http://localhost:9000/infer
```

### Example inference request
```bash
curl -s -X POST http://localhost:8081/infer \\
  -H 'Content-Type: application/json' \\
  -H 'X-ECS-Policy-Snapshot: pol-2026-02' \\
  -H 'X-ECS-Authority-Snapshot: auth-2026-01' \\
  -H 'X-ECS-Correlation-Id: corr-123' \\
  -H 'X-ECS-Model-Id: model-001' \\
  -d '{\"prompt\":\"hello\"}'
```

## Expected evidence events
