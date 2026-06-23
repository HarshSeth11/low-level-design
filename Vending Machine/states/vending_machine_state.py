from abc import ABC

class VendingMachineState(ABC):

    def select_product(self, machine, product_id, quantity):
        raise Exception("Operation not allowed")

    def make_payment(self, machine, payment_strategy):
        raise Exception("Operation not allowed")

    def dispense_product(self, machine):
        raise Exception("Operation not allowed")

    def cancel_transaction(self, machine):
        raise Exception("Operation not allowed")