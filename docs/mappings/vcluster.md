# vCluster Mapping (Draft, Non‑Normative)

## What vCluster is (short)
vCluster provides **virtual Kubernetes clusters** with separate control planes while sharing or isolating worker nodes depending on the tenancy model.

## Tenancy models (as described in vCluster docs)
- **Shared Nodes**: workloads from multiple virtual clusters run on the same physical nodes; control planes are isolated, node‑level isolation is not.
- **Dedicated Nodes / Virtual Nodes**: control plane is isolated; workloads are constrained to specific node sets or virtual nodes on a shared host cluster.
- **Private Nodes / Standalone**: strongest isolation; workloads run on dedicated nodes and are not synced to a host cluster. Standalone runs the control plane as a binary on its own nodes.

## ECS mapping (execution envelopes)
| vCluster model | ECS envelope interpretation | Notes |
|---|---|---|
| Shared Nodes | Multi‑tenant container envelope | Strong API isolation; weaker node isolation |
| Dedicated / Virtual Nodes | Tenant‑scoped container envelope | Better node boundaries, still shared infra |
| Private Nodes / Standalone | Regulated / CRP‑grade envelope | Strongest isolation; best fit for regulated workloads |

## Where ECS adds requirements
vCluster focuses on tenancy mechanics; ECS adds governance contracts:
- **Authority/policy snapshots** bound to each governed action.
- **Refusal evidence** when policy or routing constraints block actions.
- **Evidence export bundles** for portability and audit.
- **Jurisdiction‑aware routing evidence** for cross‑border flows.

## Compatibility summary
vCluster can be an **execution envelope implementation** within ECS, but it must emit ECS‑compatible evidence events and support export bundles to meet ECS profiles.

## Reverse‑playbook portability (context)
vCluster Auto Nodes reuses AWS‑originated Karpenter, but packages it as a **portable managed capability** outside AWS.  
This is a practical example of “reverse‑playbook portability” aligned with ECS: extract a capability from a hyperscaler stack and make it portable across environments.
