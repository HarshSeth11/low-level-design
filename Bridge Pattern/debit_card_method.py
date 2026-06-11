from payment_methods import PaymentMethod

class DebitCardMethod(PaymentMethod):

    def __init__(self, gateway):
        super().__init__(gateway)

    def make_payment(self, amount):
        print(f"Initiating debit card payment of {amount}.")
        self.gateway.pay(amount)