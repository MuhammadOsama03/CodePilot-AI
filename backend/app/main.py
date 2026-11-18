import os
import sqlite3
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .review_rules import review
from .summary import summarize
from .limits import MAX_SOURCE_CHARACTERS
from .gemini import ai_review, GeminiUnavailable
from .finding_metrics import affected_lines, rule_counts
from .source_validation import source_is_meaningful, source_has_null_bytes
from .history import save_review, list_reviews

app = FastAPI(title="CodePilot AI API", version="0.5.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in os.environ.get("CODEPILOT_ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",") if origin.strip() and origin.strip() != "*"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class ReviewRequest(BaseModel):
    language: str = Field(pattern=r"^(python|javascript|typescript)$")
    code: str = Field(min_length=1, max_length=MAX_SOURCE_CHARACTERS)
    use_ai: bool = False

@app.get("/health")
def health():
    return {"status": "ok", "phase": "prototype"}

@app.get("/reviews")
def review_history(limit: int = Query(default=20, ge=1, le=100)):
    return {"reviews": list_reviews(limit)}

@app.post("/review")
def review_code(payload: ReviewRequest):
    if not source_is_meaningful(payload.code):
        raise HTTPException(status_code=422, detail="Source code must contain non-whitespace characters")
    if source_has_null_bytes(payload.code):
        raise HTTPException(status_code=422, detail="Source code must not contain null bytes")
    findings = review(payload.code, payload.language)
    result = {"language": payload.language, "findings": findings, "summary": summarize(findings), "affected_lines": affected_lines(findings), "rule_counts": rule_counts(findings),
              "engine": "local-rules", "disclaimer": "Heuristic hints only; not a comprehensive audit or AI review."}
    if payload.use_ai:
        try:
            result["ai_review"] = ai_review(payload.code, payload.language)
            result["engine"] = "gemini+local-rules"
        except GeminiUnavailable:
            result["ai_warning"] = "AI review unavailable; local rules used instead."
    try:
        result["review_id"] = save_review(payload.language, result["engine"], len(findings), len(payload.code))
    except (OSError, sqlite3.Error):
        result["history_warning"] = "Review completed but history could not be saved."
    return result
