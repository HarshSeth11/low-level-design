from strategies.payment_gateway import PaymentGateway
from singleton.logger import Logger
from models.payment_response import PaymentResponse

class PaytmGateway(PaymentGateway):
    def __init__(self):
        self.logger = Logger()

    def process_payment(self, payment_request):
        # Implement Paytm-specific payment processing logic here
        self.logger.info(f"Processing payment of {payment_request.amount} {payment_request.currency} through Paytm.")
        return PaymentResponse(
            status="success",
            message="Payment processed successfully through Paytm."
        )