from payment.payment_interface import Payment_Interface

class Razorpay_Adapter(Payment_Interface):
    def __init__(self, razorpay):
        self.razorpay = razorpay

    def pay(self, amount):
        self.razorpay.process_payment(amount)