from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .review_rules import review

app = FastAPI(title="CodePilot AI API", version="0.3.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class ReviewRequest(BaseModel):
    language: str = Field(pattern=r"^(python|javascript|typescript)$")
    code: str = Field(min_length=1, max_length=50000)

@app.get("/health")
def health():
    return {"status": "ok", "phase": "prototype"}

@app.post("/review")
def review_code(payload: ReviewRequest):
    return {"language": payload.language, "findings": review(payload.code, payload.language), "engine": "local-rules", "disclaimer": "Heuristic hints only; not a comprehensive audit or AI review."}
