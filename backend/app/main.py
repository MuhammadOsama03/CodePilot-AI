from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .review_rules import review
from .summary import summarize
from .limits import MAX_SOURCE_CHARACTERS

app = FastAPI(title="CodePilot AI API", version="0.4.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class ReviewRequest(BaseModel):
    language: str = Field(pattern=r"^(python|javascript|typescript)$")
    code: str = Field(min_length=1, max_length=MAX_SOURCE_CHARACTERS)

@app.get("/health")
def health():
    return {"status": "ok", "phase": "prototype"}

@app.post("/review")
def review_code(payload: ReviewRequest):
    findings = review(payload.code, payload.language)
    return {"language": payload.language, "findings": findings, "summary": summarize(findings), "engine": "local-rules", "disclaimer": "Heuristic hints only; not a comprehensive audit or AI review."}
