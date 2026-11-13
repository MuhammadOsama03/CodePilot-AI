"""Public metadata for the prototype rule engine."""
RULE_DESCRIPTIONS = {
    "possible-secret": "Flags certain literal assignments to credential-like names.",
    "debug-output": "Flags common print and console logging calls.",
    "python-eval": "Flags eval calls in Python source.",
    "javascript-eval": "Flags eval calls in JavaScript and TypeScript source.",
}

def describe_rule(rule: str) -> str | None:
    return RULE_DESCRIPTIONS.get(rule)
