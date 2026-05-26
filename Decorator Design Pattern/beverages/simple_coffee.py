from beverages.coffee import Coffee

class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Simple Coffee"

    def cost(self) -> float:
        return 100.0
