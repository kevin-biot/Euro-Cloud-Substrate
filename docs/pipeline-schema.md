# Minimal Pipeline Schema (Draft)

## Intent
Define a portable, evidence‑aware pipeline schema for provisioning, deployment, rollback, and migration workflows.

## Why this matters
Without a shared pipeline contract, deployers must build bespoke wrappers for evidence emission and portability. A minimal schema enables ECS‑aligned adapters across CI/CD and GitOps tools.

## Pipeline record (draft JSON)
Verifier input: `evidence_profile_id` MUST match the declared profile in the export manifest.
```json
{
  "pipeline_id": "pipe-001",
  "stage": "deploy",
  "action": "apply",
  "workload_id": "wl-123",
  "artifact_ref": "oci://image@sha256:...",
  "evidence_profile_id": "ecs-evidence-baseline",
  "policy_snapshot_id": "pol-001",
  "authority_snapshot_id": "auth-789",
  "correlation_id": "corr-456",
  "outcome": "accepted",
  "evidence_pointer": "eosc://evidence/evt-123"
}
```

## Evidence hooks (draft)
Evidence hooks SHOULD emit events at:
- **Provisioning**: landing zone, network baseline, identity binding.
- **Build/Scan**: artifact integrity, SBOM, provenance.
- **Deploy/Rollback**: policy snapshot binding, admission decisions.
- **Migrate/Export**: evidence export bundle creation and validation.

## Suggested evidence events
- `pipeline.provision.start|complete`
- `pipeline.deploy.start|complete`
- `pipeline.rollback.start|complete`
- `pipeline.migrate.start|complete`

## Notes
- This schema is intentionally minimal; tools may extend it.
- Evidence bundles SHOULD follow `docs/evidence-export-schema.md`.
