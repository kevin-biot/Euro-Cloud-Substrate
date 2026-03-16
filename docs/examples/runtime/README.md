# Runtime Example Kit (Draft)

## Purpose
Provide a concrete runnable path from operation -> evidence emission -> bundle export -> verifier checks.

## Files
- `mock_object_backend.py`: local mock object service (PUT/GET/DELETE).
- `run-demo.sh`: executes end-to-end runtime demo.
- `smoke-checks.sh`: validates exported bundle quickly.

## Run
```bash
bash docs/examples/runtime/run-demo.sh
```

## Outputs
- `docs/examples/runtime/.run/evidence-store/`
- `docs/examples/runtime/.run/bundle/`

## Related docs
- `docs/guides/runtime-quickstart.md`
- `docs/guides/runtime-reference-architecture.md`
- `docs/conformance/runtime-smoke-tests.md`
