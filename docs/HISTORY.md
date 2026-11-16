# Review history (prototype)

The backend stores **metadata only** in SQLite after each successful `POST /review`: timestamp, language, engine, number of local findings and source character count. It **does not store source code, AI suggestions, prompts or API keys**.

- Default database: `codepilot-history.sqlite3` relative to the backend working directory.
- Set `CODEPILOT_DB_PATH=/path/to/private/history.sqlite3` to select a persistent volume.
- `GET /reviews?limit=20` returns newest metadata records; limit must be 1–100.
- The database is created on first review or history read.
- Back up or delete the database according to your own retention policy; automatic pruning is not implemented.
- If a database write fails, the review still returns findings with a `history_warning` instead of claiming it was saved.
- This API has **no authentication**. Do not expose review or history endpoints publicly until authentication and access controls are implemented.
- SQLite history is single-instance storage. Multiple distributed replicas need a shared database solution.

Run backend tests from `backend/` using `python -m unittest discover -s tests`. No claim of passing tests is made until CI or a local run verifies them.
