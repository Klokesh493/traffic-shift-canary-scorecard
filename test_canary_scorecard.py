import unittest

from canary_scorecard import verdict


class CanaryScorecardTest(unittest.TestCase):
    def test_rolls_back_high_error_rate(self):
        row = {"service": "edge", "error_rate_pct": "2.5", "p95_latency_ms": "300", "saturation_pct": "55", "rollback_ready": "yes"}
        self.assertEqual(verdict(row), "rollback")

    def test_invalid_telemetry_never_advances(self):
        healthy = {"error_rate_pct": "0.2", "p95_latency_ms": "220", "saturation_pct": "40",
                   "rollback_ready": "yes"}
        for field, value in (("error_rate_pct", "nan"), ("p95_latency_ms", "-1"),
                             ("saturation_pct", "101"), ("error_rate_pct", "")):
            with self.subTest(field=field, value=value):
                self.assertEqual(verdict({**healthy, field: value}), "pause")


if __name__ == "__main__":
    unittest.main()
