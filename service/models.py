class Product:
    """Product model for the test-driven development project."""

    _products = []
    _next_id = 1

    def __init__(
        self,
        name=None,
        description=None,
        price=0.0,
        category=None,
        available=True,
        id=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.available = available

    def create(self):
        """Save a new product."""
        if self.id is None:
            self.id = Product._next_id
            Product._next_id += 1

        existing = Product.find(self.id)
        if existing is None:
            Product._products.append(self)
        return self

    def update(self):
        """Update an existing product."""
        for index, product in enumerate(Product._products):
            if product.id == self.id:
                Product._products[index] = self
                return self
        return None

    def delete(self):
        """Delete this product."""
        Product._products = [
            product for product in Product._products
            if product.id != self.id
        ]

    @classmethod
    def all(cls):
        return list(cls._products)

    @classmethod
    def find(cls, product_id):
        for product in cls._products:
            if product.id == product_id:
                return product
        return None

    @classmethod
    def find_by_name(cls, name):
        return [
            product for product in cls._products
            if product.name == name
        ]

    @classmethod
    def find_by_category(cls, category):
        return [
            product for product in cls._products
            if product.category == category
        ]

    @classmethod
    def find_by_availability(cls, available=True):
        return [
            product for product in cls._products
            if product.available == available
        ]