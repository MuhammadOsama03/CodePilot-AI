import unittest
from app.source_validation import source_has_null_bytes, source_is_meaningful

class SourceValidationTests(unittest.TestCase):
    def test_whitespace_is_not_meaningful(self):
        self.assertFalse(source_is_meaningful(" \n\t "))

    def test_code_is_meaningful(self):
        self.assertTrue(source_is_meaningful("x = 1"))

    def test_detects_null_byte(self):
        self.assertTrue(source_has_null_bytes("x\x00y"))
