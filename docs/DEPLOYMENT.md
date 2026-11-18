# Deployment preparation (not a deployment record)

## Required services
- Python 3.11+ backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --host 127.0.0.1 --port 8000`.
- Node 22+ frontend: `cd frontend && npm install && npm run build && npm run start`.
- Configure `NEXT_PUBLIC_API_URL` **at frontend build time** to the public HTTPS backend URL.
- Configure `CODEPILOT_DB_PATH` to a writable persistent-volume path on the backend.
- Set `GEMINI_API_KEY` **only in the backend runtime secret store**; omit to use local review only.

## Deployment blockers / cautions
- Set `CODEPILOT_ALLOWED_ORIGINS` to a comma-separated list of exact HTTPS frontend origins (for example `https://app.example.com`). Wildcard `*` is ignored. Localhost origins are the development default.
- There is no user authentication or rate limiting. Do not expose review history or costly Gemini calls as an unrestricted public service.
- The review endpoint accepts source code and may forward it to Gemini when AI is enabled. Only submit code you are authorized to share.
- SQLite history contains metadata, not submitted source. Use one backend instance with persistent storage.
- No production hosting credentials, domain, or deployed URL have been provided.

## Smoke checks (must be executed; not claimed as passing)
1. GET `/health` and confirm 200.
2. POST `/review` with `{"language":"python","code":"print(1)","use_ai":false}`; verify local findings and `review_id`.
3. GET `/reviews` and confirm metadata history.
4. Verify AI-disabled and AI-failure fallback paths.
5. Open the built frontend, run a review and inspect browser network/CORS errors.
6. Verify TLS, secret redaction, restart persistence, access restrictions, and monitoring.
