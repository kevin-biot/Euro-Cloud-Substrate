# Hash Profile Registry (Draft)

## Intent
Provide a minimal, shared registry of hashing profiles so independent implementations compute identical hashes without coordination.

## ecs-hash-v1 (draft)
**Status:** baseline profile for ECS ML evidence.

### Canonicalisation rules
- Input is the exact byte sequence of the canonical payload (after normalisation rules below).
- Hash algorithm: `sha256`.
- For structured payloads, hash the canonical JSON bytes only (no surrounding transport or envelope fields).

### Normalisation rules
- JSON objects MUST be canonicalised by:
  - UTF-8 encoding.
  - Lexicographic ordering of object keys.
  - No insignificant whitespace.
  - Normalised newline as `\n`.
- Arrays preserve order.
- Numeric values use canonical JSON formatting (no trailing zeros).

### Exclusion rules
- Raw PII (e.g., names, emails, IPs) MUST NOT be hashed unless explicitly required by policy and documented.
- Secrets (tokens, keys, credentials) MUST NEVER be included.
- Transport metadata (HTTP headers, TLS info) is excluded unless the collision domain explicitly includes it.

### Salt / pepper guidance
- Salting or peppering is **not allowed** in `ecs-hash-v1` for portability.
- If privacy requires salting, define a new profile (e.g., `ecs-hash-v1-salted`) and document salt storage and verifier access.

### Collision domain statement
`input_hash` represents **request payload only** (payload bytes after normalisation). It does **not** include:
- transport headers
- policy snapshot ids
- retrieval context

If a deployment requires payload+context, define a new profile and declare it explicitly.

### Determinism statement
A verifier with the same canonical payload MUST be able to recompute the hash and match the emitted value without platform access.

## Adding new profiles
New profiles must:
- Declare canonicalisation and exclusion rules.
- Specify collision domain.
- State determinism guarantees and verifier requirements.
