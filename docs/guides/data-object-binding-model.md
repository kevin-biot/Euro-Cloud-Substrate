# Data Object Binding Model (Draft)

## Intent
Define how ECS governance metadata attaches to cloud/data objects in a portable way across files, object storage, queues, streams, datasets, and model artifacts.

## Core model
- ECS uses an **overlay binding record** as the canonical attachment model.
- Provider-native metadata/tags are optional mirrors, not the source of truth.
- Binding records are immutable evidence-linked records keyed by stable object references.

## Why overlay-first
- Embedded/native metadata is platform-specific and drifts across copy/move/export paths.
- Overlay records stay portable and verifier-friendly across providers and object classes.
- Governance survives format changes and storage migrations.

## Object reference (draft JSON)
Verifier input: `evidence_profile_id` MUST match the declared profile in the export manifest.
```json
{
  "object_ref": {
    "object_class": "object",
    "locator": "s3://bucket/key",
    "provider_id": "cloud-a",
    "account_id": "tenant-123",
    "region": "eu-west-1",
    "version_id": "3Lg...",
    "etag": "\"ab12...\"",
    "content_hash": "sha256:..."
  }
}
```

## Binding record (draft JSON)
```json
{
  "binding_key": "bkey-001",
  "binding_id": "bind-001",
  "object_ref": {
    "object_class": "object",
    "locator": "s3://bucket/key"
  },
  "purpose_id": "purpose.training",
  "consent_token_ref": "consent-abc",
  "terms_snapshot_id": "terms-v7",
  "classification": "restricted",
  "jurisdiction": "EU",
  "retention": "P180D",
  "policy_snapshot_id": "pol-2026-03-16",
  "authority_snapshot_id": "auth-2026-03-16",
  "evidence_profile_id": "ecs-evidence-baseline",
  "outcome": "accepted",
  "evidence_pointer": "eosc://evidence/evt-123"
}
```

- `binding_key` is the stable identity for the object/purpose attachment scope.
- `binding_id` identifies the specific immutable binding revision, including governance fields such as policy snapshot, jurisdiction, retention, and evidence profile.

## Object-class attachment matrix
| Object class | Typical locator | Native metadata mirror | Canonical ECS attachment |
|---|---|---|---|
| File (Nextcloud/POSIX) | path + file_id/inode | optional xattrs/platform fields | overlay binding record |
| Object storage (S3-like) | bucket/key + version_id | object tags/metadata | overlay binding record |
| Queue message | queue/topic + message_id | headers/attributes | overlay binding record |
| Stream event | stream/topic + offset | event headers | overlay binding record |
| Dataset/table | dataset/table + snapshot id | catalog metadata | overlay binding record |
| Model artifact | registry uri + digest | OCI labels/registry metadata | overlay binding record |
| API response artifact | request id + response hash | response headers | overlay binding record |

## Verifier checks
- Resolve object identity from `object_ref` and verify hash/version where available.
- Validate binding continuity across transforms (`parent_refs` chain).
- Validate purpose/consent/terms propagation from parent to derived objects.
- Validate deletion/rectification propagation evidence for downstream objects.
- Detect drift between native metadata mirror and overlay record; treat overlay as authoritative.

## Event alignment
The model is designed to align with:
- `data.product.publish`
- `data.transform.link`
- `policy.outcome.measure`
- `policy.rule.update`

## Non-goals
- ECS does not mandate one storage API or one metadata mechanism.
- ECS does not require embedding governance metadata in file formats.

## Reference helper code
- Neutral binding helper (draft): `adapters/common/object_binding.py`
- Usage notes: `adapters/common/README.md`
