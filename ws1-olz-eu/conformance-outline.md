# WS1 Conformance Outline (Draft)

## Tenant and authority
- Tenant creation MUST require identity binding and explicit authority approval.
- Verify project/workspace creation fails without authority evidence.
- Audit events MUST capture who approved and under what scope.

## Network and policy baseline
- Default posture MUST be deny for governed workloads; test that unsanctioned egress fails.
- Segmentation tests: ensure cross-tenant flows are blocked unless explicitly allowed.
- Exception paths MUST require explicit approval and produce evidence.

## Audit and evidence
- Control-plane actions (create/update/delete) MUST emit evidence events with policy snapshot IDs.
- Evidence events MUST be chainable (hash-linked) and exportable via the audit API.
