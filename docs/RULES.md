# Heuristic rule catalog

CodePilot AI currently uses a small set of regular-expression rules:

- `possible-secret`: literal credential-like assignments
- `debug-output`: common print and console output
- `python-eval`: Python eval calls
- `javascript-eval`: JavaScript and TypeScript eval calls

These patterns are approximate and may miss risky code or flag harmless examples. A finding is a prompt for human review, not proof of a vulnerability. The backend also returns severity counts in the review response.
