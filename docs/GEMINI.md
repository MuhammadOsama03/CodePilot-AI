# Optional Gemini review

The API always supports local heuristic review. AI review is **opt-in** per request:

```json
{"language":"python","code":"print('hello')","use_ai":true}
```

Set `GEMINI_API_KEY` **only in the backend environment**, never in Next.js public variables or committed files. Optional `GEMINI_MODEL` supports `gemini-2.5-flash` (default) or `gemini-2.5-flash-lite`. Do not send secrets, private code, or regulated data to an external provider without authorization. Provider calls have a 12-second timeout and response-size cap. If unavailable, the API returns local findings plus `ai_warning`; no fake AI results are produced. AI suggestions require human verification. No production rate limiting, authentication, or persistence exists yet.
