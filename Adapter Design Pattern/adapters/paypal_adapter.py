from payment.payment_interface import Payment_Interface

class Paypal_Adapter(Payment_Interface):
    def __init__(self, paypal):
        self.paypal = paypal

    def pay(self, amount):
        self.paypal.make_payment(amount)