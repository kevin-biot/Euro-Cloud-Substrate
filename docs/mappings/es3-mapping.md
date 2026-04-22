# ES3 Sovereign Stack Standard Mapping (Draft, Non-Normative)

## Purpose
Map the publicly described **European Sovereign Stack Standard (ES3)** from Schwarz Digits to ECS invariants, profiles, and evidence artifacts.

This note is not an endorsement, certification claim, or competitive ranking. It is a practical crosswalk for providers and evaluators asking how an ES3-style sovereignty assessment could be backed by portable runtime evidence rather than brochure assertions.

## Publicly confirmed shape
From Schwarz Digits' 17 April 2026 press release and LinkedIn launch post, the following points are public and attributable:
- ES3 is presented as a European standard for cloud solutions and IT services.
- It uses a **four-stage maturity model**: `Basic`, `Initial`, `Advanced`, `Future-Proof`.
- It is aimed at **industry, Mittelstand, and regulated sectors**, not only public procurement.
- The model is described as using **more than 100 criteria**.
- Schwarz Digits says BDO verified the maturity model.
- Schwarz Digits says the model **follows the structure, values, and principles** of the European Commission Cloud Sovereignty Framework (CSF).

Sources:
- Schwarz Digits press release: [European Sovereign Stack Standard](https://schwarz-digits.de/presse/archiv/2026/european-sovereign-stack-standard)
- Schwarz Digits launch post: [LinkedIn post](https://de.linkedin.com/posts/schwarz-digits_es-hm26-schwarzdigits-activity-7451887736413892608-n5wx)
- European Commission CSF baseline: [Cloud Sovereignty Framework v1.2.1](https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en?filename=Cloud-Sovereignty-Framework.pdf)
- Commission procurement use of CSF: [17 April 2026 news](https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en)

## Reported but not yet fully specified in public primary material
Secondary descriptions, including the user-supplied article in this thread, describe ES3 as:
- extending the CSF with a dedicated **AI** dimension,
- evaluating each dimension across **regulatory**, **organisational**, and **technological** layers,
- applying a **minimum principle** where the weakest dimension constrains the overall result.

Those points are plausible and coherent, but they are not all spelled out in the Schwarz primary materials above. Treat them as working assumptions until Schwarz publishes full methodology.

## Why ECS should map it
CSF defines a procurement baseline. ES3 appears to translate that baseline into an industry maturity model. ECS is useful underneath both because it defines the runtime proof layer:
- authority before execution,
- policy snapshots at decision time,
- refusal as a first-class evidenced outcome,
- portable evidence export,
- verifier-friendly bundles independent of provider tooling.

If ES3 becomes commercially influential, providers will need a concrete answer to: **what evidence proves my claimed maturity level?**
ECS is one candidate answer to that implementation gap.

## CSF vs ES3 vs ECS
| Aspect | EC CSF | ES3 | ECS |
|---|---|---|---|
| Primary role | Public procurement framework | Industry/vendor maturity model | Runtime evidence and portability contract |
| Public owner | European Commission | Schwarz Digits | Open architectural definition project |
| Core lens | 8 sovereignty objectives + SEAL + weighted score | 4-stage maturity model, reportedly more granular operationalization | Invariants, profiles, refusal semantics, exportable evidence |
| Evaluation unit | Bid / service offering | IT service / stack maturity | Execution path, control point, evidence bundle |
| Strength | Political legitimacy and procurement anchor | Market-facing operationalization | Verifiable runtime proof and provider-neutral export |
| Main gap | Says what to assess, not how to emit proof | Appears vendor-centered unless evidence is portable | Does not itself assign badges or market scores |

## Mapping logic
Where ES3 claims a maturity level, ECS asks four hard questions:
- What authority approved the action?
- What policy and constraint set applied at execution time?
- What artifact proves the outcome or refusal?
- Can an independent verifier validate it without privileged provider access?

If those answers are weak, the maturity claim is weak even if the contractual story is strong.

## ES3-style dimensions to ECS mapping
The first eight rows track the Commission CSF objectives because Schwarz states ES3 follows the CSF structure. The ninth AI row is included as a working extension because that is the most plausible and most useful industrial addition.

| ES3 dimension or area | ECS mapping | Evidence examples | Likely gap ECS closes |
|---|---|---|---|
| Strategic sovereignty | `docs/domains/sovereignty-assurance.md`, `core10/04-policy-authority-interface.md` | authority map, change-of-control artifact, operator/control declarations | Moves claim from org chart narrative to verifier-readable authority evidence |
| Legal and jurisdictional sovereignty | `core10/01-olz-eu-baseline.md`, `docs/domains/federation.md`, `docs/evidence/refusal-semantics.md` | jurisdiction policy snapshot, compelled-access refusal trace, corridor/routing evidence | Makes jurisdiction enforceable at runtime rather than contractual only |
| Data sovereignty | `core10/03-eosc-metadata-spec.md`, `docs/guides/data-object-binding-model.md`, `docs/evidence/catalog.md` | object bindings, data lineage records, deletion/export evidence, key-custody artifacts | Gives portable proofs for residency, custody, deletion, propagation |
| Operational sovereignty | `crp/README.md`, `docs/deployment-profile.md`, `docs/conformance/runtime-smoke-tests.md` | partition-mode evidence, control-plane continuity artifacts, migration/exit artifacts | Distinguishes availability from continuity under crisis or provider disruption |
| Supply chain sovereignty | `docs/invariants/sup.md`, `docs/compliance/pattern-library.md` | SBOMs, provenance set, dependency graph, supplier visibility artifacts | Adds structured export and verifier checks instead of checklist-only declarations |
| Technology sovereignty | `core10/08-interop-api-surface.md`, `core10/10-exit-interop.md`, `docs/mappings/aws-to-eu-cloud-service-map.md` | API schemas, portability bundles, adapter evidence, refusal traces for unsupported interop | Makes portability measurable through artifact export, not architecture slides |
| Security and compliance | `core10/05-evidence-event-model.md`, `core10/06-audit-chain-custody.md`, `docs/evidence/export-schema.md` | chain-segment records, incident evidence, immutable evidence events | Replaces provider-log dependence with portable, verifier-friendly evidence chains |
| Sustainability | outside ECS core; optional link-out only | external environmental disclosures | ECS intentionally does not score environmental posture |
| AI sovereignty (working extension) | `docs/profiles/regulated-ml/`, `docs/evidence/ontology.md`, `docs/examples/evidence-operations/`, `docs/evidence/verifier-responsibilities.md` | model SBOM, dataset manifest, training/inference lineage, refusal evidence, policy outcome traces | Gives concrete proof for model provenance, dependency custody, decision traceability |

## If ES3 uses regulatory / organisational / technological layers
If the reported three-layer model is correct, ECS fits mainly in the **technological** layer, but it also strengthens the other two.

| ES3 layer | What ECS can support | What ECS does not replace |
|---|---|---|
| Regulatory | machine-readable policy snapshots, refusal evidence, legal-demand handling artifacts | legal interpretation, contract drafting, regulatory sign-off |
| Organisational | authority maps, operator role declarations, control ownership evidence | governance committees, board accountability, procurement decisions |
| Technological | runtime events, audit chains, lineage continuity, portability and continuity tests | the platform itself |

This matters because many sovereignty programmes over-weight the first two layers. ECS is useful precisely because it hardens the third.

## Maturity interpretation hook
A practical ECS reading of the four ES3 stages would be:

| ES3 stage | ECS-oriented interpretation |
|---|---|
| Basic | documentation exists, but evidence is mostly declarative and provider-bound |
| Initial | some control points emit evidence; portability and refusals are partial |
| Advanced | critical control points emit verifier-friendly evidence; exit, continuity, and custody are demonstrable |
| Future-Proof | evidence is portable, refusal-capable, crisis-resilient, and largely independent of proprietary provider tooling |

This is not Schwarz's scoring model. It is an implementation interpretation for ECS adopters.

## Where ECS is stronger than public ES3 descriptions
Based on public material available on 22 April 2026, ECS is more explicit on:
- **refusal semantics**,
- **portable evidence export**,
- **runtime evidence ontology**,
- **object binding and lineage continuity**,
- **crisis partition behavior**,
- **verifier mode** (`public`, `export bundle`, `privileged access`).

These are the areas most likely to matter when a sovereignty claim is challenged under audit, incident response, or procurement dispute.

## Where ECS is weaker or deliberately different
ECS does not currently provide:
- a commercial badge system,
- a branded maturity score,
- a market-facing presales assessor,
- a single overall sovereignty rating.

That is intentional. ECS defines evidence contracts and constraints, not a commercial labeling programme.

## Practical repo implication
If ECS wants to remain useful as CSF and ES3 gain traction, the repo should continue to sharpen:
- verifier-accessible artifact sets per sovereignty objective,
- concrete provider implementation kits,
- AI/data sovereignty evidence for training and inference,
- procurement-facing mappings that separate threshold evidence from score-improving evidence.

## Suggested use of this mapping
Use this document when:
- a provider says it is aligning to ES3 and needs a concrete evidence design,
- a buyer wants to distinguish maturity marketing from runtime proof,
- a working group needs to separate procurement scoring from implementation semantics.

## Related ECS docs
- `docs/mappings/ec-cloud-sovereignty-framework-mapping.md`
- `docs/mappings/eu-sovereignty-assurance-matrix.md`
- `docs/domains/sovereignty-assurance.md`
- `docs/evidence/export-schema.md`
- `docs/evidence/refusal-semantics.md`
- `docs/profiles/regulated-ml/README.md`
