"""Presentation helpers for rule findings."""
def format_finding(finding: dict) -> str:
    line = finding["line"]
    severity = str(finding["severity"]).upper()
    return f"Line {line} [{severity}] {finding['message']}"

def format_report(findings: list[dict]) -> str:
    if not findings:
        return "No heuristic findings. This is not a security guarantee."
    return "\n".join(format_finding(finding) for finding in findings)
