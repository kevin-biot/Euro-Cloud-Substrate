# SlapOS Archetype (Non-Normative)

## Intent
Map ECS planes to the SlapOS master/compute architecture (ERP5 master, SlapGRID, Buildout/Supervisord, computer partitions).

## Plane-to-component mapping (illustrative)
| ECS plane | SlapOS-aligned components | ECS mapping considerations |
|---|---|---|
| Plane A — Identity/Authority | SlapOS Master (ERP5), X.509 certificate issuance for users/compute nodes/instances | Map authority bindings to issued certificates and allocation records |
| Plane B — Control Plane/LZ | SlapOS Master portal and allocation logic, service catalog | Map admission/refusal to ECS evidence events |
| Plane C — Execution Envelopes | Compute nodes with SlapGRID managing computer partitions (lightweight containers); optional VM inside partition | Map partition selection and lifecycle to envelope evidence |
| Plane D — Data & Evidence | Resource accounting collected by SlapGRID and sent to master; object storage integration for evidence | Map accounting and evidence persistence to ECS evidence/export requirements |
| Plane E — Interop & Portability | SlapOS Web portal/Web services for instance requests and provisioning | Align portal/APIs with ECS interop surface |

## Control and evidence flow (Mermaid)
```mermaid
flowchart TB
    Master[SlapOS Master (ERP5)] -->|Allocation decisions| SlapGRID[SlapGRID]
    SlapGRID -->|Install software| Buildout[Buildout]
    SlapGRID -->|Run services| Supervisord[Supervisord]
    Supervisord --> Partitions[Computer Partitions]
    Partitions --> Storage[Data/Evidence Storage]
    SlapGRID -->|Accounting/Evidence| Master
```

## Notes
- Master holds state; compute nodes are stateless and request what to install/run.
- Computer partitions provide lightweight isolation; stronger isolation can be layered with VM/TEE where needed.
