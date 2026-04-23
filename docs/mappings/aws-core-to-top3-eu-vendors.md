# AWS Core to Top-3 EU Vendors Crosswalk (Draft, Non-Normative)

## Purpose
Give startups, SMEs, and platform teams a concrete parity view of the **AWS core working set**
against three current EU cloud candidates:
- **OVHcloud**
- **Scaleway**
- **STACKIT**

This is not a market ranking. It is a practical build-and-run crosswalk for teams asking:
**"If we currently build on AWS, what do these three EU vendors look like against the small set of services we actually use?"**

## Why only three vendors
This document intentionally uses a narrow working set. The goal is implementation clarity, not market completeness.

These three are included because they currently expose enough public service surface to make the comparison useful:
- managed Kubernetes,
- S3-compatible object storage,
- managed PostgreSQL-class services,
- automation/API/CLI posture.

Sources:
- [OVHcloud Managed Kubernetes](https://us.ovhcloud.com/public-cloud/kubernetes/)
- [OVHcloud Object Storage](https://www.ovhcloud.com/en/public-cloud/object-storage/)
- [OVHcloud Managed PostgreSQL](https://www.ovhcloud.com/en/public-cloud/postgresql/)
- [Scaleway Kapsule](https://www.scaleway.com/en/kubernetes-kapsule/)
- [Scaleway Object Storage](https://www.scaleway.com/en/docs/object-storage)
- [Scaleway Serverless SQL Databases](https://www.scaleway.com/en/docs/serverless-sql-databases)
- [STACKIT Kubernetes Engine](https://stackit.com/en/products/runtime/stackit-kubernetes-engine)
- [STACKIT Object Storage](https://docs.stackit.cloud/products/storage/object-storage)
- [STACKIT PostgreSQL Flex](https://docs.stackit.cloud/products/databases/postgresql-flex)

## Reading guide
- `Equivalent` means a public managed service or clearly documented vendor capability exists.
- `Partial` means the capability exists but the parity shape differs materially from the AWS default, or additional assembly work is likely.
- `Gap` means no clear current managed equivalent is visible from the public primary sources used here.
- `PoC priority` means how early the capability should be tested in a real migration or greenfield evaluation.
  - `High`: test first; a weak result can kill the provider choice quickly.
  - `Medium`: test after core viability is proven.
  - `Low`: test later; important, but usually not the first blocker.

This document is intentionally conservative. Where a capability is unclear, it is treated as partial rather than assumed.

## AWS core working set
This crosswalk uses the smallest set that repeatedly shows up in real startup deployments:
- `IAM / STS`
- `EKS`
- `S3`
- `RDS for PostgreSQL / Aurora PostgreSQL`
- `ALB / ingress / edge TLS`
- `Route53`
- `ACM`
- `CloudWatch / CloudTrail`
- `ECR`
- `Secrets Manager / KMS`

## Crosswalk matrix
| AWS core service | What teams actually depend on | OVHcloud | Scaleway | STACKIT | Likely overall parity | PoC priority | ECS relevance | Notes |
|---|---|---|---|---|---|---|---|---|
| IAM / STS | API credentials, workload/service auth, delegation | Partial | Partial | Partial | Partial | High | High | All three expose automation auth surfaces, but AWS-style IAM+STS parity is not the right comparison. Expect adaptation around API keys, service accounts, or OIDC integration rather than a one-to-one STS clone. |
| EKS | Managed Kubernetes control plane | Equivalent | Equivalent | Equivalent | Equivalent | High | High | This is the strongest parity zone across all three. It is also the primary execution surface for ECS adapters and policy hooks. |
| S3 | Object storage with S3-compatible API | Equivalent | Equivalent | Equivalent | Equivalent | High | High | API compatibility exists across all three, but S3-compatible does not automatically mean full operational parity. Test object lock, lifecycle, events, and tooling paths separately. |
| RDS PostgreSQL / Aurora PG | Managed PostgreSQL-class relational service | Equivalent | Equivalent | Equivalent | Equivalent | High | Medium | All three document a managed PostgreSQL-class service, though Scaleway also emphasizes serverless PostgreSQL semantics. Important for policy/evidence state and app durability. |
| ALB / ingress / edge TLS | L7 front door, load balancing, ingress attachment | Partial | Partial | Partial | Partial | High | High | The capability exists, but AWS’s integrated ALB/ingress/edge fit is usually smoother. Expect more assembly and validation work. Critical because many ECS refusal and routing controls surface here. |
| Route53 | DNS zones, programmable records, traffic control | Partial | Partial | Partial | Partial | Medium | Medium | DNS exists, but Route53-style deep integration and traffic-policy ergonomics should be validated directly in PoC. |
| ACM | Managed certificate lifecycle | Partial | Partial | Partial | Partial | High | Medium | Certificate handling exists in some form, but AWS’s default ACM fit remains the benchmark to test against. This often drives operator friction early. |
| CloudWatch / CloudTrail | Metrics, logs, alerts, audit source | Partial | Partial | Partial | Partial | High | High | All three have observability/audit surfaces, but the operator experience and evidence export shape are not AWS-identical. This matters directly for ECS evidence export and verification posture. |
| ECR | Managed OCI/container registry | Partial | Partial | Partial | Partial | Medium | Low | Commonly available, but image-scanning, policy, and workflow fit should be treated as a separate check. Important operationally, but less central to ECS than ingress/storage/evidence surfaces. |
| Secrets Manager / KMS | Secret lifecycle, key custody, encryption controls | Partial | Partial | Partial | Partial | High | High | This is a parity-sensitive area. The existence of key/secret services does not by itself establish AWS-like integration depth. It is also central to sovereign trust-root and custody posture. |

## Immediate PoC order
If time is limited, test these first:
1. `EKS`
2. `S3`
3. `ALB / ingress / edge TLS`
4. `IAM / STS`
5. `CloudWatch / CloudTrail`
6. `ACM`
7. `RDS PostgreSQL / Aurora PG`

Reason:
- the first six determine whether the provider feels coherent enough for day-to-day delivery,
- and they overlap most directly with ECS runtime evidence, refusal, and portability concerns.

## Practical takeaways by vendor

### OVHcloud
- Strongest visible parity areas:
  - managed Kubernetes,
  - S3-compatible object storage,
  - managed PostgreSQL.
- Likely integration work:
  - identity/delegation model relative to AWS IAM/STS,
  - ingress/DNS/certificate ergonomics,
  - audit/observability normalization for automated operator workflows.

### Scaleway
- Strongest visible parity areas:
  - managed Kubernetes,
  - S3-compatible object storage,
  - serverless PostgreSQL-class service with autoscaling and backups.
- Likely integration work:
  - identity/service auth adaptation,
  - edge/DNS/certificate shape versus AWS defaults,
  - operational fit validation for production observability and governance exports.

### STACKIT
- Strongest visible parity areas:
  - managed Kubernetes,
  - object storage,
  - managed PostgreSQL.
- Likely integration work:
  - IAM/STS-style workflow replacement,
  - certificate and DNS lifecycle ergonomics,
  - practical operator experience around logging, alerting, and service composition.

## What this means for EU cloud adoption
The key lesson is not that EU vendors lack core primitives. They do have the core primitives.

The issue is **coherence**:
- how smoothly the primitives fit together,
- how good the automation surface is,
- how much operator assembly is required,
- how portable the resulting governance evidence is.

That is why AWS continues to win by default in many startups:
not because European clouds lack compute or storage,
but because AWS still offers a tighter default operating model across the working set.

## Recommended use of this document
Use this crosswalk together with:
- `docs/mappings/eu-cloud-provider-selection-matrix.md`
- `docs/mappings/aws-to-eu-cloud-service-map.md`
- `docs/guides/runtime-quickstart.md`

Then do a provider PoC around a single slice:
- API,
- object storage,
- PostgreSQL,
- ingress/TLS,
- audit/evidence export.

That is where the real parity picture appears.
