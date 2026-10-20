import unittest

from service.routes import app
from service.models import Product


class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        Product._products = []
        Product._next_id = 1
        app.config["TESTING"] = True
        self.client = app.test_client()

        response = self.client.post("/api/products", json={
            "name": "Hat",
            "description": "A red fedora",
            "price": 20.0,
            "category": "Clothing",
            "available": True,
        })
        self.product_id = response.get_json()["id"]

    def test_read_product(self):
        response = self.client.get(
            f"/api/products/{self.product_id}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Hat")

    def test_update_product(self):
        response = self.client.put(
            f"/api/products/{self.product_id}",
            json={"description": "unknown"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["description"], "unknown")

    def test_delete_product(self):
        response = self.client.delete(
            f"/api/products/{self.product_id}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(Product.find(self.product_id))

    def test_list_all_products(self):
        response = self.client.get("/api/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_list_by_name(self):
        response = self.client.get("/api/products?name=Hat")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_list_by_category(self):
        response = self.client.get(
            "/api/products?category=Clothing"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_list_by_availability(self):
        response = self.client.get(
            "/api/products?available=true"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)


if __name__ == "__main__":
    unittest.main()