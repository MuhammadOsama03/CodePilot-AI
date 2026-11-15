"""Safe JSON serialization of structured local findings."""
import json

def findings_json(findings: list[dict]) -> str:
    return json.dumps({"findings": findings, "count": len(findings)}, ensure_ascii=False, sort_keys=True)
