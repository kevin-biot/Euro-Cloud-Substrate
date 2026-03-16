import hashlib
import json
from typing import Any, Dict, List, Optional

SUPPORTED_OBJECT_CLASSES = {
    "file",
    "object",
    "queue_message",
    "stream_event",
    "dataset",
    "model_artifact",
    "api_response",
}


def canonical_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _require_fields(data: Dict[str, Any], fields: List[str]) -> None:
    missing = [name for name in fields if not data.get(name)]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")


def build_object_ref(
    object_class: str,
    locator: str,
    provider_id: Optional[str] = None,
    account_id: Optional[str] = None,
    region: Optional[str] = None,
    version_id: Optional[str] = None,
    etag: Optional[str] = None,
    content_hash: Optional[str] = None,
    message_id: Optional[str] = None,
    offset: Optional[str] = None,
    request_id: Optional[str] = None,
    response_hash: Optional[str] = None,
) -> Dict[str, Any]:
    if object_class not in SUPPORTED_OBJECT_CLASSES:
        raise ValueError(f"unsupported object_class: {object_class}")

    object_ref: Dict[str, Any] = {
        "object_class": object_class,
        "locator": locator,
    }

    optional_fields = {
        "provider_id": provider_id,
        "account_id": account_id,
        "region": region,
        "version_id": version_id,
        "etag": etag,
        "content_hash": content_hash,
        "message_id": message_id,
        "offset": offset,
        "request_id": request_id,
        "response_hash": response_hash,
    }

    for key, value in optional_fields.items():
        if value:
            object_ref[key] = value

    if object_class == "queue_message":
        _require_fields(object_ref, ["message_id"])
    elif object_class == "stream_event":
        _require_fields(object_ref, ["offset"])
    elif object_class == "api_response":
        _require_fields(object_ref, ["request_id", "response_hash"])

    return object_ref


def build_binding_record(
    object_ref: Dict[str, Any],
    purpose_id: str,
    policy_snapshot_id: str,
    authority_snapshot_id: str,
    evidence_profile_id: str,
    evidence_pointer: str,
    consent_token_ref: Optional[str] = None,
    terms_snapshot_id: Optional[str] = None,
    classification: Optional[str] = None,
    jurisdiction: Optional[str] = None,
    retention: Optional[str] = None,
    outcome: str = "accepted",
) -> Dict[str, Any]:
    record = {
        "object_ref": object_ref,
        "purpose_id": purpose_id,
        "policy_snapshot_id": policy_snapshot_id,
        "authority_snapshot_id": authority_snapshot_id,
        "evidence_profile_id": evidence_profile_id,
        "evidence_pointer": evidence_pointer,
        "outcome": outcome,
    }

    if consent_token_ref:
        record["consent_token_ref"] = consent_token_ref
    if terms_snapshot_id:
        record["terms_snapshot_id"] = terms_snapshot_id
    if classification:
        record["classification"] = classification
    if jurisdiction:
        record["jurisdiction"] = jurisdiction
    if retention:
        record["retention"] = retention

    digest_source = {
        "object_ref": object_ref,
        "purpose_id": purpose_id,
        "policy_snapshot_id": policy_snapshot_id,
        "authority_snapshot_id": authority_snapshot_id,
        "terms_snapshot_id": terms_snapshot_id or "",
    }
    digest = sha256_hex(canonical_json(digest_source).encode("utf-8"))
    record["binding_id"] = f"bind-{digest[:12]}"
    return record


def build_data_product_publish_event(binding_record: Dict[str, Any]) -> Dict[str, Any]:
    object_ref = binding_record["object_ref"]
    event = {
        "event_type": "data.product.publish",
        "data_product_id": object_ref.get("locator"),
        "object_ref": object_ref,
        "purpose_id": binding_record["purpose_id"],
        "policy_snapshot_id": binding_record["policy_snapshot_id"],
        "authority_snapshot_id": binding_record["authority_snapshot_id"],
        "evidence_profile_id": binding_record["evidence_profile_id"],
        "outcome": binding_record["outcome"],
        "evidence_pointer": binding_record["evidence_pointer"],
    }
    for name in ["consent_token_ref", "terms_snapshot_id", "classification", "jurisdiction", "retention"]:
        if binding_record.get(name):
            event[name] = binding_record[name]
    return event


