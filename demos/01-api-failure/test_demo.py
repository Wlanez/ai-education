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


    def test_script_is_long_enough_for_six_minutes_at_a_measured_pace(self):
        from pathlib import Path
        import re
        repo_root = Path(__file__).resolve().parents[2]
        script = (repo_root / "videos/01-api-failure/script.md").read_text()
        narration = " ".join(line for line in script.splitlines()
                             if not line.startswith("#") and not line.startswith("**")
                             and not line.startswith("[SCREEN:"))
        spoken_words = re.findall(r"\b[\w’'-]+\b", narration)
        self.assertGreaterEqual(len(spoken_words), 850,
                                f"Expected at least 850 spoken words, got {len(spoken_words)}")

    def test_reviewed_briefs_state_concrete_business_consequences(self):
        from pathlib import Path
        repo_root = Path(__file__).resolve().parents[2]
        expectations = {
            "videos/03-webhook-processing-loss/brief.md": "fulfillment request is never created",
            "videos/05-agent-authorization-boundary/brief.md": "invoice total and billing address",
            "videos/09-investigation-logs/brief.md": "wrong delivery status",
            "videos/12-preproduction-reliability-review/brief.md": "two customers for one available slot",
        }
        for relative_path, phrase in expectations.items():
            with self.subTest(path=relative_path):
                self.assertIn(phrase, (repo_root / relative_path).read_text())

if __name__ == "__main__":
    unittest.main()

