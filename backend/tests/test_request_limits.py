import unittest
from fastapi.testclient import TestClient
from app.main import app

class RequestLimitTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_empty_source_rejected(self):
        self.assertEqual(self.client.post("/review", json={"language": "python", "code": ""}).status_code, 422)

    def test_oversized_source_rejected(self):
        self.assertEqual(self.client.post("/review", json={"language": "python", "code": "x" * 50001}).status_code, 422)

    def test_unknown_origin_not_allowed(self):
        response = self.client.options("/review", headers={
            "Origin": "https://untrusted.example",
            "Access-Control-Request-Method": "POST",
        })
        self.assertNotIn("access-control-allow-origin", response.headers)
