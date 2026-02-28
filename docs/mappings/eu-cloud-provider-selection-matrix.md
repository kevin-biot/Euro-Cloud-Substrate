# EU Cloud Provider Selection Matrix (Draft, Non-Normative)

## Purpose
Provide a practical, weighted selection matrix to choose one primary EU cloud provider for ECS deployments, while comparing against an AWS core-services baseline.

This is a procurement and architecture aid, not a certification.

## Decision model (single-vendor primary)
- **Primary target:** one EU provider for production posture.
- **Dev velocity lane:** AWS can remain a development/test baseline.
- **Portability guardrail:** ECS deployment profile + evidence export must stay portable.

This avoids operational sprawl across many clouds while preserving exit options.

## Inputs from current ECS/SAPP/aARP needs
The matrix is built from current deployment needs implied by:
- ECS deployment contract: `docs/deployment-profile.md`
- WS6 portability requirements: `ws6-migration/spec.md`
- ECS evidence export/verifier model: `docs/evidence/export-schema.md`, `docs/evidence/verifier-responsibilities.md`
- SAPP runtime needs (K8s, Postgres, S3-style archive, JWKS/OIDC path)
- aARP runtime needs (K8s control-plane services, policy/evidence services, jurisdiction-aware routing)

## Must-pass gates (no score override)
A provider fails selection if any of these cannot be satisfied with acceptable controls:
1. Managed Kubernetes suitable for production workloads.
2. S3-compatible object storage with versioning and immutability controls (WORM/object lock/legal hold or equivalent).
3. Managed relational store suitable for durable evidence state (Postgres class).
4. Workload/API identity path that can integrate with OIDC/JWKS and mTLS service identity.
5. Evidence export and retrieval posture compatible with ECS bundle/verifier model.

## Weighted criteria (100 total)
| ID | Criterion | Weight | What to verify |
|---|---|---:|---|
| C1 | Kubernetes control-plane maturity | 20 | Upstream conformance, version cadence, upgrade model, autoscaling, ingress/LB support |
| C2 | Object storage (S3) governance depth | 20 | S3 compatibility, versioning, object lock/WORM/legal hold, replication, encryption options |
| C3 | Identity and workload auth model | 15 | OIDC/JWKS integration, service identity patterns, mTLS compatibility |
| C4 | Sovereignty and residency controls | 15 | Regional control, policy boundaries, data locality statements |
| C5 | Data services for SAPP/aARP | 10 | Managed Postgres-class service, backup/restore, HA options |
| C6 | IaC/API automation fitness | 10 | Terraform/Pulumi/API/CLI coverage, non-interactive auth, and scriptability for repeatable deployment profile execution |
| C7 | Operability and evidence readiness | 10 | Audit/log export paths, monitoring, supportability for evidence pipelines |

## Scoring scale
- 0 = missing
- 1 = major gap / custom build likely
- 2 = partial support / high integration effort
- 3 = viable with known constraints
- 4 = strong fit with minor gaps
- 5 = excellent fit

Weighted score formula:
`total = sum((score_i / 5.0) * weight_i)` (max 100)

## Ops parity extension (recommended)
The base criteria above score substrate fitness. For real-world deployment posture, add an operations parity score against your current AWS operating model (Route53, ACM, CloudWatch, ALB/NLB, ingress, OpenShift path).

### Ops parity weighted criteria (100 total)
| ID | Criterion | Weight | What to verify |
|---|---|---:|---|
| O1 | DNS and traffic control parity | 20 | Route53-like capabilities: public/private zones, health checks, failover/weighted routing, API/IaC control |
| O2 | Certificate lifecycle parity | 15 | ACM-like certificate issuance/renewal, wildcard cert handling, private CA integration |
| O3 | Observability and alerting parity | 15 | CloudWatch-like metrics/logs/alerts/traces, retention/export, SIEM integration |
| O4 | LB / ingress / edge security parity | 20 | Managed L4/L7 LB, ingress controllers, WAF/edge policy hooks, mTLS compatibility |
| O5 | OpenShift deployment path | 15 | Managed OpenShift option or validated self-managed OpenShift path with supportable upgrades |
| O6 | Network foundation and private connectivity | 15 | VPC/VNet controls, NAT/egress controls, private endpoints, firewall/security policy APIs |

Ops parity score formula:
`ops_total = sum((ops_score_i / 5.0) * weight_i)` (max 100)

### Composite decision rule (recommended)
- Select candidates that satisfy all must-pass gates.
- Prefer providers with:
  - `substrate_total >= 75`
  - `ops_total >= 70`
  - no critical gaps in O1/O2/O4 (DNS, certs, LB/ingress).

