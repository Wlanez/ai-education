import json
import subprocess
import sys
import unittest

from demo import FakeFulfillmentAPI, submit_naively, submit_with_bounded_retry


class FailureFirstDemoTests(unittest.TestCase):
    def test_naive_workflow_does_not_call_a_503_success(self):
        api = FakeFulfillmentAPI(failures_before_success=1)
        result = submit_naively(api, "ORDER-1001")
        self.assertEqual(result["http_status"], 503)
        self.assertEqual(result["workflow_status"], "needs_attention")
        self.assertEqual(api.accepted_order_count, 0)

    def test_bounded_retry_recovers_after_transient_503(self):
        api = FakeFulfillmentAPI(failures_before_success=1)
        result = submit_with_bounded_retry(api, "ORDER-1001", max_attempts=3)
        self.assertEqual(result["workflow_status"], "completed")
        self.assertEqual(result["attempts"], 2)
        self.assertEqual(api.accepted_order_count, 1)

    def test_exhausted_retries_leave_order_pending_without_claiming_success(self):
        api = FakeFulfillmentAPI(always_fail=True)
        result = submit_with_bounded_retry(api, "ORDER-1001", max_attempts=3)
        self.assertEqual(result["workflow_status"], "pending_review")
        self.assertEqual(result["attempts"], 3)
        self.assertEqual(api.accepted_order_count, 0)

    def test_non_retryable_4xx_is_not_retried(self):
        api = FakeFulfillmentAPI(always_fail=True, failure_status=400)
        result = submit_with_bounded_retry(api, "ORDER-1001", max_attempts=3)
        self.assertEqual(result["workflow_status"], "pending_review")
        self.assertEqual(result["attempts"], 1)
        self.assertEqual(result["http_status"], 400)

    def test_replaying_the_same_order_does_not_create_a_duplicate(self):
        api = FakeFulfillmentAPI()
        first = submit_with_bounded_retry(api, "ORDER-1001", max_attempts=3)
        second = submit_with_bounded_retry(api, "ORDER-1001", max_attempts=3)
        self.assertEqual(first["workflow_status"], "completed")
        self.assertEqual(second["workflow_status"], "completed")
        self.assertEqual(api.accepted_order_count, 1)

    def test_demo_output_includes_baseline_failure_and_controlled_outcomes(self):
        result = subprocess.run([sys.executable, "demo.py"], check=True, capture_output=True, text=True)
        output = json.loads(result.stdout)
        self.assertIn("healthy_path", output)
        self.assertEqual(output["healthy_path"]["http_status"], 201)
        self.assertEqual(output["healthy_path"]["accepted_orders"], 1)
        self.assertIn("single_attempt_503", output)
        self.assertEqual(output["single_attempt_503"]["http_status"], 503)
        self.assertEqual(output["single_attempt_503"]["accepted_orders"], 0)
        self.assertEqual(output["transient_503"]["attempts"], 2)
        self.assertEqual(output["persistent_503"]["workflow_status"], "pending_review")

if __name__ == "__main__":
    unittest.main()
