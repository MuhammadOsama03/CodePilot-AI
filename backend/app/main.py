from fastapi import FastAPI
from pydantic import BaseModel, Field
from .review_rules import review

app = FastAPI(title="CodePilot AI API", version="0.2.0")

class ReviewRequest(BaseModel):
    language: str = Field(min_length=1, max_length=40)
    code: str = Field(min_length=1, max_length=50000)

@app.get("/health")
def health():
    return {"status": "ok", "phase": "prototype"}

@app.post("/review")
def review_code(payload: ReviewRequest):
    return {"language": payload.language, "findings": review(payload.code), "engine": "local-rules", "disclaimer": "Heuristic hints only; not a comprehensive audit or AI review."}
