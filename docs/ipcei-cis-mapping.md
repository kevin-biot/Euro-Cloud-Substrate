# IPCEI‑CIS Reference Architecture v2.0 → ECS Mapping (Draft)

## Purpose
Provide a crosswalk between the IPCEI‑CIS Reference Architecture (ICRA) v2.0 and ECS components, with emphasis on federation, portability, and evidence export.

## Source scope (ICRA)
ICRA v2.0 defines layered architecture (Application → Data → AI → Service Orchestration → Cloud‑Edge Platform → Virtualization → Network Systems → Physical) and cross‑cutting domains (Federation, Management, Security & Compliance, Sustainability). It is a high‑level, technology‑agnostic reference framework that organizes functional components and interfaces to guide pilots and federation across a multi‑provider cloud‑edge continuum.

## Layer‑by‑layer crosswalk (ICRA → ECS)
*Mapping is ECS‑specific interpretation.*

| ICRA layer | ICRA intent (summary) | ECS mapping (Core10 / WS / invariants) |
|---|---|---|
| Application | End‑user applications, functions, and catalogs. | Core10‑08 (interop API surface), WS4 interop APIs, INT/EXIT invariants for portability. |
| Data | Data collection/processing/exchange across the continuum. | WS2‑EOSC (governed object storage), DATA/EVID invariants, evidence export schema. |
| AI | Distributed AI lifecycle (training/inference/agents). | Regulated‑ML profile, ML evidence events, SUP/EVID/EXEC invariants. |
| Service Orchestration | Multi‑provider orchestration and lifecycle management. | WS3 execution envelopes, WS4 interop APIs, Core10‑07/08. |
| Cloud‑Edge Platform | Resource allocation/lifecycle mgmt across providers. | Core10‑01 (OLZ‑EU), Core10‑07 (envelopes), WS1/WS3. |
| Virtualization | Abstraction over physical compute/storage/network. | EXEC/DEP/PHY invariants, VM envelope profile (Core10‑07), WS3. |
| Network Systems | Network management across the continuum. | PHY invariants, CRP partition resilience, WS3/CRP. |
| Physical | Physical compute/storage/network resources. | PHY/DEP invariants, CRP assumptions. |

## Federation components → ECS interop/export roles
ICRA defines two core federation components: **Federation Manager** (negotiates federation, access, onboarding, accounting; enables allocation/scale across providers via compatible APIs) and **Federation Broker** (service marketplace / on‑demand bundle discovery).

ECS mapping:
- **Federation Manager** → WS4 interop APIs + WS6 migration + Core10‑08/10 (portable APIs, export/import, evidence of success/refusal).
- **Federation Broker** → Interop API discovery + profile claims + evidence bundle contracts (export manifests and verifier inputs).
- **Federation domain portability** aligns with ECS export bundles and evidence profiles; ECS supplies contract‑level evidence artifacts for auditability and switching.

## Gaps / extensions (ECS beyond ICRA’s high‑level scope)
ICRA is intentionally high‑level and technology‑agnostic; it focuses on component placement and functional interfaces rather than specifying evidence bundle semantics.

ECS adds:
- **Evidence profiles + profile claims** (baseline/admissible/NCP/regulated‑ML) as procurement‑grade declarations.
- **Deterministic evidence bundles** (manifest + chain segment + verifier inputs) as portable audit artifacts.
- **No‑Control Profile (NCP)** proof artifacts for jurisdictional exposure control.

## Notes
This mapping does **not** claim ICRA and ECS are equivalent; it shows how ECS supplies the missing contract layer (evidence and export semantics) within the ICRA’s conceptual structure.
See `docs/federation-domain.md` for the ECS federation domain summary and evidence expectations.
