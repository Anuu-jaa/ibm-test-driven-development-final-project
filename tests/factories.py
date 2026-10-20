import factory
from factory import fuzzy
from service.models import Product


class ProductFactory(factory.Factory):
    """Factory for creating fake products."""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = fuzzy.FuzzyChoice(["Hat", "Shoes", "Big Mac", "Sheets"])
    description = factory.Faker("text")
    price = fuzzy.FuzzyFloat(0.5, 2000.0)
    category = fuzzy.FuzzyChoice(["Clothing", "Food", "Housewares"])
    available = factory.Faker("boolean")
