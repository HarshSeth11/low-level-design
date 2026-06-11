from payment_gateway import PaymentGateway

class RazorpayGateway(PaymentGateway):
    
    def pay(self, amount):
        print(f"Processing payment of {amount} through Razorpay Gateway.\n")