# ECS ML Inference Sidecar Adapter (Draft)

## Intent
Provide a minimal reference sidecar that emits **Core10‑05 evidence** for ML inference calls, aligned to the regulated‑ML profile when required.

## Components (planned)
- `sidecar.py` — HTTP sidecar that wraps model inference.
- `evidence.py` — Core10‑05 event emission (reuse from `adapters/k8s-admission`).
- `exporter.py` — Evidence bundle exporter (reuse from `adapters/k8s-admission`).
- `example-manifest.yaml` — Deployment example (sidecar container + env).

## Expected evidence events
