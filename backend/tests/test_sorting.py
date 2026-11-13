import unittest
from app.sorting import sort_findings

class SortingTests(unittest.TestCase):
    def test_severity_order(self):
        rows = [{"severity": "low", "line": 1}, {"severity": "high", "line": 3}]
        self.assertEqual(sort_findings(rows)[0]["severity"], "high")

    def test_does_not_mutate_input(self):
        rows = [{"severity": "low", "line": 1}]
        self.assertEqual(sort_findings(rows), rows)
