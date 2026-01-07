#!/usr/bin/env bash
set -euo pipefail

labels=(
  "spec-draft:9c27b0:Spec drafts and updates"
  "discussion:0e8a16:Discussions and questions"
  "conformance:0366d6:Conformance outlines/tests"
  "governance:d93f0b:Governance/ADR/process"
  "diagram:5319e7:Diagram/visual updates"
)

for entry in "${labels[@]}"; do
  IFS=":" read -r name color desc <<<"$entry"
  gh label create "$name" --color "$color" --description "$desc" 2>/dev/null || \
    gh label edit "$name" --color "$color" --description "$desc"
done

echo "Labels ensured."
