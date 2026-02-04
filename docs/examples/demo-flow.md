# Demo Flow — ECS Evidence (Draft)

## Goal
Deploy the reference admission binder, submit a workload, export a bundle, and validate verifier inputs.

## Steps (10-minute path)
1) **Deploy the binder**
```bash
kubectl apply -f adapters/k8s-admission/k8s-manifest.yaml
```
Replace TLS placeholders in the manifest first.

2) **Opt in a namespace**
```bash
kubectl label namespace default ecs.evidence/enabled=true
```

3) **Apply a sample workload**
```bash
kubectl apply -f - <<'YAML'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecs-demo
  namespace: default
  annotations:
    ecs.policy/snapshot: pol-001
    ecs.authority/snapshot: auth-001
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ecs-demo
  template:
    metadata:
      labels:
        app: ecs-demo
    spec:
      containers:
        - name: app
          image: nginx:stable
YAML
```

4) **Export a bundle**
```bash
python3 adapters/k8s-admission/exporter.py \
  --store ./evidence-store \
  --out ./bundle \
  --from-seq 1 \
  --to-seq 10 \
  --profile ecs-evidence-baseline
```

5) **Verify inputs**
- Check `bundle/verifier-inputs.json` and confirm:
  - `evidence_profile_id` matches the manifest.
  - `chain_id`, `from_sequence`, `to_sequence` are present.

## Notes
- For regulated ML, set `ecs.evidence/profile=ecs-evidence-regulated-ml` and ensure `hash_profile_id` is emitted.
- For fail-closed posture, set webhook `failurePolicy: Fail` when the profile requires it.
