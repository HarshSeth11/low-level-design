from payment_state import PaymentState
from processing_state import ProcessingState

class CreatedState(PaymentState):
    def initialize_payment(self, payment):
        print("Payment request is created.")

        payment.set_state(ProcessingState())

    def process_payment(self, payment):
        print("Initialize the payment.")

    def finish_payment(self, payment):
        print("Initialize the payment.")