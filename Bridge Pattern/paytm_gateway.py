from payment_gateway import PaymentGateway

class PaytmGateway(PaymentGateway):
    
    def pay(self, amount):
        print(f"Processing payment of {amount} through Paytm Gateway.\n")