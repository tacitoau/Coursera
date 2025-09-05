import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product


class ProductFactory(factory.Factory):
    """Creates fake Products"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(choices=[
        "Hat",
        "Pants",
        "Shirt",
        "Apple",
        "Banana",
        "Orange",
        "Potato",
        "Carrot",
        "Milk",
        "Eggs",
        "Cheese",
        "Bread",
        "Water",
        "Soda",
        "Juice",
        "Computer",
        "Keyboard",
        "Mouse",
        "Monitor",
        "Speaker",
    ])
    category = FuzzyChoice(choices=[
        "Clothes",
        "Food",
        "Beverage",
        "Electronics",
        "Home",
        "Outdoor",
        "Beauty",
        "Sports",
    ])
    available = FuzzyChoice(choices=[True, False])
    price = FuzzyDecimal(0.99, 1000.00)
