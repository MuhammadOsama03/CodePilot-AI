import unittest
from app.summary import summarize

class SummaryTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(summarize([]), {"total": 0, "by_severity": {"high": 0, "medium": 0, "low": 0}})

    def test_counts(self):
        findings = [{"severity": "high"}, {"severity": "low"}, {"severity": "high"}]
        self.assertEqual(summarize(findings)["by_severity"]["high"], 2)
