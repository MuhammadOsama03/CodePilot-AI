import unittest
from app.finding_metrics import affected_lines, rule_counts

class FindingMetricTests(unittest.TestCase):
    def test_unique_sorted_lines(self):
        rows = [{"line": 4}, {"line": 2}, {"line": 4}, {"line": -1}]
        self.assertEqual(affected_lines(rows), [2, 4])

    def test_counts_rules(self):
        rows = [{"rule": "eval"}, {"rule": "eval"}, {"rule": "debug"}]
        self.assertEqual(rule_counts(rows), {"debug": 1, "eval": 2})
