from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="CodePilot AI API", version="0.1.0")


class ReviewRequest(BaseModel):
    language: str = Field(min_length=1, max_length=40)
    code: str = Field(min_length=1, max_length=50000)


@app.get("/health")
def health():
    return {"status": "ok", "phase": "foundation"}


# AI review implementation will be added in a later milestone.
