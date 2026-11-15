# Quality gates for a public release

- Run backend unit tests and API contract tests.
- Verify frontend type checking and production build.
- Verify AI failure falls back to local heuristics without leaking provider errors.
- Check source length, whitespace, and invalid language handling.
- Ensure provider API keys stay server-side and outside version control.
- Verify secrets and submitted source are not logged.
- Check accessible form labels, keyboard navigation, and loading states.
- Confirm security claims match implemented behavior.

This is a checklist, not evidence that these checks passed.
