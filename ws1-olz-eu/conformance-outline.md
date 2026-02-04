# WS1 Conformance Outline (Draft)

## Tenant and authority
- Tenant creation MUST require identity binding and explicit authority approval.
- Verify project/workspace creation fails without authority evidence.
- Audit events MUST capture who approved and under what scope.
 - Verify policy baseline is applied and recorded as a policy snapshot at creation time.
 - Verify refusal paths emit evidence with refusal reason and snapshot IDs.

## Network and policy baseline
- Default posture MUST be deny for governed workloads; test that unsanctioned egress fails.
- Segmentation tests: ensure cross-tenant flows are blocked unless explicitly allowed.
- Exception paths MUST require explicit approval and produce evidence.

## Identity federation
- Verify OIDC validation evidence is captured for accepted and refused tokens.
- Verify S2S mTLS validation evidence is captured where used.

## Audit and evidence
- Control-plane actions (create/update/delete) MUST emit evidence events with policy snapshot IDs.
- Evidence events MUST be chainable (hash-linked) and exportable via the audit API.
 - Export bundles MUST declare `evidence_profile_id`; profile-required chain fields must be present.
