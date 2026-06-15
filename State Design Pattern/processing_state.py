from payment_state import PaymentState
from success_state import SuccessState

class ProcessingState(PaymentState):
    def process_payment(self, payment):
        print("Processing the payment")

        payment.set_state(SuccessState())
    
    def finish_payment(self, request):
        print("Process the previous payment.")
    
    def initialize_payment(self, payment):
        print("finish previous payment.")
