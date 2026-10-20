
import unittest

from service.models import Product
from tests.factories import ProductFactory


class TestProduct(unittest.TestCase):

    def setUp(self):
        Product._products = []
        Product._next_id = 1

    def test_read_a_product(self):
        product = ProductFactory(id=None)
        self.assertIsNone(product.id)
        product.create()
        self.assertIsNotNone(product.id)

        found = Product.find(product.id)
        self.assertEqual(found.id, product.id)
        self.assertEqual(found.name, product.name)
        self.assertEqual(found.description, product.description)
        self.assertEqual(found.price, product.price)

    def test_update_a_product(self):
        product = ProductFactory(id=None)
        product.create()
        original_id = product.id

        product.description = "testing"
        product.update()

        found = Product.find(original_id)
        self.assertEqual(found.id, original_id)
        self.assertEqual(found.description, "testing")
        self.assertEqual(len(Product.all()), 1)

    def test_delete_a_product(self):
        product = ProductFactory(id=None)
        product.create()
        product.delete()

        self.assertIsNone(Product.find(product.id))
        self.assertEqual(len(Product.all()), 0)

    def test_list_all_products(self):
        products = ProductFactory.create_batch(5)
        for product in products:
            product.create()

        self.assertEqual(len(Product.all()), 5)

    def test_find_by_name(self):
        products = ProductFactory.create_batch(5, name="Hat")
        for product in products:
            product.create()

        found = Product.find_by_name("Hat")
        self.assertEqual(len(found), 5)

        for product in found:
            self.assertEqual(product.name, "Hat")

    def test_find_by_category(self):
        products = ProductFactory.create_batch(
            5, category="Clothing"
        )
        for product in products:
            product.create()

        found = Product.find_by_category("Clothing")
        self.assertEqual(len(found), 5)

        for product in found:
            self.assertEqual(product.category, "Clothing")

    def test_find_by_availability(self):
        product = ProductFactory(id=None, available=True)
        product.create()

        found = Product.find_by_availability(True)
        self.assertIn(product, found)


if __name__ == "__main__":
    unittest.main()