## Prefilled provider evidence (public docs snapshot)
Status key:
- `P` = present in docs
- `U` = unclear/needs PoC confirmation

| Provider | K8s managed | Object storage S3 | Immutability controls (lock/WORM) | Initial notes |
|---|---|---|---|---|
| AWS (baseline) | P | P | P | Baseline reference for dev velocity and service breadth |
| OVHcloud | P | P | U | Strong K8s + S3 positioning; immutability controls need PoC confirmation |
| Scaleway | P | P | P | Clear K8s docs, S3 docs, and explicit object lock documentation |
| IONOS | P | P | U | Clear managed K8s and S3 compatibility; lock/legal-hold depth needs PoC confirmation |
| STACKIT | P | P | U | Strong SKE and object storage docs; immutability specifics need PoC confirmation |
| Open Telekom Cloud | P | P | P | CCE + OBS docs; S3 API reference and object lock/WORM capabilities documented |
| Exoscale | P | P | P | SKS + S3 docs; object lock/versioning and audit-oriented features documented |

## Agent automation surface parity (recommended addition)
For coding-agent workflows, evaluate whether a provider supports robust non-interactive automation across CLI + API + IaC.

Status key:
- `P` = clearly present in docs
- `M` = mixed/partial
- `U` = unclear

| Provider | First-party CLI | API/OpenAPI docs | IaC tooling | Non-interactive auth posture | Agent automation note |
|---|---|---|---|---|---|
| AWS (baseline) | P (`aws`) | P | P (Terraform/Pulumi/CloudFormation) | P (IAM roles, OIDC, API keys) | Strong baseline for agentic automation |
| OVHcloud | P (`ovhcloud`) | P (OVH API explorer) | P (Terraform docs) | M (API keys/tokens; validate workload identity path) | Good CLI/API surface; identity model needs PoC |
| Scaleway | P (`scw`) | P | P (Terraform docs) | M (API keys; validate workload identity path) | Strong developer tooling docs |
| IONOS | P (`ionosctl`) | P (Cloud API + Auth API + Activity Log API) | P (Terraform provider docs) | M (token-based auth documented; validate workload identity) | Good API-first posture |
| STACKIT | P (`stackit`) | P (STACKIT API + IaaS API) | P (Terraform + Pulumi noted) | M (service account flows documented; validate full workload identity path) | Rapidly maturing toolchain |
| Open Telekom Cloud | M (OpenStack ecosystem common; dedicated first-party CLI unclear) | M (service docs + API references, fragmented) | M (Terraform modules and ecosystem support) | M (AK/SK + OpenStack flows; validate modern workload identity) | Functional but less unified automation surface |
| Exoscale | P (`exo`) | P | P (Terraform provider docs; S3 via AWS tooling) | M (API key/secret; validate workload identity path) | Strong CLI + API for core infra |

## Agent automation smoke tests (v0 command packs)
Use these as fast, repeatable checks for non-interactive automation readiness. They are intentionally minimal: auth, k8s, object storage, logging/audit.

Prerequisites:
- `jq`, `kubectl`, `aws` CLI, and the provider CLI where applicable.
- Required environment variables exported before execution.
- Existing resources where IDs are required (cluster, project, instance, pipeline).

### AWS (baseline)
```bash
set -euo pipefail
aws sts get-caller-identity >/tmp/aws-auth.json
aws eks list-clusters --region "${AWS_REGION}" >/tmp/aws-k8s.json
aws s3api list-buckets >/tmp/aws-s3.json
aws logs describe-log-groups --region "${AWS_REGION}" --max-items 20 >/tmp/aws-logs.json
```

### OVHcloud
```bash
set -euo pipefail
ovhcloud cloud project list --json >/tmp/ovh-auth.json
# K8s check uses kubeconfig from OVH MKS (downloaded via portal or API).
kubectl --kubeconfig "${OVH_KUBECONFIG}" get nodes -o json >/tmp/ovh-k8s.json
aws --endpoint-url "${OVH_S3_ENDPOINT}" s3api list-buckets >/tmp/ovh-s3.json
# If Logs Data Platform is used, replace with your project command/API call.
ovhcloud ldp --help >/tmp/ovh-logs.txt
```

### Scaleway
```bash
set -euo pipefail
scw account project list -o json >/tmp/scw-auth.json
scw k8s cluster list region=all -o json >/tmp/scw-k8s.json
scw object bucket list region="${SCW_REGION}" -o json >/tmp/scw-s3.json
scw cockpit token list region=all -o json >/tmp/scw-logs.json
```

