from logger.logger import Logger

class PaymentService:
    def __init__(self):
        self.logger = Logger()
    
    def process_payment(self, payment_details):
        self.logger.log(f"Processing payment with details: {payment_details}")
        # Logic to process payment
        self.logger.log("Payment processed successfully")