import unittest
from app.finding_filters import filter_findings

class FindingFilterTests(unittest.TestCase):
    def test_filters_severity(self):
        rows = [{"severity": "high"}, {"severity": "low"}]
        self.assertEqual(filter_findings(rows, "high"), [{"severity": "high"}])

    def test_rejects_invalid_severity(self):
        with self.assertRaises(ValueError):
            filter_findings([], "critical")

    def test_returns_copies(self):
        rows = [{"severity": "high"}]
        result = filter_findings(rows)
        result[0]["severity"] = "low"
        self.assertEqual(rows[0]["severity"], "high")
