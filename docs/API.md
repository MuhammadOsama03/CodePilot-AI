# CodePilot AI prototype API

The backend uses local regex-based hints, not a hosted AI provider or a security audit.

## Endpoints

- `GET /health` returns prototype health metadata.
- `POST /review` accepts `{"language":"python","code":"print('hello')"}`.
- Supported languages: `python`, `javascript`, `typescript`.
- Source code is limited to 50,000 characters.
- Responses contain `findings`, `engine: local-rules`, and a disclaimer.

## Local development

Run the FastAPI server on port 8000 and Next.js on port 3000. CORS allows localhost and 127.0.0.1 on port 3000 only. Change allowed origins deliberately for deployments.

## Limitations

Regex patterns can produce false positives and miss vulnerabilities. Never paste credentials or confidential code into an untrusted deployment.
