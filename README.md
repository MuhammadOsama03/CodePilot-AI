# CodePilot AI

An AI-assisted code review workspace for developers. **Five-day sprint status (2026-11-18): prototype, not publicly deployed or end-to-end verified.**

## Vision

Paste source code, select a language, and request a review that highlights potential bugs, security concerns, readability, and performance opportunities. Suggestions will be reviewed by a human rather than automatically applied.

## Planned stack

- **Frontend:** Next.js, React, TypeScript
- **Backend:** Python, FastAPI
- **AI integration:** Optional Gemini API with server-side key management and local fallback
- **Persistence:** SQLite metadata-only review history (see [history documentation](docs/HISTORY.md))
- **Testing:** GitHub Actions runs backend unit tests, frontend TypeScript checks and frontend build; browser-to-backend verification remains pending

## Development stages

- [x] Project brief and repository initialization
- [x] Scaffold frontend and backend
- [x] Implement review UI (runtime verification pending)
- [x] Implement backend analysis endpoint and input validation
- [x] Implement opt-in Gemini provider with local fallback (live credentials not verified)
- [x] Add metadata-only SQLite history, tests and backend CI
- [x] Add a frontend view for saved review metadata
- [x] Add optional operator access and a single-process review limit
- [ ] Complete browser integration tests and deployment verification

> API and UI source code are present, but a deployed, end-to-end working AI review has not been demonstrated. Configure `GEMINI_API_KEY` only on the backend; do not use a `NEXT_PUBLIC_` key. Do not submit secrets or code you are not authorized to share. The rule-based review is heuristic, not a security certification.

## Sprint closeout (November 18, 2026)

Source-level features include local rule-based reviews, optional Gemini calls with fallback, metadata-only SQLite review history, and a Next.js review interface. The backend supports `CODEPILOT_ALLOWED_ORIGINS` for explicitly configured frontend origins. The latest pre-closeout `main` CI run on November 17 succeeded; check [current Actions](https://github.com/MuhammadOsama03/CodePilot-AI/actions) for results of November 18 changes. No Gemini credential, live deployed endpoint or browser-to-backend smoke test was available for this closeout. No production deployment is claimed.

**Remaining release blockers:** per-user authentication and authorization, per-client gateway controls, persistent-volume configuration, production TLS/hosting, explicit CORS configuration, real Gemini response verification, and end-to-end browser tests. Until these are addressed, keep the API private. See [deployment checklist](docs/DEPLOYMENT.md).
