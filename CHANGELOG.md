# Changelog

All notable changes to this project are documented here.

This changelog was retrofitted after the repo had already accumulated substantial history.
Entries through `2026-04-23` are reconstructed from git history and grouped by meaningful
architecture and implementation milestones rather than by every individual commit.

## Unreleased
- No unreleased entries yet.

## v0.1.0 - 2026-04-23
- Fixed reference binding semantics in `adapters/common/object_binding.py`:
  - `binding_id` now identifies an immutable binding revision.
  - `binding_key` now identifies the stable object/purpose attachment scope.
- Fixed native API/queue header projection to use the documented hyphenated `X-ECS-*` wire format.
- Fixed runtime demo startup flakiness by replacing fixed sleep with readiness polling and log-tail failure output in `docs/examples/runtime/run-demo.sh`.
- Updated binding model and helper docs to reflect revision-vs-identity semantics.

## 2026-04-22
- Added ES3 sovereignty mapping in `docs/mappings/es3-mapping.md`.
- Added explicit ES3 strengths vs remaining gaps analysis, with emphasis on:
  - runtime evidence gaps,
  - verifier portability,
  - crisis posture,
  - AI proof under-specification.
- Added cross-jurisdiction sovereignty minimum extraction in `docs/mappings/cross-geo-sovereignty-minimum.md`.
- Added jurisdictional fragmentation positioning note in `docs/mappings/jurisdictional-fragmentation.md`.
- Added SlapOS proof-of-implementability mapping in `docs/mappings/slapos-mapping.md`.
- Added regulated operations experience gap note in `docs/positioning/regulated-ops-gap.md`.

## 2026-03-31
- Added CDMC crosswalk in `docs/mappings/cdmc-mapping.md`.
- Positioned CDMC as a control-objective layer and ECS as the runtime proof/export layer.

## 2026-03-16
- Added lineage schema, required lineage/policy events, and verifier checks.
- Added MetaVox + Nextcloud mapping and clarified ID-bound metadata portability implications.
- Added data object binding model for portable metadata attachment across files, objects, queues, streams, datasets, model artifacts, and API responses.
- Added neutral object binding helper in `adapters/common/object_binding.py`.
- Added evidence ontology and JSON-LD context overlay.
- Added canonical operation-level evidence emission samples in `docs/examples/evidence-operations/`.
- Added runtime implementation kit:
  - `docs/guides/runtime-quickstart.md`
  - `docs/guides/runtime-reference-architecture.md`
  - `docs/guides/vendor-integration-playbook.md`
  - `docs/examples/runtime/`
  - `docs/conformance/runtime-smoke-tests.md`
- Added AWS-to-EU cloud service mapping for portability and provider implementation framing.
- Cleaned Python cache artifacts and updated `.gitignore`.

## 2026-02-28
- Added deployment and EU cloud coherence reports.
- Added sovereignty assurance surface and profile links.
- Added EU sovereignty assurance matrix.
- Added EUCS and EU Cloud CoC mapping set.
- Added EC Cloud Sovereignty Framework mapping.
- Added role guides, refusal semantics quick spec, and pilot pack.

## 2026-02-07
- Added training provenance risk notes.

## 2026-02-05
- Repo reached ~296 unique clones (Jan 17–Feb 4, 2026).
- Docs reorganized; architecture consolidated under `docs/architecture/` with diagrams index and deliverables map.
- CRP README added; CRP spec tightened with activation/exit criteria and evidence alignment.
- Federation minimum contract clarified; optional federation claims and portability limits added.
- Added SUSE CSF and Tech Sovereignty Catalogue mappings; mappings index added.
- Added data services (queues/streams) and edge/IoT domain notes.
- Added data space compatibility profile (non-normative).
- Regulated-ML evidence upgraded with data-use posture, dataset manifests (DSBOM), and governance phases; examples updated.
- Added optional data governance endpoints to WS4/Core10 interop.
- IAM clarified (authn vs authz, delegation scope/time bounds); EUDI delegation guidance expanded.
- Added competition and differentiation notes around CRDs, mesh, ingress, and evidence expectations.

## 2026-02-03
- Expanded Core10 deep-dives (01–10) with requirements, evidence, and conformance outlines.
- Added evidence export schema and aligned evidence catalog to envelopes, outcomes, usage receipts, and anchoring.
- Drafted compliance pattern library with JSON schema snippets and governance notes.
- Added ML evidence implementation note, deployer checklist, SDK proposal, and risk guidance.
- Updated architecture with archetypes, control-plane capabilities, and flow diagrams.
- Extended EOSC spec for data sharing, usage receipts, and block/file storage evidence.
- Expanded IRN mapping context; added conformance checklists/metrics and SOC/log control profile.
- Added EUDI wallet integration note with delegation/payment evidence events.
- Added qualified archiving guidance with chain anchoring references.
- Updated `SECURITY.md` with reporting, scope, and response expectations.

## Pre-changelog history
- Phase 0 declared complete; invariant set `v0.3` frozen in `docs/invariants/v0.3.md`.
- Core10 and workstreams linked to invariant families and IDs.
- IRN crosswalk drafted; profile guardrails defined.
- Deliverables diagrams added; conformance model drafted.
- EOSC storage spec iterated toward implementable governance metadata and evidence.
- Regulated ML profile added with SBOM, inference/training evidence, AI Act mapping, and conformance.
- OLZ requirements expanded with tenant lifecycle, OIDC federation, and network baseline.
- Interop API skeleton added with resources, auth, errors, versioning, and OpenAPI stub.
- Core10 governance trio drafted: policy/authority, evidence model, and audit chain.
- Tenant isolation, execution envelopes, fail-closed, and migration baselines moved to draft v1.
