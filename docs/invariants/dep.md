# Dependency Invariants (DEP) — Draft

## Scope
- Applies to services/workloads designated critical within an ECS deployment.
- Dependency includes technical services, platforms, providers, operators, and non-substitutable components on execution, authority, policy, data, and evidence paths.

## Invariants
- **DEP-01 Critical Path Identification**  
  - Define critical dependency paths for governed services (compute, storage, network, identity, policy, evidence).
- **DEP-02 Non-Substitutable Dependency Declaration**  
  - Explicitly declare any dependency without a viable substitute (technical, contractual, geographic).
- **DEP-03 Exclusivity Constraint**  
  - A single actor MUST NOT control a non-substitutable critical path unless explicitly accepted with compensating measures.
- **DEP-04 Dependency Evidence Exposure**  
  - Dependency structure MUST be observable and auditable (declared, versioned, exportable).

## Required evidence (examples)
- Dependency graph per critical service (including authorities, control-plane, data/evidence planes).
- Classification of dependencies: substitutable vs. non-substitutable; jurisdiction/operator ownership.
- Concentration metrics (e.g., spend/utilization per actor on critical path).
- Accepted exceptions with compensating controls and review cadence.

## Notes
- No tooling mandated; focus on declarations, observability, and evidence.
- Ties directly to EXIT/INT (portability), CRP (rupture tolerance), and IRN RES-2.3/2.4.
