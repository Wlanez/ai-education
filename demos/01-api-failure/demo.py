"""Deterministic, dependency-free API 503 demonstration using synthetic orders."""


class FakeFulfillmentAPI:
    """Local stand-in for an upstream service; no network calls are made."""

    def __init__(self, failures_before_success=0, always_fail=False, failure_status=503):
        if failures_before_success < 0:
            raise ValueError("failures_before_success must not be negative")
        self.failures_remaining = failures_before_success
        self.always_fail = always_fail
        self.failure_status = failure_status
        self.accepted_by_key = {}
        self.attempts = 0
        self.events = []

    @property
    def accepted_order_count(self):
        return len(self.accepted_by_key)

    def submit(self, order_id, idempotency_key):
        self.attempts += 1
        if self.always_fail or self.failures_remaining > 0:
            if not self.always_fail:
                self.failures_remaining -= 1
            event = {"attempt": self.attempts, "http_status": self.failure_status, "order_id": order_id}
            self.events.append(event)
            return self.failure_status

        if idempotency_key in self.accepted_by_key:
            status = 200
        else:
            self.accepted_by_key[idempotency_key] = order_id
            status = 201
        self.events.append({"attempt": self.attempts, "http_status": status, "order_id": order_id})
        return status


def submit_naively(api, order_id):
    """Make one request and expose the 503 instead of claiming the order succeeded."""
    status = api.submit(order_id, idempotency_key=f"order-{order_id}")
    return {
        "workflow_status": "completed" if status < 300 else "needs_attention",
        "http_status": status,
        "attempts": 1,
    }


def submit_with_bounded_retry(api, order_id, max_attempts=3):
    """Retry only the local simulated request up to a fixed attempt limit."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    status = None
    for attempt in range(1, max_attempts + 1):
        status = api.submit(order_id, idempotency_key=f"order-{order_id}")
        if status < 300:
            return {"workflow_status": "completed", "http_status": status, "attempts": attempt}
        if status != 503:
            return {"workflow_status": "pending_review", "http_status": status, "attempts": attempt}

    return {"workflow_status": "pending_review", "http_status": status, "attempts": max_attempts}


if __name__ == "__main__":
    import json

    healthy_api = FakeFulfillmentAPI()
    healthy = submit_with_bounded_retry(healthy_api, "ORDER-0999", max_attempts=3)
    fragile_api = FakeFulfillmentAPI(failures_before_success=1)
    fragile = submit_naively(fragile_api, "ORDER-1000")
    recovered_api = FakeFulfillmentAPI(failures_before_success=1)
    recovered = submit_with_bounded_retry(recovered_api, "ORDER-1001", max_attempts=3)
    stuck_api = FakeFulfillmentAPI(always_fail=True)
    stuck = submit_with_bounded_retry(stuck_api, "ORDER-1002", max_attempts=3)
    print(json.dumps({
        "healthy_path": {**healthy, "api_events": healthy_api.events,
                         "accepted_orders": healthy_api.accepted_order_count},
        "single_attempt_503": {**fragile, "api_events": fragile_api.events,
                                "accepted_orders": fragile_api.accepted_order_count},
        "transient_503": {**recovered, "api_events": recovered_api.events,
                          "accepted_orders": recovered_api.accepted_order_count},
        "persistent_503": {**stuck, "api_events": stuck_api.events,
                            "accepted_orders": stuck_api.accepted_order_count},
    }, indent=2))
