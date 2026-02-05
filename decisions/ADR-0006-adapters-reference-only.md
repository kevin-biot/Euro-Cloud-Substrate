# ADR-0006: Adapters Are Reference Implementations Only

## Status
Proposed

## Context
ECS defines contract‑level requirements (evidence, authority, policy, portability). Adapters are small reference implementations that demonstrate how to emit evidence at key control points (admission, inference, storage). There is a risk that readers treat adapters as mandatory implementation stacks or certification paths.

## Decision
- Adapters are **reference implementations** only.
- They **do not define conformance** or certification.
- Providers may be ECS‑conformant without adopting any adapter.
- Adapters exist to prove **contract fidelity**, refusal semantics, and exportability in minimal code.

## Consequences
- Keeps ECS implementation‑neutral.
- Prevents vendor lock‑in around adapter code.
- Encourages multiple implementations and ecosystems to emit ECS evidence.
