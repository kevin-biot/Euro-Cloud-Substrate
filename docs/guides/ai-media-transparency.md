# AI‑Generated Media Transparency (Draft)

## Purpose
Explain the practical obligations around AI‑generated media (AI Act Article 50) and how ECS can support evidence without mandating watermarking or specific tooling.

## What Article 50 requires (plain language)
- **Providers** of AI systems generating synthetic audio/image/video/text must ensure outputs are **machine‑readably marked and detectable** as AI‑generated/manipulated, where technically feasible.
- **Deployers** must **disclose** deepfakes (image/audio/video) and AI‑generated text used to inform the public, with limited exceptions (e.g., obvious artistic/satirical contexts, law‑enforcement).
- **Users** interacting with AI must be informed unless obvious.

ECS does **not** implement these rules; it provides **evidence hooks** so providers/deployers can prove what was done.

## ECS position (non‑normative)
- **Watermarking/labeling** remains a product/provider choice.
- **Disclosure** remains an app/deployer responsibility.
- ECS should **enable evidence** that marking and disclosure occurred when required.

## Evidence hooks (recommended, non‑normative)
Providers/deployers SHOULD emit evidence events for:
- `content.marking.apply` (marking or watermark applied)
- `content.marking.verify` (verification at distribution)
- `content.disclosure.notice` (user‑facing disclosure presented)
- `content.disclosure.exempt` (exception applied, with reason)

These events should bind to policy snapshots and evidence pointers to support audits.

## Optional provenance feature (recommended)
Article 50 does not mandate provenance, but provenance can **close accountability gaps**.  
ECS recommends an **optional provenance artifact**:
- content hash + model id/version
- generation timestamp and policy snapshot
- marking method (if any)
- distribution/disclosure evidence pointer

### Optional provenance artifact (draft JSON)
```json
{
  "type": "object",
  "properties": {
    "content_id": { "type": "string" },
    "content_hash": { "type": "string" },
    "model_id": { "type": "string" },
    "model_version": { "type": "string" },
    "generated_at": { "type": "string", "format": "date-time" },
    "policy_snapshot_id": { "type": "string" },
    "authority_snapshot_id": { "type": "string" },
    "jurisdiction": { "type": "string" },
    "classification": { "type": "string" },
    "retention": { "type": "string" },
    "marking_method": { "type": "string" },
    "disclosure_evidence_ref": { "type": "string" }
  },
  "required": ["content_id", "content_hash", "model_id", "generated_at", "policy_snapshot_id", "jurisdiction", "classification", "retention"]
}
```
Provenance artifacts SHOULD be stored under the same jurisdiction and retention policy as the content they describe.
