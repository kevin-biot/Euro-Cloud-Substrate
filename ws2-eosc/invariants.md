# WS2 Invariants (Draft)

- **EOSC-01 Mandatory governance metadata**  
  Objects MUST carry governance metadata; writes without it MUST fail.

- **EOSC-02 Metadata preservation**  
  Governance metadata MUST persist across copy/move/replication and export/import.

- **EOSC-03 Jurisdiction enforcement**  
  Placement and replication MUST honor declared jurisdiction; violations MUST be refused and evidenced.

- **EOSC-04 Integrity validation**  
  Integrity hashes MUST be validated on write; optional read validation MUST produce evidence on mismatch.

- **EOSC-05 Retention and immutability**  
  Retention/immutability controls MUST be enforced; delete/overwrite MUST be refused when locked and evidenced.

- **EOSC-06 Evidence emission and exportability**  
  Compliance‑relevant operations MUST emit evidence events and be exportable with profile declaration.

- **EOSC-07 Usage receipts for governed access**  
  Governed GET/EXPORT operations MUST emit usage receipt evidence when applicable.
