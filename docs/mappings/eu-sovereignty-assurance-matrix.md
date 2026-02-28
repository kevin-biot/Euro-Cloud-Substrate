# EU Sovereignty Assurance Matrix (Draft, Non-Normative)

## Purpose
Provide a single crosswalk for sovereignty-oriented claims so deployers, auditors, and procurement teams can verify enforceable control (not just residency statements).

This matrix is indicative and architecture-focused. It does not provide legal advice or certification.

## How to use
- Pick the claimed assurance area.
- Check the ECS surface and required artifacts.
- Run verifier checks against exported evidence bundles.
- Record gaps and compensating controls explicitly.

## Matrix
| EU assurance area (indicative) | ECS surface | Required artifacts/events | Verifier checks | Gap signal / refusal expectation |
|---|---|---|---|---|
| Legal authority chain (controller/processor/subprocessor, governing-law context) | `docs/domains/sovereignty-assurance.md` (surface 1), `core10/04-policy-authority-interface.md`, `docs/conformance/model.md` | Authority map artifact, policy snapshot references, control-plane ownership declaration | Artifact exists, immutable reference resolves, decisions reference snapshot IDs used at run time | Missing authority map or unresolvable snapshot should fail claim |
| Compelled disclosure handling (technical and legal constraint posture) | `docs/domains/sovereignty-assurance.md` (surface 2), `docs/profiles/no-control-profile.md`, `core10/09-fail-closed-profile.md` | Legal-demand handling artifact, refusal events, policy/authority snapshot references | Refusal decisions are reproducible from declared policy and authority state | Demand handling not evidenced or no refusal path for disallowed case |
| Trust-root provenance (IdP/CA/KMS ownership and custody) | `docs/domains/sovereignty-assurance.md` (surface 3), `docs/domains/iam.md`, `docs/domains/data-security.md` | Trust-root declaration artifact, key-custody artifact, trust-root change audit events | Trust anchors and key custody are attributable, scoped, and time-bounded | Undeclared trust anchor or opaque break-glass ownership |
| Identity federation and cross-border identity handling | `docs/domains/iam.md`, `docs/domains/eudi-wallet-integration.md`, `ws4-interop-api/spec.md` | Credential verification events, issuer validation evidence, cross-border matching outcome evidence where used | Signature/issuer/audience/expiry checks evidenced; delegated actions attributable | Invalid/expired/unknown issuer should produce refusal evidence |
| Non-human identity and delegation controls (agents/services) | `docs/guides/agent-delegation.md`, `docs/domains/iam.md`, `docs/domains/sovereignty-assurance.md` (surface 4) | Delegation issue/revoke events, delegated action evidence with scope/expiry, refusal events for scope violations | Delegation is time-bounded, scoped, revocable, and bound to actor instance/session | Missing delegation proof or out-of-scope action without refusal |
| Jurisdiction-aware routing and path control | `docs/domains/federation.md`, `docs/architecture/control-plane.md`, `docs/invariants/data.md` | Routing policy artifacts, jurisdictional refusal events, telemetry path audit artifacts | Routing/refusal outcomes align with declared jurisdiction policy snapshots | Cross-border fallback without evidence or refusal trace |
| Audit chain integrity and independent verification | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-custody.md`, `docs/evidence/export-schema.md`, `docs/evidence/verifier-responsibilities.md` | Export bundle (`manifest`, `events`, `chain-segment`, verifier inputs), profile claim, artifact refs | Chain continuity, pointer integrity, profile-constrained checks all pass without provider-private access | Broken chain continuity, unresolved artifact refs, or profile mismatch |
| Exit and portability assurance | `ws6-migration/spec.md`, `docs/deployment-profile.md`, `core10/10-exit-interop.md` | Dependency/exit artifacts, export bundle portability evidence, refusal evidence for unsupported capabilities | Bundle and control evidence can be validated after provider move | Portability claim without reproducible export/verification trail |

## Minimum evidence package for sovereignty claims
Recommended baseline package:
1. Declared `evidence_profile_id` and claim scope.
2. Authority and trust-root artifacts (immutable refs).
3. Export bundle with verifier inputs.
4. At least one refusal case (policy/jurisdiction/delegation) with chain evidence.
5. Gap register with compensating controls and retest date.

## Related ECS references
- `docs/domains/sovereignty-assurance.md`
- `docs/mappings/ec-cloud-sovereignty-framework-mapping.md`
- `docs/mappings/reg-mapping.md`
- `docs/profiles/no-control-profile.md`
- `docs/profiles/evidence-profiles.md`
- `docs/evidence/verifier-responsibilities.md`
