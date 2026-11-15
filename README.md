# CodePilot AI

An AI-assisted code review workspace for developers. **Work in progress — prototype; runtime and integration tests not yet verified.**

## Vision

Paste source code, select a language, and request a review that highlights potential bugs, security concerns, readability, and performance opportunities. Suggestions will be reviewed by a human rather than automatically applied.

## Planned stack

- **Frontend:** Next.js, React, TypeScript
- **Backend:** Python, FastAPI
- **AI integration:** Optional Gemini API with server-side key management and local fallback
- **Persistence (planned Nov 16):** SQLite
- **Testing:** Python unit tests exist; end-to-end verification and CI are pending

## Development stages

- [x] Project brief and repository initialization
- [x] Scaffold frontend and backend
- [x] Implement review UI (runtime verification pending)
- [x] Implement backend analysis endpoint and input validation
- [x] Implement opt-in Gemini provider with local fallback (live credentials not verified)
- [ ] Add history, tests, CI, and deployment documentation

> API and UI source code are present, but a deployed, end-to-end working AI review has not been demonstrated. Configure `GEMINI_API_KEY` only on the backend; do not use a `NEXT_PUBLIC_` key. Do not submit secrets or code you are not authorized to share. The rule-based review is heuristic, not a security certification.
