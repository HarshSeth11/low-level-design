class Payment_Service:
    def __init__(self, payment_interface):
        self.payment_interface = payment_interface

    def process_payment(self, amount):
        print(f"\nInitiating payment of {amount}. on {self.payment_interface.__class__.__name__}")
        self.payment_interface.pay(amount)
        print(f"Payment of {amount} completed using {self.payment_interface.__class__.__name__}.\n")