# AI‑Generated Media Transparency (Draft)

## Purpose
Explain the practical obligations around AI‑generated media (AI Act Article 50) and how ECS can support evidence without mandating watermarking or specific tooling.

## What Article 50 requires (plain language)
- **Providers** of AI systems generating synthetic audio/image/video/text must ensure outputs are **machine‑readably marked and detectable** as AI‑generated/manipulated, where technically feasible.
- **Deployers** must **disclose** deepfakes (image/audio/video) and AI‑generated text used to inform the public, with limited exceptions (e.g., obvious artistic/satirical contexts, law‑enforcement).
- **Users** interacting with AI must be informed unless obvious.

ECS does **not** implement these rules; it provides **evidence hooks** so providers/deployers can prove what was done.

## High‑risk vs transparency (clarifying note)
Election‑influence systems are already treated as **high‑risk** under Annex III (democratic processes).  
If a system is intended to influence electoral outcomes or voting behavior, high‑risk controls apply (risk management, logging, conformity assessment).  
By contrast, **general media generation** is governed by **Article 50 transparency duties** (marking + disclosure) unless the use‑case itself falls into a high‑risk category.

## CE mark vs transparency (clarifying note)
The **CE mark applies to high‑risk AI systems**, not to media outputs themselves.  
Most AI‑generated media use cases fall under **Article 50 transparency duties** (marking + disclosure), not CE marking.  
If a media‑generation system is classified as **high‑risk**, then the provider must complete the **conformity assessment** path and affix CE marking for the system.

## ECS position (non‑normative)
- **Watermarking/labeling** remains a product/provider choice.
- **Disclosure** remains an app/deployer responsibility.
- ECS should **enable evidence** that marking and disclosure occurred when required.

## Capability‑scoped invocation (STA‑L pattern, non‑normative)
Where AI media generation is invoked via a capability router (local or remote), providers SHOULD bind the call to a **scoped capability token** (STA‑L pattern) that declares:
- `content_class` (text | image | audio | video | mixed)
- `media_risk_class` (low | moderate | high‑impact)
- `disclosure_required` (true/false) and reason
- `provenance_required` (true/false) and profile
- `policy_snapshot_id`, `authority_snapshot_id`, `jurisdiction`

Evidence events SHOULD carry a `capability_token_ref` so auditors can verify the duties that were in force at generation time.  
If a required duty (disclosure/provenance) cannot be met, the invocation SHOULD be refused with refusal evidence.

### Example (request + refusal evidence)
Media generation request (capability‑scoped):
```json
{
  "capability_token_ref": "sta:local:media:7f4b",
  "content_class": "image",
  "media_risk_class": "high-impact",
  "disclosure_required": true,
  "provenance_required": true,
  "policy_snapshot_id": "pol-2026-02",
  "authority_snapshot_id": "auth-2026-01",
  "jurisdiction": "EU",
  "input_ref": "prompt://tenant/briefs/election-visual-v3"
}
```

Refusal evidence (Core10‑05 envelope):
```json
{
  "id": "7b7b2a9d-8cc0-43b5-8e2b-3cb6a6d2a3c1",
  "event_type": "content.generation.refuse",
  "occurred_at": "2026-02-05T13:58:12Z",
  "tenant_id": "tenant-123",
  "sequence": 41821,
  "outcome": "refused",
  "capability_token_ref": "sta:local:media:7f4b",
  "content_class": "image",
  "media_risk_class": "high-impact",
  "refusal_reason": "provenance_required_not_supported",
  "evidence_pointer": "eosc://evidence/tenant-123/refusals/7b7b2a9d.json"
}
```

## Enforceability gap (non‑normative)
Transparency duties without **evidence** are hard to verify.  
ECS addresses this by defining **evidence hooks** (marking, disclosure, refusal, provenance) so compliance can be audited without mandating a specific watermarking technology.

## Evidence hooks (recommended, non‑normative)
Providers/deployers SHOULD emit evidence events for:
- `content.marking.apply` (marking or watermark applied)
- `content.marking.verify` (verification at distribution)
- `content.disclosure.notice` (user‑facing disclosure presented)
- `content.disclosure.exempt` (exception applied, with reason)
- `content.generation.refuse` (prohibited‑practice or policy‑blocked generation)

These events should bind to policy snapshots and evidence pointers to support audits.

## Prohibited‑practice bans (emerging, non‑normative)
If prohibited‑practice bans are introduced (e.g., non‑consensual sexual deepfakes), providers SHOULD emit `content.generation.refuse` with:
- the policy snapshot in force,
- refusal reason and category,
- evidence pointer for audit and dispute resolution.

## Jurisdiction + trusted origin (non‑normative)
For AI media as a service, providers MAY return **jurisdiction and provenance metadata** (headers or evidence pointers), e.g.:
- `ai_provider_id`
- `processing_jurisdiction`
- `model_id` / `model_version`
- `policy_snapshot_id`
- `provenance_ref` (optional)

Apps SHOULD only display “trusted origin” claims when they can dereference provenance evidence, not merely on provider assertion.

## UI trust defaults (non‑normative)
Industry can act ahead of regulation here: if provenance or jurisdiction is **unknown**, apps SHOULD treat content as **untrusted** by default (no trust badge or a neutral warning).  
For high‑impact contexts (elections, public information, crisis response), apps SHOULD require evidence‑backed provenance and jurisdiction metadata before displaying content without warnings.

### Delegation context (internal evidence only)
If media actions are performed by delegated agents, evidence events SHOULD include delegation attributes (not for public disclosure):
- `delegation_id`, `delegator_id`
- `agent_class_id`, `agent_instance_id`, `session_id`
- `intent_ref` / `purpose_id` (when disclosure is required)

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
