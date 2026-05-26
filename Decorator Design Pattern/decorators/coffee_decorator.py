from beverages.coffee import Coffee

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self) -> str:
        return self._coffee.get_description()
    
    def cost(self) -> float:
        return self._coffee.cost()
    