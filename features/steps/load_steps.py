from behave import given
from service.models import Product


@given("the following products")
def load_products(context):
    """Load sample products for BDD scenarios."""
    Product._products = []
    Product._next_id = 1

    products = [
        {
            "name": "Hat",
            "description": "A red fedora",
            "price": 20.0,
            "category": "Clothing",
            "available": True,
        },
        {
            "name": "Shoes",
            "description": "Running shoes",
            "price": 50.0,
            "category": "Clothing",
            "available": False,
        },
        {
            "name": "Big Mac",
            "description": "A burger",
            "price": 5.0,
            "category": "Food",
            "available": True,
        },
        {
            "name": "Sheets",
            "description": "Cotton bed sheets",
            "price": 30.0,
            "category": "Housewares",
            "available": True,
        },
    ]

    for data in products:
        Product(**data).create()