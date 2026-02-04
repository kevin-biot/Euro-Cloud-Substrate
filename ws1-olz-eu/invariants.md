# WS1 Invariants (Draft)

- **OLZ-01 Authority binding on tenant creation**  
  Tenant/project/workspace creation MUST reference an authority snapshot and policy baseline; refusal MUST be recorded with evidence.

- **OLZ-02 Default-deny network posture**  
  Governed workloads MUST default to deny for egress/ingress; exceptions MUST be explicitly authorized and evidenced.

- **OLZ-03 Cross-tenant flow authorization**  
  Any cross-tenant flow MUST be explicitly authorized and recorded with evidence (policy snapshot IDs, outcome).

- **OLZ-04 Evidence emission for lifecycle actions**  
  All create/update/delete/suspend actions MUST emit evidence-grade events with authority/policy snapshot IDs.

- **OLZ-05 Connectivity dependency declaration**  
  Required connectivity dependencies (operators, paths, egress destinations) MUST be declared and evidenced.
