import unittest
from app.review_rules import review

class LanguageRuleTests(unittest.TestCase):
    def test_python_eval(self):
        self.assertEqual(review("eval(user_input)", "python")[0]["rule"], "python-eval")

    def test_typescript_eval(self):
        self.assertEqual(review("eval(userInput)", "typescript")[0]["rule"], "javascript-eval")

    def test_clean_typescript(self):
        self.assertEqual(review("const result = 2 + 2;", "typescript"), [])

    def test_secret_line(self):
        result = review("x=1\napi_key = 'example-only'", "python")
        self.assertEqual(result[0]["line"], 2)