### IONOS
```bash
set -euo pipefail
ionosctl token list --output json >/tmp/ionos-auth.json
ionosctl k8s cluster list --output json >/tmp/ionos-k8s.json
aws s3 ls --endpoint-url "https://s3.${IONOS_S3_REGION}.ionoscloud.com" >/tmp/ionos-s3.txt
ionosctl logging-service pipeline list --location "${IONOS_LOG_LOCATION}" --output json >/tmp/ionos-logs.json
```

### STACKIT
```bash
set -euo pipefail
# Service-account auth is preferred for automation.
stackit curl "https://iaas.api.eu01.stackit.cloud/v1/projects/${STACKIT_PROJECT_ID}" >/tmp/stackit-auth.json
stackit ske cluster list --project-id "${STACKIT_PROJECT_ID}" --output-format json >/tmp/stackit-k8s.json
aws --endpoint-url "https://object.storage.eu01.onstackit.cloud" s3api list-buckets >/tmp/stackit-s3.json
stackit curl "https://argus.api.eu01.stackit.cloud/v1/projects/${STACKIT_PROJECT_ID}/instances/${STACKIT_OBS_INSTANCE_ID}/backup-retentions" >/tmp/stackit-logs.json
```

### Open Telekom Cloud (OTC)
```bash
set -euo pipefail
# OTC automation is commonly API/OpenStack-driven; endpoints vary by region.
openstack token issue -f json >/tmp/otc-auth.json
curl -sS -H "X-Auth-Token: ${OTC_TOKEN}" \
  "https://cce.${OTC_REGION}.otc.t-systems.com/api/v3/projects/${OTC_PROJECT_ID}/clusters" >/tmp/otc-k8s.json
aws --endpoint-url "${OTC_S3_ENDPOINT}" s3api list-buckets >/tmp/otc-s3.json
curl -sS -H "X-Auth-Token: ${OTC_TOKEN}" \
  "https://lts.${OTC_REGION}.otc.t-systems.com/v2/${OTC_PROJECT_ID}/groups" >/tmp/otc-logs.json
```

### Exoscale
```bash
set -euo pipefail
exo iam api-key list -O json >/tmp/exo-auth.json
exo compute sks list -O json >/tmp/exo-k8s.json
exo storage list -O json >/tmp/exo-s3.json
exo api list-events --from "${EXO_FROM}" --to "${EXO_TO}" >/tmp/exo-logs.json
```

### Pass criteria (all providers)
- Auth command returns valid JSON or non-empty machine-readable output.
- K8s command returns a list/description without interactive prompts.
- Object storage command returns bucket metadata using non-interactive credentials.
- Logging/audit command returns records or an empty list with HTTP/CLI success.

## Provider scoring worksheet (fill during PoC)
Use this table during hands-on testing.

| Provider | C1 (20) | C2 (20) | C3 (15) | C4 (15) | C5 (10) | C6 (10) | C7 (10) | Total /100 | Decision notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| OVHcloud |  |  |  |  |  |  |  |  |  |
| Scaleway |  |  |  |  |  |  |  |  |  |
| IONOS |  |  |  |  |  |  |  |  |  |
| STACKIT |  |  |  |  |  |  |  |  |  |
| Open Telekom Cloud |  |  |  |  |  |  |  |  |  |
| Exoscale |  |  |  |  |  |  |  |  |  |

## Ops parity worksheet (fill during PoC)
| Provider | O1 (20) | O2 (15) | O3 (15) | O4 (20) | O5 (15) | O6 (15) | Ops Total /100 | Decision notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| OVHcloud |  |  |  |  |  |  |  |  |
| Scaleway |  |  |  |  |  |  |  |  |
| IONOS |  |  |  |  |  |  |  |  |
| STACKIT |  |  |  |  |  |  |  |  |
| Open Telekom Cloud |  |  |  |  |  |  |  |  |
| Exoscale |  |  |  |  |  |  |  |  |

## V0 ops parity pre-score (docs-only, low confidence)
This pass is intentionally conservative. It reflects public product/docs visibility, not hands-on validation.

| Provider | O1 (20) | O2 (15) | O3 (15) | O4 (20) | O5 (15) | O6 (15) | Ops Total /100 | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| OVHcloud | 12 | 9 | 9 | 12 | 6 | 9 | 57 | Low |
| Scaleway | 12 | 9 | 12 | 12 | 6 | 9 | 60 | Low |
| IONOS | 12 | 9 | 9 | 12 | 6 | 9 | 57 | Low |
| STACKIT | 12 | 9 | 9 | 12 | 6 | 12 | 60 | Low |
| Open Telekom Cloud | 12 | 9 | 12 | 12 | 6 | 12 | 63 | Low |
| Exoscale | 12 | 9 | 12 | 12 | 6 | 9 | 60 | Low |

