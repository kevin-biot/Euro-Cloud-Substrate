# Runtime Smoke Tests (Draft)

## Purpose
Provide pass/fail runtime checks that vendors can run in CI after generating an ECS evidence bundle.

## Inputs
- Bundle directory containing:
  - `manifest.json`
  - `events.jsonl`
  - `chain-segment.json`
  - `verifier-inputs.json`
  - `profile-claim.json`

## Test R1: required files present
**Check**
```bash
for f in manifest.json events.jsonl chain-segment.json verifier-inputs.json profile-claim.json; do
  test -f "$BUNDLE/$f" || exit 1
done
```
**Pass**: all files exist.

## Test R2: profile declaration consistency
**Check**
```bash
m=$(jq -r '.evidence_profile_id' "$BUNDLE/manifest.json")
v=$(jq -r '.evidence_profile_id' "$BUNDLE/verifier-inputs.json")
p=$(jq -r '.evidence_profile_id' "$BUNDLE/profile-claim.json")
[ "$m" = "$v" ] && [ "$m" = "$p" ]
```
**Pass**: all three match.

## Test R3: event envelope minimum
**Check**
```bash
jq -c . "$BUNDLE/events.jsonl" | while read -r ev; do
  echo "$ev" | jq -e '.id and .event_type and .occurred_at and .tenant_id and .sequence and .outcome and .evidence_pointer' >/dev/null || exit 1
done
```
**Pass**: all events contain minimum envelope fields.

## Test R4: chain continuity
**Check**
```bash
prev=""
first=1
while IFS= read -r ev; do
  event_hash=$(echo "$ev" | jq -r '.event_hash')
  prev_hash=$(echo "$ev" | jq -r '.prev_hash // ""')
  if [ "$first" -eq 1 ]; then
    [ -z "$prev_hash" ]
    first=0
  else
    [ "$prev_hash" = "$prev" ]
  fi
  prev="$event_hash"
done < <(jq -c . "$BUNDLE/events.jsonl")
```
**Pass**: every event links to previous hash, first event has no `prev_hash`.

## Test R5: refusal coverage
**Check**
```bash
jq -c 'select(.outcome=="refused")' "$BUNDLE/events.jsonl" | grep -q .
```
Then validate refusal reason present:
```bash
jq -c 'select(.outcome=="refused")' "$BUNDLE/events.jsonl" | while read -r ev; do
  echo "$ev" | jq -e '.refusal_reason' >/dev/null || exit 1
done
```
**Pass**: at least one refusal event and each refusal has `refusal_reason`.

## Test R6: artifact pointer shape
**Check**
```bash
jq -r '.evidence_pointer' "$BUNDLE/events.jsonl" | grep -E '^eosc://(evidence|artifact)/'
```
**Pass**: all pointers use expected URI shape.

## Test R7: sequence window matches manifest
**Check**
```bash
from=$(jq -r '.scope.from_sequence' "$BUNDLE/manifest.json")
to=$(jq -r '.scope.to_sequence' "$BUNDLE/manifest.json")
min=$(jq -r '.sequence' "$BUNDLE/events.jsonl" | sort -n | head -1)
max=$(jq -r '.sequence' "$BUNDLE/events.jsonl" | sort -n | tail -1)
[ "$from" = "$min" ] && [ "$to" = "$max" ]
```
**Pass**: event range equals declared manifest scope.

## Optional R8: hash profile checks (ML)
If ML profile is used, verify `hash_profile_id` exists in manifest and ML events.

## CI recommendation
- Fail pipeline on R1-R7 failure.
- Attach bundle and smoke output as build artifacts.
- Run full verifier checks as a second stage.
