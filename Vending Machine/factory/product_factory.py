class ProductFactory:

    @staticmethod
    def choose_product(machine):

        inventory = machine.inventory

        print("Available Products")

        for product in inventory.products:
            print(
                f"ID: {product.id} | "
                f"Name: {product.name} | "
                f"Price: {product.price} | "
                f"Qty: {product.quantity}"
            )

        product_id = int(input("Enter product id: "))

        while not inventory.is_available(product_id, 1):
            product_id = int(input("Enter valid product id: "))

        quantity = int(input("Enter quantity: "))

        while not inventory.is_available(product_id, quantity):

            available = inventory.get_product(
                product_id
            ).quantity

            quantity = int(
                input(
                    f"Only {available} available. "
                    "Enter quantity again: "
                )
            )

        machine.selected_product = (
            inventory.get_product(product_id)
        )

        machine.selected_quantity = quantity

        return machine.selected_product
