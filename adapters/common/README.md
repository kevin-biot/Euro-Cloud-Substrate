# Common Adapter Helpers (Draft)

This folder provides neutral helper code for ECS object binding across multiple object classes.

## Why this exists
The same governance fields (purpose, terms, policy snapshot, authority snapshot, jurisdiction, retention) need to attach to different object classes in a portable way.

The helper in `object_binding.py` demonstrates an overlay-first model:
- canonical `object_ref`
- canonical binding record (`binding_key` for stable scope, `binding_id` for immutable revision)
- event payload helpers
- optional provider-native metadata mirror projection

## Supported object classes
- `file`
- `object`
- `queue_message`
- `stream_event`
- `dataset`
- `model_artifact`
- `api_response`

## Example usage
```python
from adapters.common.object_binding import (
    build_object_ref,
    build_binding_record,
    build_data_product_publish_event,
    build_native_mirror,
)

obj = build_object_ref(
    object_class="api_response",
    locator="https://api.example.eu/v1/infer",
    provider_id="provider-eu-1",
    account_id="tenant-123",
    region="eu-west-1",
    request_id="req-456",
    response_hash="sha256:beadfeed",
)

binding = build_binding_record(
    object_ref=obj,
    purpose_id="purpose.governed-processing",
    policy_snapshot_id="pol-2026-03-16",
    authority_snapshot_id="auth-2026-03-16",
    evidence_profile_id="ecs-evidence-baseline",
    evidence_pointer="eosc://evidence/evt-123",
    classification="restricted",
    jurisdiction="EU",
    retention="P180D",
)

publish_event = build_data_product_publish_event(binding)
api_headers = build_native_mirror(binding, target="api_headers")
```

## Notes
- This is a reference helper, not a mandatory runtime dependency.
- Overlay records remain authoritative; native metadata mirrors are convenience projections.
- API and queue header mirrors use the same hyphenated `X-ECS-*` wire shape used by the adapter examples.
