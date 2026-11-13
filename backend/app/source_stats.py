"""Small source metrics; not semantic analysis."""
def source_stats(source: str) -> dict:
    lines = source.splitlines()
    return {
        "characters": len(source),
        "lines": len(lines),
        "nonempty_lines": sum(bool(line.strip()) for line in lines),
    }
