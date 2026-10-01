# Demo Plan — Essential API Returns HTTP 503

## Purpose

Show how one temporary HTTP 503 can leave an order unsubmitted, then demonstrate a bounded retry, stable idempotency key, and safe pending state when the service keeps failing.

## Requirements

- Python 3.10 or later; standard library only.
- No network access, account, token, production system, or third-party service.
- Synthetic order IDs only.

## Run and reset

From this directory:

```bash
python3 demo.py
python3 -m unittest -v test_demo.py
```

Each command starts a fresh in-memory simulator. Running demo.py again resets all attempts, events, and accepted orders. The script does not make live API requests or wait between attempts.

## Scenarios and expected evidence

1. **Healthy path — ORDER-0999:** one request returns HTTP 201; workflow status is completed; accepted_orders is 1.
2. **Single attempt — ORDER-1000:** injected first response is HTTP 503; workflow status is needs_attention; accepted_orders is 0.
3. **Transient failure — ORDER-1001:** the first response is 503 and the next is 201; after two attempts, status is completed and accepted_orders is 1.
4. **Persistent failure — ORDER-1002:** each of three attempts returns 503; status is pending_review and accepted_orders is 0.

The tests also verify that a non-retryable 400 is not retried, replaying the same order with the same idempotency key does not create another record in this simulator, and exhausted retries never claim success.

## Recording sequence

1. Run the healthy path and point out status 201 and one accepted order.
2. Show the one-shot 503 and explain that the request was not accepted.
3. Show the transient case: 503, then 201, two attempts, one accepted order.
4. Show persistent 503: three attempts, pending_review, zero accepted orders.
5. Run the unit tests to support the replay and 400 examples if needed.

## Control and limits

The simulator retries only status 503 and stops after three attempts. It uses the same order key on each request. The in-memory simulator models idempotency behavior; it does not establish that a real provider supports idempotency. Verify the provider contract before applying this pattern.

There is no backoff or jitter in this short deterministic demo. A production retry policy should use service-specific guidance and a suitable delay; repeated immediate requests can worsen load. The demo does not implement alerting or a real review queue. It demonstrates the pending_review state that a real workflow should connect to an owner-visible queue or alert.

## Safety check

Confirm the recording shows only synthetic IDs and local output. Inspect screen, terminal, logs, and browser before publishing. Do not add credentials, customer information, production payloads, or employer/client data.
