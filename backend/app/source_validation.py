"""Reusable preflight checks for user-submitted source text."""
def source_is_meaningful(source: str) -> bool:
    return bool(source.strip())

def source_has_null_bytes(source: str) -> bool:
    return "\x00" in source
