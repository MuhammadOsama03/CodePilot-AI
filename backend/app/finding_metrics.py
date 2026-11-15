"""Derive display metrics from the scanner's findings."""
def affected_lines(findings: list[dict]) -> list[int]:
    return sorted({item["line"] for item in findings if isinstance(item.get("line"), int) and item["line"] > 0})

def rule_counts(findings: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in findings:
        name = str(finding.get("rule", "unknown"))
        counts[name] = counts.get(name, 0) + 1
    return dict(sorted(counts.items()))
