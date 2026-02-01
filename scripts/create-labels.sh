#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found. Install GitHub CLI and authenticate (gh auth login)." >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "gh CLI not authenticated. Run: gh auth login" >&2
  exit 1
fi

labels=(
  "spec-draft:9c27b0:Spec drafts and updates"
  "discussion:0e8a16:Discussions and questions"
  "conformance:0366d6:Conformance outlines/tests"
  "governance:d93f0b:Governance/ADR/process"
  "diagram:5319e7:Diagram/visual updates"
  "good-first-issue:fbca04:Starter issues for newcomers"
)

for entry in "${labels[@]}"; do
  IFS=":" read -r name color desc <<<"$entry"
  gh label create "$name" --color "$color" --description "$desc" 2>/dev/null || \
    gh label edit "$name" --color "$color" --description "$desc"
done

echo "Labels ensured."
