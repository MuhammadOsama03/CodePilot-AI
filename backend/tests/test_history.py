import os
import tempfile
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.history import save_review, list_reviews
from app.main import app

class HistoryTests(unittest.TestCase):
    def test_persists_only_metadata_and_orders_newest_first(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"CODEPILOT_DB_PATH": os.path.join(directory, "history.db")}):
                first = save_review("python", "local-rules", 1, 100)
                second = save_review("typescript", "gemini+local-rules", 2, 200)
                rows = list_reviews()
                self.assertEqual([row["id"] for row in rows], [second, first])
                self.assertEqual(rows[0]["source_characters"], 200)
                self.assertNotIn("code", rows[0])
                self.assertEqual(len(list_reviews(1)), 1)
                with self.assertRaises(ValueError):
                    list_reviews(101)

    def test_review_endpoint_writes_history(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"CODEPILOT_DB_PATH": os.path.join(directory, "history.db")}):
                client = TestClient(app)
                response = client.post("/review", json={"language": "python", "code": "print('hello')"})
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json()["review_id"], int)
                history = client.get("/reviews?limit=1")
                self.assertEqual(history.status_code, 200)
                self.assertEqual(len(history.json()["reviews"]), 1)
                self.assertNotIn("print", str(history.json()))
                self.assertEqual(client.get("/reviews?limit=101").status_code, 422)
