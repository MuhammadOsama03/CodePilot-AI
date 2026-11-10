"""Conservative local code review hints; not an AI security audit."""
from dataclasses import dataclass, asdict
import re

@dataclass
class Finding:
    rule: str
    severity: str
    line: int
    message: str

RULES = [
    ("possible-secret", "high", re.compile(r"(?i)\b(?:api_key|password|secret)\s*=\s*['\"][^'\"]+['\"]"), "Possible hardcoded credential; use environment variables."),
    ("debug-output", "low", re.compile(r"\b(?:console\.log|print)\s*\("), "Consider removing debugging output before release."),
    ("python-eval", "high", re.compile(r"\beval\s*\("), "Avoid evaluating untrusted expressions."),
]

def review(code: str) -> list[dict]:
    findings = []
    for line_number, line in enumerate(code.splitlines(), 1):
        for rule, severity, pattern, message in RULES:
            if pattern.search(line):
                findings.append(asdict(Finding(rule, severity, line_number, message)))
    return findings
