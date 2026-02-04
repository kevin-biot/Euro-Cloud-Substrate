# WS5 Invariants (Draft)

- **EVID-WS5-01 Canonical envelope**  
  Evidence events MUST follow the Core10‑05 envelope.

- **EVID-WS5-02 Integrity and chaining**  
  Hash chaining MUST be applied when required by the selected evidence profile.

- **EVID-WS5-03 Query integrity**  
  Audit queries MUST preserve ordering and integrity proofs.

- **EVID-WS5-04 Exportability**  
  Evidence MUST be exportable with declared `evidence_profile_id` and verifier inputs.

- **EVID-WS5-05 Partition reconciliation**  
  Evidence buffered during partitions MUST reconcile to the main chain without loss.
