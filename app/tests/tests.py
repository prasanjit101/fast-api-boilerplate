import unittest
from fastapi.testclient import TestClient
from main import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_items(self):
        response = self.client.get("/items")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)

    def test_add_item(self):
        item_data = {"name": "Item 1", "description": "This is item 1"}
        response = self.client.post("/items", json=item_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Item added successfully")

if __name__ == '__main__':
    unittest.main()
