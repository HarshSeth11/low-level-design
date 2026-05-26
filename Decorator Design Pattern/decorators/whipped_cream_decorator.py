from decorators.coffee_decorator import CoffeeDecorator

class WhippedCreamDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Whipped Cream"

    def cost(self) -> float:
        return self._coffee.cost() + 30.0