import json
import unittest
from app.report_export import findings_json

class ReportExportTests(unittest.TestCase):
    def test_unicode_and_count(self):
        rows = [{"message": "évaluation", "line": 1}]
        report = json.loads(findings_json(rows))
        self.assertEqual(report["count"], 1)
        self.assertEqual(report["findings"][0]["message"], "évaluation")
