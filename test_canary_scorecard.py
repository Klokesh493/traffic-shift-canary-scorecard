import unittest

from canary_scorecard import verdict


class CanaryScorecardTest(unittest.TestCase):
    def test_rolls_back_high_error_rate(self):
        row = {"service": "edge", "error_rate_pct": "2.5", "p95_latency_ms": "300", "saturation_pct": "55", "rollback_ready": "yes"}
        self.assertEqual(verdict(row), "rollback")


if __name__ == "__main__":
    unittest.main()
