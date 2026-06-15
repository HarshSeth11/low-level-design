from payment_state import PaymentState

class SuccessState(PaymentState):
    def finish_payment(self, request):
        print("Payment is successful.")
    
    def initialize_payment(self, payment):
        print("finish previous payment.")

    def process_payment(self, payment):
        print("finish previous payment.")