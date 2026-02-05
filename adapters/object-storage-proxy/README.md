# ECS Object Storage Proxy Adapter (Draft)

## Intent
Provide a minimal proxy that emits **Core10‑05 evidence** for object storage operations (S3/Swift/MinIO/Ceph), aligned to EOSC governance metadata.

## Components
- `proxy.py` — HTTP proxy that forwards S3‑style requests and emits evidence events.
- `evidence.py` — Core10‑05 event emission (mirrors `adapters/k8s-admission`).
- `exporter.py` — Evidence bundle exporter (mirrors `adapters/k8s-admission`).

## Supported operations (baseline)
- `GET`/`HEAD` → `object.get`
- `PUT`/`POST` → `object.put`
- `DELETE` → `object.delete`

## Required headers (governed requests)
- `X-ECS-Policy-Snapshot`
- `X-ECS-Authority-Snapshot`
- `X-ECS-Correlation-Id` (optional; generated if missing)

Optional governance headers:
- `X-ECS-Jurisdiction`
- `X-ECS-Classification`
- `X-ECS-Retention`

## Quick start (local reference)
```bash
python3 proxy.py \
  --upstream http://localhost:9001 \
  --store ./evidence-store \
  --profile ecs-evidence-baseline
```

## Example manifest
See `example-manifest.yaml` for a minimal deployment manifest.

### Example request
```bash
curl -X PUT http://localhost:8082/bucket/key.txt \
  -H 'X-ECS-Policy-Snapshot: pol-2026-02' \
  -H 'X-ECS-Authority-Snapshot: auth-2026-01' \
  -H 'X-ECS-Correlation-Id: corr-123' \
  -H 'X-ECS-Jurisdiction: EU' \
  -H 'X-ECS-Classification: restricted' \
  -d 'hello'
```

## Notes
- This is a reference adapter; it does not implement S3 auth/signing.
- Use `--fail-closed` (or `ECS_FAIL_CLOSED=true`) to refuse requests missing required snapshots.
