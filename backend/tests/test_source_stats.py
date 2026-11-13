import unittest
from app.source_stats import source_stats

class SourceStatsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(source_stats(""), {"characters": 0, "lines": 0, "nonempty_lines": 0})

    def test_multiline(self):
        self.assertEqual(source_stats("a\n\nb")["nonempty_lines"], 2)
