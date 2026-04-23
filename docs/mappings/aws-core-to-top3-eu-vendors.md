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

## Concrete evidence pack by row

The point of this section is to stop the discussion drifting into assertion.
For each AWS-core row, capture:
- official source links,
- one minimal smoke-test command set,
- expected output,
- and a hard pass/fail note.

The commands below are **illustrative smoke-test patterns**. They are intended to show
what should be tested and what successful output should look like. They may require
adaptation to current provider CLI/API versions, account layout, and regional endpoints.

### IAM / STS
**Official source links**
- OVHcloud API getting started: [OVHcloud](https://support.us.ovhcloud.com/hc/en-us/articles/360018130839-First-Steps-with-the-OVHcloud-API)
- Scaleway API authentication: [Scaleway](https://www.scaleway.com/en/developer-api/)
- STACKIT service accounts and token flow: [STACKIT](https://docs.stackit.cloud/platform/access-and-identity/service-accounts/authentication-flows/)

**Test command**
```bash
ovhcloud cloud project list --json >/tmp/ovh-auth.json
scw account project list -o json >/tmp/scw-auth.json
stackit curl "https://authorization.api.eu01.stackit.cloud/v1/service-accounts" >/tmp/stackit-auth.json
```

**Expected output**
- Non-interactive success.
- Machine-readable JSON.
- Clear project/account/service-account identity in output.

**Pass/fail note**
- **Pass** if auth works non-interactively and can be wired into CI or agent automation without human prompts.
- **Fail** if the flow depends on console-only setup, interactive approval, or undocumented token handling.

### EKS-equivalent
**Official source links**
- OVHcloud Managed Kubernetes: [OVHcloud](https://us.ovhcloud.com/public-cloud/kubernetes/)
- Scaleway Kapsule: [Scaleway](https://www.scaleway.com/en/kubernetes-kapsule/)
- STACKIT Kubernetes Engine: [STACKIT](https://docs.stackit.cloud/products/runtime/kubernetes-engine/)

**Test command**
```bash
kubectl --kubeconfig "${OVH_KUBECONFIG}" get nodes -o json >/tmp/ovh-k8s.json
scw k8s cluster list region=all -o json >/tmp/scw-k8s.json
stackit ske cluster list --project-id "${STACKIT_PROJECT_ID}" --output-format json >/tmp/stackit-k8s.json
```

**Expected output**
- Cluster listing or node listing without retries or interactive login.
- Machine-readable output showing cluster identity and readiness.

**Pass/fail note**
- **Pass** if cluster lifecycle and `kubectl` attachment are straightforward enough for repeatable automation.
- **Fail** if kubeconfig acquisition, upgrade posture, or automation auth feels fragile.

### S3-equivalent
**Official source links**
- OVHcloud Object Storage: [OVHcloud](https://www.ovhcloud.com/en/public-cloud/object-storage/)
- Scaleway Object Storage: [Scaleway](https://www.scaleway.com/en/docs/object-storage)
- STACKIT Object Storage: [STACKIT](https://docs.stackit.cloud/products/storage/object-storage)

**Test command**
```bash
aws --endpoint-url "${OVH_S3_ENDPOINT}" s3api list-buckets >/tmp/ovh-s3.json
scw object bucket list region="${SCW_REGION}" -o json >/tmp/scw-s3.json
aws --endpoint-url "https://object.storage.eu01.onstackit.cloud" s3api list-buckets >/tmp/stackit-s3.json
```

**Expected output**
- Bucket metadata returned successfully.
- S3-compatible auth works with non-interactive credentials.

**Pass/fail note**
- **Pass** if core S3 operations work cleanly and follow-on checks for versioning/object lock/lifecycle are available.
- **Fail** if the service is nominally S3-compatible but key governance features or tooling paths break quickly.

### RDS PostgreSQL / Aurora PostgreSQL equivalent
**Official source links**
- OVHcloud Managed PostgreSQL: [OVHcloud](https://www.ovhcloud.com/en/public-cloud/postgresql/)
- Scaleway Serverless SQL Databases: [Scaleway](https://www.scaleway.com/en/docs/serverless-sql-databases)
- STACKIT PostgreSQL Flex: [STACKIT](https://docs.stackit.cloud/products/databases/postgresql-flex)

**Test command**
```bash
psql "${OVH_PG_DSN}" -c 'select version();' >/tmp/ovh-pg.txt
psql "${SCW_PG_DSN}" -c 'select version();' >/tmp/scw-pg.txt
psql "${STACKIT_PG_DSN}" -c 'select version();' >/tmp/stackit-pg.txt
```

**Expected output**
- Successful connection.
- PostgreSQL version string returned.
- No hidden proxying or network constraints that block normal app connectivity.

**Pass/fail note**
- **Pass** if connection, backup posture, and automation lifecycle look like a credible app default.
- **Fail** if the service exists on paper but is awkward for normal startup/operator use.

### ALB / ingress / edge TLS
**Official source links**
- OVHcloud Load Balancer: [OVHcloud](https://www.ovhcloud.com/en/public-cloud/load-balancer/)
- Scaleway SSL/TLS for Edge Services: [Scaleway](https://www.scaleway.com/en/docs/edge-services/reference-content/ssl-tls-certificate)
- STACKIT Application Load Balancer: [STACKIT](https://docs.stackit.cloud/products/network/load-balancing-and-content-delivery/application-load-balancer/)

**Test command**
```bash
curl -skI "https://${OVH_EDGE_HOST}" >/tmp/ovh-edge.txt
curl -skI "https://${SCW_EDGE_HOST}" >/tmp/scw-edge.txt
curl -skI "https://${STACKIT_EDGE_HOST}" >/tmp/stackit-edge.txt
```

**Expected output**
- Valid HTTPS response headers.
- TLS handshake succeeds.
- Host/path routing lands on the expected backend.

**Pass/fail note**
- **Pass** if TLS termination and ingress routing are simple enough to automate and reason about.
- **Fail** if edge setup becomes a bespoke assembly exercise for basic production use.

### Route53-equivalent
**Official source links**
- OVHcloud DNS / API intro: [OVHcloud](https://help.ovhcloud.com/csm/en-sg-domain-names-api-introduction?id=kb_article_view&sysparm_article=KB0051557)
- Scaleway Domains and DNS: [Scaleway](https://www.scaleway.com/en/docs/domains-and-dns/)
- STACKIT DNS: [STACKIT](https://docs.stackit.cloud/products/network/core-networking/dns/)

**Test command**
```bash
dig +short "${OVH_TEST_RECORD}"
dig +short "${SCW_TEST_RECORD}"
dig +short "${STACKIT_TEST_RECORD}"
```

**Expected output**
- Correct A/CNAME/TXT answer returned.
- Low-friction zone and record management through API or CLI.

**Pass/fail note**
- **Pass** if DNS can be managed programmatically and is usable in deployment flows.
- **Fail** if DNS management is effectively console-only or too detached from the rest of the provider workflow.

### ACM-equivalent
**Official source links**
- OVHcloud cert-manager on Managed Kubernetes: [OVHcloud](https://help.ovhcloud.com/csm/en-public-cloud-kubernetes-install-cert-manager?id=kb_article_view&sysparm_article=KB0049779)
- Scaleway SSL/TLS certificates for Edge Services: [Scaleway](https://www.scaleway.com/en/docs/edge-services/reference-content/ssl-tls-certificate)
- STACKIT DNS01 ACME with cert-manager: [STACKIT](https://docs.stackit.cloud/products/network/core-networking/dns/tutorials/use-stackit-dns-for-dns01-to-act-as-a-dns01-acme-issuer-with-cert-manager/)

**Test command**
```bash
openssl s_client -connect "${OVH_TLS_HOST}:443" -servername "${OVH_TLS_HOST}" </dev/null 2>/dev/null | openssl x509 -noout -issuer -subject -dates
openssl s_client -connect "${SCW_TLS_HOST}:443" -servername "${SCW_TLS_HOST}" </dev/null 2>/dev/null | openssl x509 -noout -issuer -subject -dates
openssl s_client -connect "${STACKIT_TLS_HOST}:443" -servername "${STACKIT_TLS_HOST}" </dev/null 2>/dev/null | openssl x509 -noout -issuer -subject -dates
```

**Expected output**
- Certificate subject, issuer, and validity dates.
- Predictable issuance/renewal flow.

**Pass/fail note**
- **Pass** if certificate lifecycle is automatable enough to feel routine.
- **Fail** if routine certificate operations require too much manual handling or service-specific glue.

### CloudWatch / CloudTrail equivalent
**Official source links**
- OVHcloud Logs Data Platform: [OVHcloud](https://www.ovhcloud.com/en/identity-security-operations/logs-data-platform/)
- Scaleway Cockpit: [Scaleway](https://www.scaleway.com/en/cockpit/)
- STACKIT Observability: [STACKIT](https://docs.stackit.cloud/products/logging-and-monitoring/observability/)

**Test command**
```bash
ovhcloud ldp --help >/tmp/ovh-obs.txt
scw cockpit token list region=all -o json >/tmp/scw-obs.json
stackit curl "https://observability.api.eu01.stackit.cloud/v1/projects/${STACKIT_PROJECT_ID}/instances" >/tmp/stackit-obs.json
```

**Expected output**
- Non-interactive access path to logs/metrics/instances.
- Machine-readable output or stable CLI interface.

**Pass/fail note**
- **Pass** if monitoring and audit data are reachable in automation and can feed ECS export tooling.
- **Fail** if the observability surface is present but awkward to consume programmatically.

### ECR-equivalent
**Official source links**
- OVHcloud Managed Private Registry: [OVHcloud](https://www.ovhcloud.com/en/public-cloud/managed-private-registry/)
- Scaleway Container Registry: [Scaleway](https://www.scaleway.com/en/docs/container-registry/)
- STACKIT Container Registry: [STACKIT](https://docs.stackit.cloud/products/developer-platform/container-registry/basics/introduction-to-container-registry/)

**Test command**
```bash
docker pull "${OVH_REGISTRY_IMAGE}" >/tmp/ovh-registry.txt 2>&1
docker pull "${SCW_REGISTRY_IMAGE}" >/tmp/scw-registry.txt 2>&1
docker pull "${STACKIT_REGISTRY_IMAGE}" >/tmp/stackit-registry.txt 2>&1
```

**Expected output**
- Successful authenticated image pull.
- Clear namespace/repository semantics.

**Pass/fail note**
- **Pass** if registry login, push/pull, and CI usage are straightforward.
- **Fail** if the registry exists but is operationally awkward enough to push teams back to Docker Hub or AWS by default.

### Secrets Manager / KMS equivalent
**Official source links**
- OVHcloud KMS: [OVHcloud](https://us.ovhcloud.com/identity-security-operations/key-management-service/)
- Scaleway Secret Manager and Key Manager: [Scaleway Secret Manager](https://www.scaleway.com/en/docs/secret-manager/), [Scaleway Key Manager](https://www.scaleway.com/en/key-manager/)
- STACKIT Secrets Manager and KMS: [STACKIT Secrets Manager](https://docs.stackit.cloud/products/security/secrets-manager/), [STACKIT KMS](https://docs.stackit.cloud/products/security/kms/)

**Test command**
```bash
ovhcloud okms service list >/tmp/ovh-kms.txt
scw secret secret list -o json >/tmp/scw-secrets.json
stackit curl "https://secrets-manager.api.eu01.stackit.cloud/v1/projects/${STACKIT_PROJECT_ID}/instances" >/tmp/stackit-secrets.json
```

**Expected output**
- Service or secret inventory returned successfully.
- Clear non-interactive path for secret or key operations.

**Pass/fail note**
- **Pass** if secret/key lifecycle is scriptable and fits application delivery without fragile manual steps.
- **Fail** if trust-root or secret handling is too awkward to make production automation comfortable.
