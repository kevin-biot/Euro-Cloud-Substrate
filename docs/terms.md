# ECS Terms (Draft)

## Evidence event
An evidence event is a **Core10-05 envelope** emitted continuously for a governed action or system state change. It includes identity/context, outcome, ordering fields, and an `evidence_pointer`.

## Evidence artifact
An evidence artifact is the **content-addressed, immutable object** referenced by an `evidence_pointer` (e.g., policy snapshot, authority graph, SBOM, consent token). Artifacts are verifiable without trusting the emitter.

## Evidence bundle / export
An evidence bundle (export) is a **manifest + event range + referenced artifacts + verification inputs** (chain segment, hashes, signatures/seals, anchor refs). Bundles are the portable unit for audit, procurement, and regulator review.
