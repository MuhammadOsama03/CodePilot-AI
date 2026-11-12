"""Summarize local heuristic findings without exposing submitted source."""
from collections import Counter

def summarize(findings: list[dict]) -> dict:
    counts = Counter(item["severity"] for item in findings)
    return {"total": len(findings), "by_severity": {level: counts[level] for level in ("high", "medium", "low")}}
