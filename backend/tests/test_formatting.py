import unittest
from app.formatting import format_report

class FormattingTests(unittest.TestCase):
    def test_empty_report_disclaimer(self):
        self.assertIn("not a security guarantee", format_report([]))

    def test_finding_line(self):
        result = format_report([{"line": 4, "severity": "high", "message": "Avoid eval"}])
        self.assertIn("Line 4 [HIGH] Avoid eval", result)
