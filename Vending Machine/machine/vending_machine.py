from factory.payment_factory import PaymentFactory
from states.idle_state import IdleState
from inventory.inventory import Inventory

class VendingMachine:
    def __init__(self):
        self.current_state = IdleState()
        self.selected_product = None
        self.selected_quantity = 0
        self.inventory = Inventory()
        self.payment_strategy = None

    # def show_products(self):
    #     self.current_state.show_products(self)

    def select_product(self):
        self.current_state.select_product(self)

    def make_payment(self):
        self.payment_strategy = PaymentFactory().select_gateway()
        self.current_state.make_payment(self, self.payment_strategy)

    def dispense_product(self):
        self.current_state.dispense_product(self)

    def cancel_transaction(self):
        self.current_state.cancel_transaction(self)