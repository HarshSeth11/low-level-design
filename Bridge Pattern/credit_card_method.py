from payment_methods import PaymentMethod

class CreditCardPayment(PaymentMethod):

    def __init__(self, gateway):
        super().__init__(gateway)

    def make_payment(self, amount):
        print(f"Initiating credit card payment of {amount}.")
        self.gateway.pay(amount)