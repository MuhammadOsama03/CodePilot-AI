import unittest
from app.rule_catalog import describe_rule, RULE_DESCRIPTIONS

class RuleCatalogTests(unittest.TestCase):
    def test_all_descriptions_are_nonempty(self):
        self.assertTrue(all(RULE_DESCRIPTIONS.values()))

    def test_unknown_rule(self):
        self.assertIsNone(describe_rule("not-a-rule"))
