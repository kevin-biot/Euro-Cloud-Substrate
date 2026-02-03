# ECS K8s Admission Reference Adapter (Draft)

## Intent
Provide a minimal, vendor-neutral reference adapter that:
- Binds authority/policy snapshots at admission time.
- Emits Core10-05 evidence events with profile annotations.
- Exports evidence bundles matching the ECS schema.

## Components
- `binder.py` — Admission webhook (binder).
- `evidence.py` — Evidence emitter library (Core10-05 events + chain fields).
- `exporter.py` — Bundle exporter CLI.

## Quick start (local reference)
```bash
python3 binder.py --store ./evidence-store --profile ecs-evidence-baseline
```

### Example AdmissionReview (curl)
```bash
curl -s -X POST http://localhost:8080/ \
  -H 'Content-Type: application/json' \
  -d '{
    "request": {
      "uid": "req-001",
      "object": {
        "metadata": {
          "name": "demo",
          "namespace": "default",
          "annotations": {
            "ecs.policy/snapshot": "pol-001",
            "ecs.authority/snapshot": "auth-001"
          }
        }
      }
    }
  }'
```

### Export a bundle
```bash
python3 exporter.py \
  --store ./evidence-store \
  --out ./bundle \
  --from-seq 1 \
  --to-seq 10 \
  --profile ecs-evidence-baseline
```

## Evidence profile selection
- Binder default profile can be set with `--profile` or `ECS_EVIDENCE_PROFILE`.
- Optional hash profile is derived from labels/annotations or from regulated-ML profile.

## Notes
- This is a reference adapter for contract fidelity, not production readiness.
- TLS/mTLS, authn/z, and Kubernetes deployment manifests are intentionally omitted.
