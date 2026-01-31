# Supply-Chain Invariants (SUP) — Draft

## Scope
- Applies to critical software/firmware components in governed services.
- Covers upstream dependencies (direct and N-tier) required for execution, authority, policy, data, and evidence paths.

## Invariants
- **SUP-01 — Declared Supply-Chain Inventory**  
  All critical software and firmware components MUST be declared.
- **SUP-02 — Provenance Verifiability**  
  The origin and build process of critical artifacts MUST be verifiable.
- **SUP-03 — Upstream Dependency Disclosure**  
  Non-immediate (N-tier) critical dependencies MUST be disclosed.
- **SUP-04 — Opaque Supply Chain Fails Conformance**  
  Undeclared or unverifiable upstream dependencies MUST fail conformance.

## Evidence expectations
- SBOMs or equivalent inventories for critical components.
- Provenance attestations (build origin, signer, integrity).
- N-tier dependency disclosure (where it affects critical paths).
- Refusal/exception records when supply-chain visibility is insufficient.

## Non-goals
- No geopolitical risk scoring.
- No supplier morality or procurement strategy.
- No tooling mandates or country lists.
