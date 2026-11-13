"""Stable ordering for finding presentation."""
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}

def sort_findings(findings: list[dict]) -> list[dict]:
    return sorted(findings, key=lambda item: (SEVERITY_ORDER.get(item.get("severity"), 3), item.get("line", 0), item.get("rule", "")))
