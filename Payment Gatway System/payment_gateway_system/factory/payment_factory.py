from strategies.paytm_gateway import PaytmGateway
from strategies.razorpay_gateway import RazorpayGateway
from strategies.stripe_gateway import StripeGateway

class PaymentGatewayFactory:
    @staticmethod
    def create_gateway(gateway_type):

        gateway_name = gateway_type.upper()

        gateways = {
            "PAYTM": PaytmGateway,
            "RAZORPAY": RazorpayGateway,
            "STRIPE": StripeGateway
        }

        gateway_class = gateways.get(gateway_name)

        if not gateway_class:
            raise ValueError(f"Unsupported payment gateway: {gateway_type}")
        
        return gateway_class()
        