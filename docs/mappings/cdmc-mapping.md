# CDMC -> ECS Mapping (Draft, Non-Normative)

## Purpose
Map EDM Council CDMC 14 Key Controls to ECS runtime evidence contracts.

Framing:
- CDMC defines control objectives and assessment expectations.
- ECS defines portable runtime evidence semantics (event envelope, chain, refusal, export).

## Source baseline
This mapping uses the public CDMC 14 Key Controls list and CDMC framework references:
- https://edmcouncil.org/frameworks/cdmc/14-key-controls/
- https://edmcouncil.org/wp-content/uploads/2023/06/CDMC_Framework_V1.1.1.pdf
- https://edmcouncil.org/wp-content/uploads/2023/02/CDMC-Information-Model-Controls-Tests-Mappings-V1.1.pdf

## Crosswalk summary
| CDMC control | ECS mapping | Evidence expectations | Coverage |
|---|---|---|---|
| 1. Data Control Compliance monitoring | `docs/conformance/metrics.md`, `policy.outcome.measure` | measurable control outcomes + exported bundle evidence | Strong |
| 2. Ownership in catalog | `docs/invariants/data.md` (`owner_id`), WS2 EOSC descriptor | ownership fields present + policy-bound access decisions | Strong |
| 3. Authoritative sources/provisioning register | DATA descriptor + AUTH/DEP declarations | authoritative source refs + provisioning decision evidence | Partial |
| 4. Data sovereignty / cross-border movement control | `docs/invariants/data.md`, `docs/domains/federation.md`, route refusals | jurisdiction metadata + explicit refusal evidence for disallowed routes | Strong |
| 5. Automated cataloging at creation/ingestion | `data.product.publish`, descriptor contract | publish-time metadata + chain-linked event evidence | Strong |
| 6. Automated always-on classification | DATA classification invariants | classification on governed events + refusal when missing | Strong |
| 7. Entitlements/access default + tracking | AUTH/POL + EXEC decision model | policy/authority-bound admit/refuse events + delegation tracking | Strong |
| 8. Consumption purpose for sharing | purpose/consent/terms events (`data.purpose.bind`, `data.consent.bind`) | purpose binding before access + refusal semantics | Strong |
| 9. Security controls enabled + evidenced | `docs/domains/data-security.md`, EVID/DEP artifacts | key custody/security posture artifacts + decision evidence | Partial-Strong |
| 10. DPIA triggers by jurisdiction | `docs/domains/privacy.md`, jurisdiction-aware policy checks | personal-data policy trigger evidence + refusal/hold outcomes | Partial |
| 11. Data quality measurement + distribution | `quality_score`, `quality_method_ref`, policy outcome metrics | quality evidence in lineage + policy outcome measurement events | Strong |
| 12. Retention/archiving/purging controls | DATA retention/erasure/export + qualified archiving references | retention + deletion propagation evidence + archive refs where used | Strong |
| 13. Data lineage availability | lineage schema + `data.transform.link` | parent-child continuity + purpose/consent propagation checks | Strong |
| 14. Cost metrics in catalog | usage metering evidence notes in DATA invariants | usage/cost receipts and catalog linkage for governed operations | Partial |

## Where ECS adds value beyond CDMC objective language
1. Deterministic event envelope and chain continuity (`event_hash`, `prev_hash`, `chain_id`).
2. Explicit refusal semantics (`outcome=refused` + reason taxonomy).
3. Verifier-friendly export bundle contract (`manifest`, `events.jsonl`, `chain-segment`, `verifier-inputs`).
4. Profile-constrained verification (`evidence_profile_id`, optional `hash_profile_id`).

## Practical adoption pattern
1. Use CDMC controls as assessment objectives.
2. Implement ECS events at runtime decision points.
3. Export ECS bundles as evidence artifacts for CDMC-aligned assessments.
4. Run independent verifier checks to reduce provider-private audit dependency.

## Suggested evidence pack for CDMC-aligned review
- `manifest.json` with selected profile.
- `events.jsonl` with governance decisions and refusals.
- `chain-segment.json` and `verifier-inputs.json`.
- Referenced artifacts (policy snapshots, authority bindings, lineage records, retention/deletion evidence).

## Limits / non-goals
- This mapping does not claim CDMC certification.
- Certification remains under CDMC program and authorized assessment processes.
- ECS remains mechanism-only and does not replace CDMC governance process.
