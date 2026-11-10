import unittest
from app.review_rules import review

class ReviewRuleTests(unittest.TestCase):
    def test_debug_output(self):
        self.assertEqual(review("console.log('hi')")[0]["rule"], "debug-output")
    def test_line_number(self):
        self.assertEqual(review("x = 1\nprint(x)")[0]["line"], 2)
    def test_clean_code(self):
        self.assertEqual(review("x = 1"), [])

if __name__ == "__main__":
    unittest.main()
