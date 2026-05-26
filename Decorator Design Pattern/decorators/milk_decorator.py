from decorators.coffee_decorator import CoffeeDecorator

class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"

    def cost(self) -> float:
        return self._coffee.cost() + 20.0