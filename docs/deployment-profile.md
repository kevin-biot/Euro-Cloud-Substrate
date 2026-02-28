# Deployment Profile (Draft)

## Intent
Define a provider-neutral deployment contract so the same ECS instance can be deployed across Cloud A and Cloud B without changing governance semantics.

## Scope
- Standardizes deployment **shape elements** and required controls.
- Does not standardize deployment tools (Pulumi/Terraform/Helm are all valid).
- Applies to deploy-time and day-2 re-deploy/cutover workflows.

## Deployment contract (profile fields)
A deployment profile SHOULD declare, at minimum:
- `profile_id`, `version`
- `control_plane` endpoints and required components
- `identity_trust` inputs (IdP/JWKS/CA references)
- `evidence_defaults` (`evidence_profile_id`, `hash_profile_id`)
- `policy_authority` snapshot inputs (`policy_snapshot_id`, `authority_snapshot_id`)
- `jurisdiction_routing` constraints and refusal mode
- `data_controls` (classification, residency, retention, legal-hold defaults)
- `export_verifier` interfaces (bundle export + verifier inputs)
- `dependency_manifest_ref` for non-substitutable dependencies

## Portability rules
- The same deployment profile MUST produce equivalent control/evidence semantics across providers.
- Provider-specific implementation details MAY vary, but profile fields and outcomes must remain stable.
- Unsupported profile requirements MUST fail closed with refusal evidence.

## Tool mapping (non-normative)
- **Pulumi**: encode the profile as stack config and component inputs.
- **Terraform**: encode the profile as module variables and outputs.
- **Helm/Kustomize**: encode the profile as values overlays and rendered manifests.

Tool choice is an implementation detail; the deployment profile is the contract.

## Conformance checks (draft)
- Profile declares required ECS fields and IDs.
- Deployed instance emits expected evidence defaults and chain/profile annotations.
- Export and verifier interfaces are reachable and match declared profile.
- Refusal evidence is emitted when profile constraints cannot be met.

## Related
- WS6 migration: `ws6-migration/spec.md`
- Federation domain: `docs/domains/federation.md`
- Evidence export schema: `docs/evidence/export-schema.md`
