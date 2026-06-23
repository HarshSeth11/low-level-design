from models.product import Product
from machine.vending_machine import VendingMachine


def main():
    vending_machine = VendingMachine()
    product_list = [[1, "Coke", "40", 10],
                [2, "Diet Coke", "40", 7],
                [3, "Chips", "50", 7],
                [4, "kurukare", "70", 8]]
    
    for product_details in product_list:
        id = product_details[0]
        name = product_details[1]
        price = product_details[2]
        quantity = product_details[3]

        # creating a product object
        product = Product(id, name, price, quantity)

        # Adding the product in inventory
        vending_machine.inventory.add_product(product)
    

    vending_machine.select_product()

    vending_machine.make_payment()

    vending_machine.dispense_product()

if __name__ == "__main__":
    main()

    