def build_data_transform_link_event(
    derived_binding_record: Dict[str, Any],
    parent_binding_records: List[Dict[str, Any]],
    transform_type: str,
) -> Dict[str, Any]:
    parent_refs = [parent["object_ref"] for parent in parent_binding_records]
    event = {
        "event_type": "data.transform.link",
        "data_product_id": derived_binding_record["object_ref"].get("locator"),
        "object_ref": derived_binding_record["object_ref"],
        "parent_refs": parent_refs,
        "transform_type": transform_type,
        "purpose_id": derived_binding_record["purpose_id"],
        "policy_snapshot_id": derived_binding_record["policy_snapshot_id"],
        "authority_snapshot_id": derived_binding_record["authority_snapshot_id"],
        "evidence_profile_id": derived_binding_record["evidence_profile_id"],
        "outcome": derived_binding_record["outcome"],
        "evidence_pointer": derived_binding_record["evidence_pointer"],
    }
    for name in ["consent_token_ref", "terms_snapshot_id", "classification", "jurisdiction", "retention"]:
        if derived_binding_record.get(name):
            event[name] = derived_binding_record[name]
    return event


def build_native_mirror(
    binding_record: Dict[str, Any],
    target: str,
) -> Dict[str, str]:
    base = {
        "ecs_binding_id": binding_record.get("binding_id", ""),
        "ecs_purpose_id": binding_record.get("purpose_id", ""),
        "ecs_policy_snapshot_id": binding_record.get("policy_snapshot_id", ""),
        "ecs_authority_snapshot_id": binding_record.get("authority_snapshot_id", ""),
        "ecs_evidence_profile_id": binding_record.get("evidence_profile_id", ""),
        "ecs_classification": binding_record.get("classification", ""),
        "ecs_jurisdiction": binding_record.get("jurisdiction", ""),
        "ecs_retention": binding_record.get("retention", ""),
    }

    if target == "s3_tags":
        return {k: v for k, v in base.items() if v}
    if target == "nextcloud_fields":
        return {k: v for k, v in base.items() if v}
    if target == "queue_headers":
        return {f"x-{k}": v for k, v in base.items() if v}
    if target == "api_headers":
        return {f"x-{k}": v for k, v in base.items() if v}

    raise ValueError(f"unsupported mirror target: {target}")


def build_example_bindings() -> Dict[str, Dict[str, Any]]:
    policy_snapshot_id = "pol-2026-03-16"
    authority_snapshot_id = "auth-2026-03-16"
    evidence_profile_id = "ecs-evidence-baseline"

    examples: Dict[str, Dict[str, Any]] = {}

    classes = [
        ("file", "nextcloud://team/42/file/123"),
        ("object", "s3://bucket-a/path/doc.pdf"),
        ("queue_message", "queue://orders", "msg-123"),
        ("stream_event", "stream://events/payments", "offset-987"),
        ("dataset", "dataset://analytics/customer360@v5"),
        ("model_artifact", "oci://registry/model@sha256:abc123"),
        ("api_response", "https://api.example.eu/v1/infer", "req-456"),
    ]

    for item in classes:
        object_class = item[0]
        locator = item[1]
        kwargs: Dict[str, Any] = {
            "provider_id": "provider-eu-1",
            "account_id": "tenant-123",
            "region": "eu-west-1",
            "content_hash": "sha256:deadbeef",
        }
        if object_class == "queue_message":
            kwargs["message_id"] = item[2]
        if object_class == "stream_event":
            kwargs["offset"] = item[2]
        if object_class == "api_response":
            kwargs["request_id"] = item[2]
            kwargs["response_hash"] = "sha256:beadfeed"

        object_ref = build_object_ref(object_class, locator, **kwargs)
        binding = build_binding_record(
            object_ref=object_ref,
            purpose_id="purpose.governed-processing",
            policy_snapshot_id=policy_snapshot_id,
            authority_snapshot_id=authority_snapshot_id,
            evidence_profile_id=evidence_profile_id,
            evidence_pointer="eosc://evidence/evt-demo",
            terms_snapshot_id="terms-v1",
            classification="restricted",
            jurisdiction="EU",
            retention="P180D",
        )
        examples[object_class] = binding

    return examples
