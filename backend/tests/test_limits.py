import unittest
from app.limits import normalize_language, MAX_SOURCE_CHARACTERS

class LimitTests(unittest.TestCase):
    def test_normalizes_language(self):
        self.assertEqual(normalize_language(" Python "), "python")

    def test_rejects_unsupported(self):
        with self.assertRaises(ValueError):
            normalize_language("ruby")

    def test_limit(self):
        self.assertEqual(MAX_SOURCE_CHARACTERS, 50_000)
