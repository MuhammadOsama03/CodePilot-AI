from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .review_rules import review
from .summary import summarize
from .limits import MAX_SOURCE_CHARACTERS
from .gemini import ai_review, GeminiUnavailable

app = FastAPI(title="CodePilot AI API", version="0.5.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
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

@app.post("/review")
def review_code(payload: ReviewRequest):
    findings = review(payload.code, payload.language)
    result = {"language": payload.language, "findings": findings, "summary": summarize(findings),
              "engine": "local-rules", "disclaimer": "Heuristic hints only; not a comprehensive audit or AI review."}
    if payload.use_ai:
        try:
            result["ai_review"] = ai_review(payload.code, payload.language)
            result["engine"] = "gemini+local-rules"
        except GeminiUnavailable:
            result["ai_warning"] = "AI review unavailable; local rules used instead."
    return result
