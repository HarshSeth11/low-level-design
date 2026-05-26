from decorators.coffee_decorator import CoffeeDecorator

class SugerDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Suger"

    def cost(self) -> float:
        return self._coffee.cost() + 10.0