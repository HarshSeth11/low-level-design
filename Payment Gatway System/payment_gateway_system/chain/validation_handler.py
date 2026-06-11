from chain.handler import Handler
from singleton.logger import Logger

class ValidationHandler(Handler):
    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def handle(self, payment_request):
        if not payment_request.amount or not payment_request.currency:
            raise ValueError("Invalid payment request: amount and currency are required.")
        if payment_request.amount <= 0:
            raise ValueError("Invalid payment request: amount must be greater than zero.")
        self.logger.info("Validation passed.")
        if self.next_handler:
            return self.next_handler.handle(payment_request)