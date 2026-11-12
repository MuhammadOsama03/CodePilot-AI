"""Simple limits shared by API and tests."""
MAX_SOURCE_CHARACTERS = 50_000
SUPPORTED_LANGUAGES = ("python", "javascript", "typescript")

def normalize_language(value: str) -> str:
    normalized = value.strip().lower()
    if normalized not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported review language")
    return normalized
