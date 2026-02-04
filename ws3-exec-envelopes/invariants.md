# WS3 Invariants (Draft)

- **ENV-01 Envelope declaration**  
  Workloads MUST declare an execution envelope (container/VM/TEE) prior to admission.

- **ENV-02 Policy‑driven admission**  
  Admission controls MUST enforce policy‑driven envelope selection and refusal with evidence.

- **ENV-03 Profile controls enforced**  
  Profile‑specific controls (isolation, integrity, network posture) MUST be applied before execution.

- **ENV-04 Evidence for lifecycle and attestation**  
  Deployment, start/stop, and attestation events MUST emit evidence with snapshot IDs and outcomes.

- **ENV-05 Partition tolerance for CRP**  
  CRP envelopes MUST continue under local control; evidence is buffered and reconciled post‑partition.
