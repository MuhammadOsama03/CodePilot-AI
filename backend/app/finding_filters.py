"""Filter review findings without changing the original result."""
VALID_SEVERITIES = frozenset({"high", "medium", "low"})

def filter_findings(findings: list[dict], severity: str | None = None) -> list[dict]:
    if severity is not None and severity not in VALID_SEVERITIES:
        raise ValueError("Unsupported severity")
    return [dict(item) for item in findings if severity is None or item.get("severity") == severity]
