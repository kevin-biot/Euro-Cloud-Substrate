# Evidence Catalog (Skeleton)

Evidence types should be tied to invariant IDs. This skeleton lists families with placeholders for future detail.

## AUTH
- Evidence types (tbd)

## POL
- Evidence types (tbd)

## EXEC
- Evidence types (tbd)

## DATA
- Evidence types (tbd)

## EVID
- Evidence events for storage (EVID/DATA/SUP example):
```json
{
  "type": "object",
  "properties": {
    "event_type": { "enum": ["object.put", "object.delete", "object.copy", "object.replicate", "object.lock", "object.unlock", "object.retention-update"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "object_id": { "type": "string" },
    "version_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "policy_snapshot_id": { "type": "string" },
    "governance_metadata": {
      "$ref": "#/definitions/eosc-metadata"
    },
    "outcome": { "enum": ["success", "refusal"] },
    "refusal_reason": { "type": "string" }
  },
  "required": ["event_type", "timestamp", "object_id", "outcome"]
}
```

Definitions (snippet):
```json
{
  "definitions": {
    "eosc-metadata": {
      "type": "object",
      "properties": {
        "x-eosc-jurisdiction": { "type": "string" },
        "x-eosc-retention-ttl": { "type": "string" },
        "x-eosc-integrity": { "type": "string" },
        "x-eosc-classification": { "type": "string" },
        "x-eosc-evidence-pointer": { "type": "string" }
      },
      "required": [
        "x-eosc-jurisdiction",
        "x-eosc-retention-ttl",
        "x-eosc-integrity",
        "x-eosc-classification",
        "x-eosc-evidence-pointer"
      ]
    }
  }
}
```

## INT
- Evidence types (tbd)

## EXIT
- Evidence types (tbd)

## DEP
- Evidence types (tbd)

## SUP
- Evidence types (tbd)

## OPS
- Evidence types (tbd)

## PHY
- Evidence types (tbd)
