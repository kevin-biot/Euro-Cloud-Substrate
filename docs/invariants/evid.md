# Evidence Invariants (EVID) — Draft

## Scope
- Applies to evidence generation, integrity, completeness, and export.
- Covers local persistence, reconciliation, and evidence as first-class output.

## Invariants
- **EVID-01 — Evidence as First-Class Output**  
  Governed actions MUST emit evidence events.
- **EVID-02 — Local Evidence Persistence**  
  Evidence MUST persist locally under partition/connection loss.
- **EVID-03 — Evidence Integrity Guarantees**  
  Evidence MUST be integrity-protected (hash chains, signatures).
- **EVID-04 — Evidence Completeness Baseline**  
  Minimum evidence sets MUST be defined and met.
- **EVID-05 — Deferred Evidence Synchronisation**  
  Buffered evidence MUST be synchronised with reconciliation evidence.

## Evidence expectations
- Canonical event schemas and required fields.
- Hash-chain or signature proofs.
- Buffering and reconciliation records.
- Export bundles per `docs/evidence/export-schema.md`.

## Non-goals
- No mandated storage backend or logging technology.
- No regulator-specific reporting format requirements.
