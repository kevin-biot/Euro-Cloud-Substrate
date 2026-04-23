#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
RUN_DIR="$ROOT_DIR/docs/examples/runtime/.run"
STORE_DIR="$RUN_DIR/evidence-store"
BUNDLE_DIR="$RUN_DIR/bundle"
BACKEND_LOG="$RUN_DIR/backend.log"
PROXY_LOG="$RUN_DIR/proxy.log"

BACKEND_PORT=19090
PROXY_PORT=18082

cleanup() {
  set +e
  [[ -n "${BACKEND_PID:-}" ]] && kill "$BACKEND_PID" >/dev/null 2>&1
  [[ -n "${PROXY_PID:-}" ]] && kill "$PROXY_PID" >/dev/null 2>&1
}
trap cleanup EXIT

wait_for_http() {
  local name="$1"
  local url="$2"
  local log_file="$3"
  local attempt=0

  while (( attempt < 50 )); do
    if curl -sS -o /dev/null --max-time 1 "$url" >/dev/null 2>&1; then
      return 0
    fi
    sleep 0.2
    attempt=$(( attempt + 1 ))
  done

  echo "$name did not become ready: $url" >&2
  if [[ -f "$log_file" ]]; then
    echo "--- $name log ---" >&2
    tail -n 50 "$log_file" >&2 || true
  fi
  exit 1
}

rm -rf "$RUN_DIR"
mkdir -p "$RUN_DIR"

python3 "$ROOT_DIR/docs/examples/runtime/mock_object_backend.py" --port "$BACKEND_PORT" >"$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!

python3 "$ROOT_DIR/adapters/object-storage-proxy/proxy.py" \
  --listen 127.0.0.1 \
  --port "$PROXY_PORT" \
  --upstream "http://127.0.0.1:${BACKEND_PORT}" \
  --store "$STORE_DIR" \
  --provider provider-demo \
  --tenant tenant-demo \
  --profile ecs-evidence-baseline \
  --fail-closed >"$PROXY_LOG" 2>&1 &
PROXY_PID=$!

wait_for_http "mock backend" "http://127.0.0.1:${BACKEND_PORT}/__ecs_ready__" "$BACKEND_LOG"
wait_for_http "object proxy" "http://127.0.0.1:${PROXY_PORT}/__ecs_ready__" "$PROXY_LOG"

curl -sS -X PUT "http://127.0.0.1:${PROXY_PORT}/eu-bucket/contracts/demo.txt" \
  -H 'X-ECS-Policy-Snapshot: pol-demo-001' \
  -H 'X-ECS-Authority-Snapshot: auth-demo-001' \
  -H 'X-ECS-Correlation-Id: corr-demo-001' \
  -H 'X-ECS-Jurisdiction: EU' \
  -H 'X-ECS-Classification: restricted' \
  -H 'X-ECS-Retention: P365D' \
  --data 'hello-evidence' >/dev/null

curl -sS "http://127.0.0.1:${PROXY_PORT}/eu-bucket/contracts/demo.txt" \
  -H 'X-ECS-Policy-Snapshot: pol-demo-001' \
  -H 'X-ECS-Authority-Snapshot: auth-demo-001' \
  -H 'X-ECS-Correlation-Id: corr-demo-001' >/dev/null

status=$(curl -sS -o /dev/null -w '%{http_code}' \
  -X PUT "http://127.0.0.1:${PROXY_PORT}/eu-bucket/contracts/refused.txt" \
  --data 'missing-snapshots')

if [[ "$status" != "403" ]]; then
  echo "expected refusal status 403, got $status" >&2
  exit 1
fi

python3 "$ROOT_DIR/adapters/object-storage-proxy/exporter.py" \
  --store "$STORE_DIR" \
  --out "$BUNDLE_DIR" \
  --from-seq 1 \
  --to-seq 50 \
  --profile ecs-evidence-baseline \
  --profile-version 1.0 \
  --producer-id ecs-reference-exporter \
  --verifier-expectations-ref docs/evidence/verifier-responsibilities.md

bash "$ROOT_DIR/docs/examples/runtime/smoke-checks.sh" "$BUNDLE_DIR"

echo "demo completed"
echo "evidence store: $STORE_DIR"
echo "bundle: $BUNDLE_DIR"
