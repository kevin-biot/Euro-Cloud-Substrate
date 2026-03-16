# AWS to EU Cloud Service Map (Draft, Non-Normative)

## Purpose
Give teams a concrete translation from common AWS services to an EU-cloud implementation path, with ECS runtime evidence requirements attached.

This is a capability map, not a one-to-one product parity claim.

## How to read this
- Column 1: common AWS service teams start from.
- Column 2: portable capability you actually need.
- Column 3: EU cloud options (illustrative candidates).
- Column 4: ECS minimum evidence contract for that capability.
- Column 5: practical implementation pattern.

## ECS minimum contract (applies to every row)
For governed operations, implementations should emit:
- Core envelope fields (`id`, `event_type`, `occurred_at`, `tenant_id`, `sequence`, `outcome`, `evidence_pointer`)
- Decision context (`policy_snapshot_id`, `authority_snapshot_id`, `correlation_id`)
- Chain continuity (`chain_id`, `event_hash`, `prev_hash`)
- Explicit refusal evidence (`outcome=refused`, `refusal_reason`)
- Export bundle (`manifest.json`, `events.jsonl`, `chain-segment.json`, `verifier-inputs.json`, `profile-claim.json`)

References:
- `docs/evidence/catalog.md`
- `docs/evidence/export-schema.md`
- `docs/evidence/refusal-semantics.md`
- `docs/examples/evidence-operations/`

## Capability map
| AWS starting point | Portable capability target | EU cloud options (examples) | ECS evidence demands | Implementation pattern |
|---|---|---|---|---|
| IAM + STS | Identity, delegation, short-lived credentials | OIDC/JWKS + provider IAM model (OVHcloud, Scaleway, IONOS, STACKIT, OTC, Exoscale) | authority binding events, delegation events, refusal on invalid scope | normalize to authority snapshots + delegation IDs; emit on token issue/use |
| KMS / CloudHSM | Key custody and crypto boundary | provider KMS/HSM services | key custody artifact refs, policy-bound key use decisions | externalize key-custody artifacts and link in evidence pointers |
| EC2 + ASG | VM compute with autoscaling controls | provider VM + autoscaling equivalents | admit/refuse for provisioning actions | emit control-plane decision events for create/update/delete |
| EKS | Managed Kubernetes control plane | managed Kubernetes services across EU providers | admission decisions with policy/authority snapshots | use `adapters/k8s-admission/` path for runtime evidence |
| Fargate | Managed container runtime | managed container/job runtime or K8s serverless layer | execution admit/refuse evidence for workload runs | sidecar or admission-based evidence emission |
| S3 | Object storage API + governance metadata | S3-compatible object services | `object.put/get/delete`, route refusals, jurisdiction/retention context | use `adapters/object-storage-proxy/` path |
| EBS/EFS | Block/file storage for workloads | provider block and file services | lifecycle events for create/attach/snapshot/export; refusal on policy violations | emit storage lifecycle events via control-plane wrappers |
| RDS Postgres / Aurora PG | Managed relational data plane | managed Postgres-class services | policy-bound access/export decisions, backup/restore evidence | treat DB actions as governed operations with snapshot context |
| DynamoDB | Managed key-value / document store | provider NoSQL alternatives or managed PostgreSQL patterns | read/write/export outcome events with policy context | enforce via gateway/service layer where native hooks are weak |
| SQS + SNS | Queue/topic messaging | queue/topic services | publish/consume decision evidence + refusal for non-compliant routing | emit `queue.publish/consume` via gateway hooks |
| Kinesis / MSK | Stream processing plane | stream services / managed Kafka | stream publish/subscribe evidence + jurisdiction refusals | emit `stream.publish/subscribe` via stream edge adapters |
| API Gateway | Managed API front door | provider API gateway / ingress gateway | `api.invoke` accepted/refused/failed with snapshots | gateway middleware + evidence emitter |
| ALB/NLB + WAF | L4/L7 traffic control and edge policy | provider load balancer + WAF/edge controls | routing/refusal evidence for jurisdiction/policy blocks | emit decisions at ingress/LB policy points |
| Route53 | DNS + health/failover routing | provider DNS/traffic services | refusal evidence when failover target violates policy boundary | treat traffic policy as governed decision source |
| CloudWatch + X-Ray | Metrics/logs/traces and alerting | provider observability stacks | evidence exportability and correlation linkage | map observability IDs into evidence correlation fields |
| CloudTrail + Config | Control-plane audit source | provider audit/config APIs | normalized Core events + chain continuity + export bundles | transform provider audit feeds to ECS envelope |
| Secrets Manager / SSM Param | Secret/config lifecycle | provider secret/config stores | secret access/update decisions with policy/authority context | front secrets access with policy-evaluated gateway |
| EventBridge + Step Functions | Event choreography and workflow orchestration | event bus + workflow services | decision and outcome evidence at workflow transitions | emit per-step events with shared correlation IDs |

## Concrete migration recipe (AWS to EU cloud)
1. Choose one workload slice (API + object + queue is enough).
2. Implement capability wrappers at decision points (gateway/admission/proxy).
3. Emit ECS events for accepted, refused, and failed paths.
4. Export bundles and run runtime smoke checks.
5. Promote provider only when smoke checks pass and refusal paths are proven.

Use:
- `docs/guides/runtime-quickstart.md`
- `docs/guides/vendor-integration-playbook.md`
- `docs/conformance/runtime-smoke-tests.md`

## Important caveat
Do not optimize for one-to-one service naming parity. Optimize for:
- stable capability abstraction,
- portable evidence semantics,
- verifier-friendly export bundles,
- clear refusal behavior under policy and jurisdiction constraints.
