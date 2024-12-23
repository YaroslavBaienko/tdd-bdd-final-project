from tests.factories import ProductFactory
from service.models import Category


def test_product_factory():
    """Test the ProductFactory to ensure it creates valid fake products"""
    product = ProductFactory()

    # Assert attributes
    assert product.name in [
        "Hat",
        "Pants",
        "Shirt",
        "Apple",
        "Banana",
        "Pots",
        "Towels",
        "Ford",
        "Chevy",
        "Hammer",
        "Wrench",
    ]
    assert isinstance(product.description, str)
    assert 0.5 <= product.price <= 2000.0
    assert product.available in [True, False]
    assert product.category in [
        Category.UNKNOWN,
        Category.CLOTHS,
        Category.FOOD,
        Category.HOUSEWARES,
        Category.AUTOMOTIVE,
        Category.TOOLS,
    ]
