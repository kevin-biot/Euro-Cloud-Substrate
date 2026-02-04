# How Open-Source Projects Can Adopt ECS (Draft)

## 1. Why ECS fits open source unusually well
Most OSS projects struggle with governance credibility, not capability.
They already have:
- transparent code
- neutral licensing
- community trust
- wide deployment

What they often lack is a credible, portable way to say:
"This system enforces policy, authority, residency, and AI governance in a way that survives audits, exits, and disputes."

ECS supplies that contract layer without turning a project into a platform or a certifier.

## 2. How OSS projects can adopt ECS without scope explosion
ECS is a contract layer, not a framework. Projects can opt in with narrow, optional changes.
Three adoption patterns cover most cases.

## 3. Three adoption patterns

### Pattern A — Evidence emission (lowest friction, highest ROI)
**Who this fits**
- storage systems (Ceph, MinIO)
- orchestration tools
- ML tooling
- policy engines
- identity systems

**What they add**
- emit Core10-05 evidence events at key decision points
- support evidence_profile_id selection
- provide a basic export bundle

**What they gain**
- immediate relevance for regulated buyers
- a concrete answer to "how do you prove this?"
- inclusion in sovereign/public-sector shortlists

**They do not need to**
- implement all profiles
- make compliance claims
- change core architecture

### Pattern B — Profile alignment (opt-in credibility)
**Who this fits**
- mature OSS projects
- foundations
- infrastructure building blocks

**What they do**
- declare support for one or more evidence profiles:
  - baseline
  - regulated-ML
  - NCP (where applicable)
- document which invariants they cover and which they do not

**What they gain**
- a precise credibility signal
- fair comparison against managed services
- defense against vague "sovereign" marketing

### Pattern C — Reference adapter ownership (ecosystem leadership)
**Who this fits**
- Kubernetes distros
- ML stacks
- object storage projects

**What they do**
- maintain a small ECS adapter:
  - admission hook
  - sidecar
  - exporter
- keep it minimal and optional

**What they gain**
- position as a governance-ready building block
- pull-through adoption via procurement requirements
- influence without capture

## 4. What ECS does not ask OSS projects to do
OSS projects are not asked to:
- certify compliance
- make legal claims
- host evidence
- act as auditors
- guarantee sovereignty

They only:
- emit verifiable facts
- document invariants
- support export

Everything else happens outside the project (deployers, operators, verifiers).

## 5. Why this matters now
OSS projects are squeezed between:
- hyperscaler value-add layers
- sovereign procurement requirements
- AI governance obligations they did not design for

Without ECS, they get:
- adopted silently
- wrapped by platforms
- blamed when audits fail
- excluded when evidence is demanded

With ECS, they can say:
"We provide the primitives and the proof. How you govern and operate is your choice."

## 6. How to message this to OSS communities
Do not lead with sovereignty or regulation. Lead with:
- portability
- evidence export
- fair comparison
- not being wrapped without credit
- remaining neutral and upstream

Simple framing:
"ECS lets your project participate in regulated and sovereign environments without becoming a platform, a certifier, or a political actor."

## 7. Quick adoption checklist (minimal)
- emit Core10-05 evidence events for key decisions
- support evidence_profile_id selection
- provide a basic export bundle
- document covered invariants

## References
- Evidence profiles: `docs/profiles/evidence-profiles.md`
- Evidence bundles: `docs/examples/evidence-bundles/`
- Reference adapter: `adapters/k8s-admission/`
- RFP guide: `docs/rfp-evidence-support.md`
