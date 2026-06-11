from chain.handler import Handler
from singleton.logger import Logger

class FraudHandler(Handler):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def handle(self, payment_request):
        if payment_request.amount > 10000:
            self.logger.error("Potential fraud detected: amount exceeds threshold.")
            raise ValueError("Potential fraud detected: amount exceeds threshold.")
        
        self.logger.info("Fraud check passed.")

        if self.next_handler:
            return self.next_handler.handle(payment_request)