### V0 ops interpretation
- None of the candidates should be selected on ops parity without PoC validation; confidence is intentionally low.
- Priority validation order should be:
  1. **O1/O2/O4** (DNS, cert lifecycle, LB/ingress),
  2. **O3** (observability integration),
  3. **O6** (private connectivity/network controls),
  4. **O5** (OpenShift path).
- If OpenShift is a hard requirement, run O5 validation first to avoid dead-end evaluation effort.

## Ops parity PoC evidence checklist (audit-ready)
For each provider, collect evidence in a folder such as:
`artifacts/provider-poc/<provider>/<date>/`

### O1 DNS and traffic control (Route53-like)
- Screenshot/export of zone configuration (public and private where applicable).
- Evidence of API/IaC-managed DNS record update (plan/apply output or API call log).
- Test evidence for weighted/failover routing behavior (before/after endpoint results).
- Health-check configuration screenshot and triggered failover/refusal result.

### O2 Certificate lifecycle (ACM-like)
- Screenshot/export of certificate issuance workflow (managed or integrated CA).
- Evidence of automated renewal policy and renewal test result.
- TLS endpoint test output (`openssl`/client) showing active cert chain and expiry.
- Private CA integration evidence (if used) or documented gap with mitigation.

### O3 Observability and alerting (CloudWatch-like)
- Screenshot/export of metrics dashboard for SAPP/aARP services.
- Log ingestion and query evidence for app + control-plane events.
- Alert rule definition and fired alert proof (test incident).
- Export/retention settings evidence aligned with ECS evidence expectations.

### O4 LB / ingress / edge security
- LB and ingress configuration export (internal/external, listener policies).
- mTLS or TLS policy test evidence at ingress/LB boundary.
- WAF/edge policy evidence (rule set, blocked request example) if available.
- Jurisdictional routing/refusal test evidence where policy denies route.

### O5 OpenShift deployment path
- Evidence of managed OpenShift availability, or successful self-managed install output.
- Cluster version/upgrade path screenshot or command output.
- Operator compatibility check evidence for required components.
- Supportability evidence (official docs/support path) and identified constraints.

### O6 Network foundation and private connectivity
- Network topology export (VPC/VNet/subnets/route tables).
- Private endpoint/service endpoint configuration evidence.
- Egress/NAT control evidence (policy + test showing enforced path).
- Firewall/security group rule export and denial test proof.

## Scoring evidence requirements
- Every O-score MUST reference at least one artifact path and test timestamp.
- Any score >=4 MUST include a successful test artifact, not only documentation screenshots.
- Any score <=2 MUST include a short gap note + compensating control (if any).
- Final decision record SHOULD include links to all artifacts and reproducible test commands.

## V0 scoring pass (docs-only, provisional)
This pass is prefilled from public documentation and should be treated as a starting point before PoC execution.

| Provider | C1 (20) | C2 (20) | C3 (15) | C4 (15) | C5 (10) | C6 (10) | C7 (10) | Total /100 | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| OVHcloud | 16 | 16 | 9 | 12 | 8 | 8 | 6 | 75 | Medium |
| Scaleway | 16 | 16 | 9 | 12 | 8 | 10 | 8 | 79 | Medium |
| IONOS | 16 | 12 | 9 | 12 | 8 | 8 | 6 | 71 | Medium |
| STACKIT | 16 | 12 | 9 | 15 | 8 | 8 | 6 | 74 | Medium |
| Open Telekom Cloud | 16 | 16 | 9 | 12 | 8 | 8 | 8 | 77 | Medium |
| Exoscale | 16 | 16 | 9 | 12 | 8 | 10 | 8 | 79 | Medium |

### V0 interpretation
- Leading cluster from docs-only pass: **Scaleway**, **Exoscale**, **Open Telekom Cloud**.
- Strong sovereignty posture signal: **STACKIT** (Germany/Austria hosting posture), needs deeper object-governance validation in PoC.
- Biggest uncertainty remains **identity/workload auth model parity** versus AWS-style patterns; validate this first in PoC.

## Managed PostgreSQL availability check (for SAPP needs)
| Provider | Managed PostgreSQL | Notes |
|---|---|---|
| OVHcloud | Yes | Managed PostgreSQL product pages (multi-AZ/backup/PITR posture). |
| Scaleway | Yes | Managed PostgreSQL and MySQL docs + API docs. |
| IONOS | Yes | DBaaS for PostgreSQL docs integrated with DCD/API/Terraform. |
| STACKIT | Yes | PostgreSQL Flex managed service docs and service description. |
| Open Telekom Cloud | Yes | RDS includes PostgreSQL with HA, backups, and PITR. |
| Exoscale | Yes | Managed PostgreSQL (DBaaS) docs and product pages. |

