import os
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.gemini import ai_review, GeminiUnavailable

class GeminiTests(unittest.TestCase):
    def test_missing_key_is_safe(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": ""}):
            with self.assertRaises(GeminiUnavailable):
                ai_review("print('hello')", "python")

    def test_ai_opt_in_falls_back_without_key(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": ""}):
            response = TestClient(app).post("/review", json={"language": "python", "code": "print('hello')", "use_ai": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["engine"], "local-rules")
        self.assertIn("ai_warning", response.json())

    def test_default_does_not_call_external_provider(self):
        with patch("app.main.ai_review", side_effect=AssertionError("unexpected call")):
            response = TestClient(app).post("/review", json={"language": "python", "code": "print('hello')"})
        self.assertEqual(response.status_code, 200)
