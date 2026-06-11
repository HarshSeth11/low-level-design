from payment_methods import PaymentMethod

class UpiPayment(PaymentMethod):

    def __init__(self, gateway):
        super().__init__(gateway)

    def make_payment(self, amount):
        print(f"Initiating UPI payment of {amount}.")
        self.gateway.pay(amount)