## Serverless PostgreSQL note
- AWS **Fargate** is serverless **container compute**, not a database service.
- On AWS, the nearest managed PostgreSQL equivalents are **RDS for PostgreSQL** and **Aurora PostgreSQL** (including Aurora Serverless v2 options).
- In this EU candidate set, explicit serverless PostgreSQL is clearly documented for **Scaleway Serverless SQL Database**; others primarily document managed/provisioned PostgreSQL services.

## Suggested PoC sequence (4 weeks)
1. **Week 1:** Deploy ECS deployment profile baseline on top 3 candidates.
2. **Week 2:** Validate ops parity controls (DNS, certs, observability, LB/ingress, network controls).
3. **Week 3:** Run SAPP core path (settlement + evidence export + archive path checks).
4. **Week 4:** Run aARP core path + verifier checks + rollback rehearsal; finalize substrate + ops scoring.

## Recommended outcome format
Publish one short decision record with:
- Selected primary EU provider
- Known constraints and compensating controls
- Exit path validation result (ECS bundle portability)
- Re-test cadence (e.g., quarterly)

## Source links (provider docs)
- AWS EKS docs: <https://aws.amazon.com/documentation-overview/eks/>
- AWS Fargate docs: <https://aws.amazon.com/documentation-overview/fargate/>
- AWS RDS for PostgreSQL docs: <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html>
- AWS Aurora Serverless v2 docs: <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html>
- AWS Route 53 docs: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html>
- AWS Certificate Manager docs: <https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html>
- AWS CloudWatch docs: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- AWS Elastic Load Balancing docs: <https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html>
- AWS Red Hat OpenShift Service (ROSA): <https://aws.amazon.com/rosa/>
- AWS IRSA docs: <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>
- AWS S3 Object Lock: <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html>
- OVHcloud Managed Kubernetes: <https://www.ovhcloud.com/en/public-cloud/kubernetes/>
- OVHcloud Object Storage: <https://www.ovhcloud.com/en/public-cloud/object-storage/>
- OVHcloud Managed PostgreSQL: <https://us.ovhcloud.com/public-cloud/postgresql/>
- Scaleway Kubernetes docs: <https://www.scaleway.com/en/docs/kubernetes/>
- Scaleway Object Storage docs: <https://www.scaleway.com/en/docs/object-storage/>
- Scaleway Object Lock docs: <https://www.scaleway.com/en/docs/object-storage/api-cli/object-lock/>
- Scaleway Managed PostgreSQL and MySQL docs: <https://www.scaleway.com/en/docs/managed-databases-for-postgresql-and-mysql>
- Scaleway Serverless SQL Database: <https://www.scaleway.com/en/serverless-sql-database/>
- IONOS Managed Kubernetes: <https://cloud.ionos.com/managed/kubernetes>
- IONOS S3 compatibility docs: <https://docs.ionos.com/cloud/storage-and-backup/ionos-object-storage/concepts/s3-api-compatibility>
- IONOS DBaaS PostgreSQL docs: <https://docs.ionos.com/cloud/databases/postgresql/overview>
- STACKIT Kubernetes Engine docs: <https://docs.stackit.cloud/stackit/en/kubernetes-engine-10125671.html>
- STACKIT Object Storage docs: <https://docs.stackit.cloud/products/storage/object-storage>
- STACKIT PostgreSQL Flex docs: <https://docs.stackit.cloud/products/databases/postgresql-flex/>
- Open Telekom Cloud CCE docs: <https://docs.otc.t-systems.com/cloud-container-engine/index.html>
- Open Telekom Cloud OBS S3 API docs: <https://docs.otc.t-systems.com/object-storage-service/s3api/>
- Open Telekom Cloud OBS product page: <https://www.open-telekom-cloud.com/en/products-services/core-services/object-storage-service>
- Open Telekom Cloud RDS product page: <https://www.open-telekom-cloud.com/en/products-services/core-services/relational-database-service>
- Exoscale SKS docs: <https://community.exoscale.com/documentation/sks/overview/>
- Exoscale Object Storage quick start: <https://community.exoscale.com/community/storage/quick-start/>
- Exoscale Object Storage product page: <https://www.exoscale.com/object-storage/>
- Exoscale Managed PostgreSQL: <https://www.exoscale.com/dbaas/postgresql/>
