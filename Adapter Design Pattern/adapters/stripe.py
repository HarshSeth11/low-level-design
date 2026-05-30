from payment.payment_interface import Payment_Interface

class Stripe_Adapter(Payment_Interface):
    def __init__(self, stripe):
        self.stripe = stripe

    def pay(self, amount):
        self.stripe.execute_payment(amount)