# WS3 Diagram (Mermaid)

```mermaid
flowchart LR
    Admission[Admission / Policy Gate] -->|profile select| EnvChoice{Envelope}
    EnvChoice -->|container| K8s[Kubernetes Controls]
    EnvChoice -->|vm| VM[VM Envelope (KubeVirt or equivalent)]
    K8s --> Evidence[Evidence Emission]
    VM --> Evidence
    Evidence --> Export[Audit / Export]
```
