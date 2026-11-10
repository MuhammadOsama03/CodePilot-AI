# Development notes

## Run locally

Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload` (port 8000).

Frontend: `cd frontend && npm install && npm run dev` (port 3000).

The frontend expects the API at `NEXT_PUBLIC_API_URL` (default localhost:8000). Cross-origin requests require configuring FastAPI CORS before browser integration works; this is **not yet implemented**.

## Test backend rules

From `backend`: `python -m unittest discover -s tests -v`.

## Limitations

The review endpoint uses simple local patterns. It does not execute code or call an AI provider. Findings can be false positives and do not replace professional review. No history, authentication, persistence or deployment configuration exists yet.
