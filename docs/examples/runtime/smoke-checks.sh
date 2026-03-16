#!/usr/bin/env bash
set -euo pipefail

BUNDLE_DIR="${1:-docs/examples/runtime/.run/bundle}"

if [[ ! -d "$BUNDLE_DIR" ]]; then
  echo "bundle directory not found: $BUNDLE_DIR" >&2
  exit 1
fi

for f in manifest.json events.jsonl chain-segment.json verifier-inputs.json profile-claim.json; do
  test -f "$BUNDLE_DIR/$f"
done

echo "[ok] required files present"

manifest_profile=$(jq -r '.evidence_profile_id' "$BUNDLE_DIR/manifest.json")
verifier_profile=$(jq -r '.evidence_profile_id' "$BUNDLE_DIR/verifier-inputs.json")
claim_profile=$(jq -r '.evidence_profile_id' "$BUNDLE_DIR/profile-claim.json")

[[ "$manifest_profile" == "$verifier_profile" && "$manifest_profile" == "$claim_profile" ]]
echo "[ok] evidence_profile_id consistency"

jq -c . "$BUNDLE_DIR/events.jsonl" | while read -r ev; do
  echo "$ev" | jq -e '.id and .event_type and .occurred_at and .tenant_id and .sequence and .outcome and .evidence_pointer' >/dev/null
done

echo "[ok] envelope fields present"

prev=""
first=1
while IFS= read -r ev; do
  event_hash=$(echo "$ev" | jq -r '.event_hash')
  prev_hash=$(echo "$ev" | jq -r '.prev_hash // ""')
  if [[ "$first" -eq 1 ]]; then
    [[ -z "$prev_hash" ]]
    first=0
  else
    [[ "$prev_hash" == "$prev" ]]
  fi
  prev="$event_hash"
done < <(jq -c . "$BUNDLE_DIR/events.jsonl")

echo "[ok] chain continuity"

refused_count=$(jq -c 'select(.outcome=="refused")' "$BUNDLE_DIR/events.jsonl" | wc -l | tr -d ' ')
[[ "$refused_count" -ge 1 ]]
jq -c 'select(.outcome=="refused")' "$BUNDLE_DIR/events.jsonl" | while read -r ev; do
  echo "$ev" | jq -e '.refusal_reason' >/dev/null
done

echo "[ok] refusal coverage"

echo "runtime smoke checks passed"
