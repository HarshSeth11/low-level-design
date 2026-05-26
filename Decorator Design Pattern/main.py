from beverages.simple_coffee import SimpleCoffee
from decorators.milk_decorator import MilkDecorator
from decorators.suger_decorator import SugerDecorator
from decorators.whipped_cream_decorator import WhippedCreamDecorator


def main():
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()} costs {coffee.cost()}")

    coffee = MilkDecorator(coffee)
    print(f"{coffee.get_description()} costs {coffee.cost()}")

    coffee = SugerDecorator(coffee)
    print(f"{coffee.get_description()} costs {coffee.cost()}")

    coffee = WhippedCreamDecorator(coffee)
    print(f"{coffee.get_description()} costs {coffee.cost()}")

if __name__ == "__main__":
    main()