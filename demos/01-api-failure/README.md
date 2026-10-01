# API 503 Demo

A deterministic local simulation for the first failure-first video. It uses Python's standard library and synthetic order IDs; it does not make network requests.

## Run

```bash
python3 demo.py
python3 -m unittest -v test_demo.py
```

Every run starts with a fresh in-memory API. The program prints a healthy request, a one-shot 503, recovery after a transient 503, and the pending-review result after three persistent 503 responses.

The simulator demonstrates status handling, bounded retries, and idempotency behavior. It does not implement retry delays, an alerting system, a real queue, or a real provider's idempotency contract. See the [demo plan](../../videos/01-api-failure/demo-plan.md) for setup, reset, expected evidence, and production limits.
