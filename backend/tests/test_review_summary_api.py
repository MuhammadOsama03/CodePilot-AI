import unittest
from fastapi.testclient import TestClient
from app.main import app

class ReviewSummaryApiTests(unittest.TestCase):
    def test_summary_matches_findings(self):
        response = TestClient(app).post("/review", json={"language": "python", "code": "print('test')"})
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["summary"]["total"], len(body["findings"]))
        self.assertEqual(body["summary"]["by_severity"]["low"], 1)
