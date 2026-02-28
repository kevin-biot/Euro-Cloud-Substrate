# Deployer/Operator Guide (Draft)

## Who this is for
Platform operators and SRE teams validating whether a provider/setup is deployment-ready.

## Goal
Run an ECS pilot and produce an artifact-backed decision in 30 days.

## Step 1: Define pilot
- Use `pilots/pilot-definition-template.md`.
- Select target profile and workload scope.
- Define must-pass gates and refusal scenarios.

## Step 2: Run Day 0 baseline
- Confirm deployment profile assumptions: `docs/deployment-profile.md`.
- Run provider smoke tests from `docs/mappings/eu-cloud-provider-selection-matrix.md`.
- Set artifact output path for all checks.

## Step 3: Run Day 7 evidence loop
- Execute governed workflow (accepted path + refusal path).
- Export bundle with verifier inputs.
- Validate profile self-description in manifest/verifier inputs.

## Step 4: Run Day 30 decision pass
- Fill scorecard: `pilots/scorecard-template.md`.
- Record C1-C7 and O1-O6 evidence paths.
- Record gaps and compensating controls with retest date.

## What to reject immediately
- No refusal evidence for denied actions.
- Export exists but verifier cannot run without privileged platform access.
- Profile mismatch between claim and manifest/events.
- Chain continuity or pointer integrity failures.

## Deliverables
- Final scorecard + gap register.
- Final evidence bundle and verifier output.
- Go/no-go recommendation with next-phase actions.
