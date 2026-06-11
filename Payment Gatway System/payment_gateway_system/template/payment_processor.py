from singleton.logger import Logger
from chain.fraud_handler import FraudHandler
from chain.validation_handler import ValidationHandler

class PaymentProcessor:

    def __init__(self, gateway, subject):
        self.gateway = gateway
        self.subject = subject
        self.logger = Logger()

        self.validation_handler = ValidationHandler()
        self.fraud_handler = FraudHandler()

        self.validation_handler.set_next_handler(self.fraud_handler)

        

    def execute_payment(self, payment_request):

        try:
            self.validate(payment_request)

            self.initialize_transaction(payment_request)

            response = self.gateway.process_payment(
                payment_request
            )

            self.generate_receipt(response)

            self.send_notification(response)

            return response

        except Exception as e:

            self.logger.error(
                f"Payment Failed: {str(e)}"
            )

        raise


    def validate(self, payment_request):
        self.logger.info(
            "Starting validation chain..."
        )
        self.validation_handler.handle(payment_request)

    def initialize_transaction(self, payment_request):

        self.logger.info(
            "Initializing transaction..."
        )

    def generate_receipt(self, payment_response):

        self.logger.info(
            f"Generating receipt for transaction."
            f"\nStatus: {payment_response.status}"
            f"\nMessage: {payment_response.message}"
        )

    def send_notification(self, payment_response):
        self.subject.notify(payment_response)

        self.logger.info(
            "Observers notified successfully."
        )