import unittest
from fastapi.testclient import TestClient
from app.main import app

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code, 200)

    def test_review(self):
        result = self.client.post("/review", json={"language": "python", "code": "print('hello')"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["engine"], "local-rules")

    def test_reject_unknown_language(self):
        self.assertEqual(self.client.post("/review", json={"language": "ruby", "code": "puts 1"}).status_code, 422)

    def test_local_preflight(self):
        response = self.client.options("/review", headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["access-control-allow-origin"], "http://localhost:3000")
