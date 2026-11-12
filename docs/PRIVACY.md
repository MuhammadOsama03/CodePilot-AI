# Source code privacy

CodePilot AI currently performs regex-based review locally in the FastAPI process. It does not send source code to an AI model.

Do not submit production secrets or proprietary code to an untrusted server. The API accepts up to 50,000 source characters and processes submitted code in memory. Avoid logging request bodies and place the API behind access controls before exposing it publicly.

CORS is a browser origin policy, not authentication. Current allowed origins are intended only for local development. The heuristic scanner does not provide a security guarantee.
