# WS1 Diagram (Mermaid)

```mermaid
flowchart LR
    Tenant[Tenant / Project] --> Identity[Identity Binding]
    Identity --> Authz[Authority Points]
    Authz --> Network[Network Segmentation & Egress Control]
    Authz --> Policy[Policy Baseline (Default Deny)]
    Policy --> Audit[Audit / Evidence Events]
    Network --> Landing[Landing Zone Resources]
```
