# Jurisdictional Fragmentation — Architecture Note (Draft, Non-Normative)

## Purpose
Document the jurisdictional fragmentation problem in sovereign cloud — the pattern by which
multiple jurisdictions produce structurally similar sovereignty frameworks that are not
architecturally interoperable — and explain how ECS invariants provide a substrate-level
response that is independent of which jurisdiction's regulatory wrapper is applied.

This is a positioning note, not a mapping to a specific framework.

---

## The Copy-Paste Problem

Several major jurisdictions have produced cloud sovereignty frameworks:

| Jurisdiction | Example framework / instrument |
|---|---|
| European Union | AI Act, NIS2, DORA, EUCS, EC Cloud Sovereignty Framework |
| France | IRN (Infrastructure Numérique de Référence), HDS |
| GCC (Gulf Cooperation Council) | PDPL variants, CSP regulatory frameworks per member state |
| California (USA) | CCPA/CPRA, AB 2013 (AI transparency), SB 1047 (AI safety) |
| Colorado (USA) | Colorado AI Act (SB 205), Colorado Privacy Act |
| China | PIPL, Data Security Law, MLPS 2.0 |

Each framework claims to address data sovereignty, security, and accountability.
Each uses similar language: residency, access control, auditability, transparency.

**The problem:** the regulatory text is structurally similar, but the underlying
execution substrate — typically a hyperscale cloud provider — does not change between
jurisdictions. AWS running under a GCC regulatory wrapper is still AWS. The sovereignty
claim is contractual, not architectural.

Regulatory copy-paste creates the **illusion of alignment** while:
- The trust root remains outside local jurisdiction.
- The key management infrastructure is provider-controlled.
- The audit chain is reconstructed from mutable provider logs, not emitted at execution time.
- Crisis resilience depends on the hyperscaler's own continuity, not the customer's.
- Legal demands (court orders, administrative access) are governed by the provider's
  jurisdiction of incorporation, not the customer's regulatory wrapper.

---

## Why Contractual Sovereignty Is Insufficient

The Apple 2016 precedent (FBI v Apple) is the clearest real-world demonstration:

- A US court issued a lawful order to Apple.
- Apple refused — not because of contract — but because the **architecture** did not
  provide a key extraction mechanism.
- The root of trust was in hardware under the customer's control.
- No contractual sovereignty claim was required; the architecture enforced it.

Conversely: a cloud provider operating under a GCC sovereignty contract but with
US-headquartered key management infrastructure is exposed to US legal process
regardless of the contract's language. The contract redistributes liability.
It does not change the architecture.

**Sovereignty achieved contractually but not architecturally is liability redistribution,
not sovereignty.**

---

## The Fragmentation Consequence

As jurisdictions proliferate their own frameworks, operators face:

1. **Compliance theatre** — meeting the letter of multiple frameworks via contractual
   wrappers while the underlying execution substrate remains unchanged.
2. **Non-interoperable evidence** — each jurisdiction's audit/logging requirements
   produce evidence in formats that are not portable across jurisdictions.
3. **Irreconcilable crisis postures** — frameworks define resilience requirements
   differently; an operator compliant with EU NIS2 and GCC PDPL simultaneously
   may satisfy neither under actual crisis conditions.
4. **Stack fragmentation** — operators deploy separate infrastructure stacks per
   jurisdiction rather than a coherent substrate with jurisdiction-aware routing.

---

## ECS Response: Substrate-Level Invariants

ECS addresses fragmentation by defining sovereignty properties at the **execution substrate**
level, independent of which jurisdiction's regulatory wrapper is applied above it.

| Fragmentation problem | ECS invariant / profile | How it helps |
|---|---|---|
| Contractual trust root | Core10-04 (Authority Before Execution), `docs/domains/sovereignty-assurance.md` | Root of trust is declared, evidenced, and verifiable — not asserted in a contract |
| Mutable post-hoc logs | IALP (Immutable AI Workload Log Primitives), Core10-05/06 | Evidence emitted at execution time; not reconstructed from logs |
| Crisis dependency on hyperscaler | CRP (Crisis Resilience Profile) | Explicit partition/continuity posture; local authority evaluation; deterministic degradation |
| Non-portable evidence formats | Core10-10 (Portable Audit Surface), `docs/evidence/export-schema.md` | Provider-neutral export bundle; verifiable without provider-specific tooling |
| Jurisdiction-unaware routing | Core10-03 (EOSC metadata), `docs/domains/federation.md` | Jurisdiction metadata travels with data; routing decisions are evidenced and refusable |
| Irreconcilable resilience postures | CRP operational modes (Normal / Partition / Recovery) | Deterministic degradation modes are declared and auditable across any jurisdiction |

The key architectural principle: **ECS makes sovereignty properties verifiable
independently of which jurisdiction's framework names them.**

A GCC-regulated operator and an EU-regulated operator running ECS-conformant
infrastructure produce evidence bundles that are structurally identical and
independently verifiable. The regulatory wrapper above the substrate differs.
The substrate evidence contract does not.

---

## Coherence as a Measurable Substrate Property

Sovereignty frameworks tend to treat coherence as a design aspiration:
"we should avoid fragmentation" or "a small set of reference architectures
would help."

ECS treats coherence as a **verifiable substrate property**:

- Authority evaluation is deterministic given the same policy snapshot.
- Evidence bundles are structurally consistent across providers and jurisdictions.
- Refusal semantics are explicit and auditable.
- Degradation modes are predefined and evidence-emitting.

A coherent sovereignty substrate is not one where everyone agrees on the regulations.
It is one where the execution contract is consistent and verifiable regardless of
which regulatory layer sits above it.

---

## Procurement Implication

When evaluating sovereign cloud claims across jurisdictions, ask:

1. **Where does the root of trust live?** Who controls the key ceremony and HSM custody?
2. **Is evidence emitted at execution time or reconstructed post-hoc from logs?**
3. **Can you export a verifier-friendly evidence bundle without provider-specific tooling?**
4. **What happens on day one of a crisis?** Can the cluster evaluate policy and produce
   admissible evidence with upstream connectivity severed?
5. **Is the sovereignty claim architectural or contractual?** If the answer requires
   reading a contract rather than running a verifier, it is contractual.

These questions apply equally to EU, GCC, California, Colorado, and Chinese sovereignty
frameworks. The substrate either supports them or it does not.

---

## Related ECS Documents
- `VISION.md` — Core10 invariants and CRP
- `crp/README.md` — Crisis Resilience Profile
- `docs/mappings/reg-mapping.md` — EU regulatory mapping
- `docs/mappings/eu-sovereignty-assurance-matrix.md` — sovereignty assurance matrix
- `docs/domains/sovereignty-assurance.md` — sovereignty assurance surfaces
- `docs/evidence/export-schema.md` — portable evidence bundle format
- `docs/profiles/no-control-profile.md` — no-control posture profile

---

*This note reflects architectural observations and does not constitute legal advice
or certification guidance. Regulatory frameworks cited are subject to change.*
