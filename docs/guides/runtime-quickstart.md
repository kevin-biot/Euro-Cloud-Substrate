# Runtime Quickstart (Draft)

## Goal
Run a minimal ECS runtime path end-to-end in 20-30 minutes:
- governed operations
- JSONL evidence emission
- refusal evidence
- bundle export
- verifier smoke checks

This path uses the object-storage proxy adapter and a local mock backend.

## Prerequisites
- `python3`
- `curl`
- `jq`

## One-command demo
From repo root:
```bash
bash docs/examples/runtime/run-demo.sh
```

Expected outputs:
- Evidence store: `docs/examples/runtime/.run/evidence-store/`
- Export bundle: `docs/examples/runtime/.run/bundle/`
- Includes at least one `outcome=refused` event.

## Manual run (step-by-step)
1) Start mock object backend:
```bash
python3 docs/examples/runtime/mock_object_backend.py --port 19090
```

2) Start object proxy (second terminal):
```bash
python3 adapters/object-storage-proxy/proxy.py \
  --listen 127.0.0.1 \
  --port 18082 \
  --upstream http://127.0.0.1:19090 \
  --store docs/examples/runtime/.run/evidence-store \
  --provider provider-demo \
  --tenant tenant-demo \
  --profile ecs-evidence-baseline \
  --fail-closed
```

3) Emit accepted events:
```bash
curl -sS -X PUT http://127.0.0.1:18082/eu-bucket/contracts/demo.txt \
  -H 'X-ECS-Policy-Snapshot: pol-demo-001' \
  -H 'X-ECS-Authority-Snapshot: auth-demo-001' \
  -H 'X-ECS-Correlation-Id: corr-demo-001' \
  -H 'X-ECS-Jurisdiction: EU' \
  -H 'X-ECS-Classification: restricted' \
  -H 'X-ECS-Retention: P365D' \
  --data 'hello-evidence'

curl -sS http://127.0.0.1:18082/eu-bucket/contracts/demo.txt \
  -H 'X-ECS-Policy-Snapshot: pol-demo-001' \
  -H 'X-ECS-Authority-Snapshot: auth-demo-001' \
  -H 'X-ECS-Correlation-Id: corr-demo-001'
```

4) Emit refusal event (missing snapshots with fail-closed):
```bash
curl -sS -o /dev/null -w '%{http_code}\n' \
  -X PUT http://127.0.0.1:18082/eu-bucket/contracts/refused.txt \
  --data 'missing-snapshots'
```
Expected status: `403`

5) Export bundle:
```bash
python3 adapters/object-storage-proxy/exporter.py \
  --store docs/examples/runtime/.run/evidence-store \
  --out docs/examples/runtime/.run/bundle \
  --from-seq 1 \
  --to-seq 50 \
  --profile ecs-evidence-baseline \
  --profile-version 1.0 \
  --producer-id ecs-reference-exporter \
  --verifier-expectations-ref docs/evidence/verifier-responsibilities.md
```

6) Run verifier smoke checks:
```bash
bash docs/examples/runtime/smoke-checks.sh docs/examples/runtime/.run/bundle
```

## What this proves
- Runtime actions are converted into ECS-shaped evidence events.
- Refusals are first-class and exported.
- Independent verifier inputs are present in the bundle.

## Next step
Run `docs/conformance/runtime-smoke-tests.md` and capture outputs as pilot evidence artifacts.
