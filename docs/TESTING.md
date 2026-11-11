# Backend checks

From the `backend` directory:

```bash
python -m pip install -r requirements.txt
python -m pip install httpx
python -m unittest discover -s tests -v
```

`httpx` is used by FastAPI's TestClient. These tests check response validation, local CORS preflight, request bounds, and heuristic rule behavior. They do not test the frontend build, security effectiveness, or production deployment.
