from models.product import Product


class Inventory:
    def __init__(self):
        self.products : list = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove(self, product_id: int):
        self.products = [
            product
            for product in self.products
            if product.id != product_id
        ]

    def is_available(self, product_id: int, quantity: int):

        for product in self.products:

            if product.id == product_id:
                return product.quantity >= quantity

        return False
    
    def get_product(self, product_id: int):
        for product in self.products:

            if product.id == product_id:
                return product