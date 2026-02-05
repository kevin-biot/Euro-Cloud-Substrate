# ADR-0005: Capability-Scoped AI Media Invocations (STA-L Pattern)

## Status
Proposed

## Context
AI media generation is typically exposed via generic APIs, which obscures when special duties apply (marking, disclosure, provenance, jurisdiction). This creates an enforcement gap: duties exist, but the API layer does not surface them or bind them to evidence.

A capability-scoped token pattern (similar to STA-L in other systems) allows each invocation to carry explicit duty declarations, TTL, scope, and policy/authority context, and gives evidence events a stable reference.

## Decision
ECS will treat AI media generation as a governed capability and recommend (non-normatively):
- Explicit AI-media fields on invocation requests/responses (content class, risk class, disclosure/provenance duties, jurisdiction).
- A scoped capability token reference (`capability_token_ref`) when using local or remote capability routers.
- Evidence events that bind to the capability token reference when duties are enforced or refused.

ECS remains mechanism-only; the token format is not mandated.

## Consequences
- API designers have a clear, portable way to distinguish AI media duties from generic content handling.
- Auditors can verify duty compliance at the invocation level using evidence references.
- Implementers can adopt the pattern incrementally without changing core execution envelopes.
