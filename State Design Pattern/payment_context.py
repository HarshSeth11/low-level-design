from created_state import CreatedState

class PaymentContext:
    def __init__(self):
        self.state = CreatedState()

    def set_state(self, state):
        self.state = state

    def initialize_payment(self):
        self.state.initialize_payment(self)

    def process_payment(self):
        self.state.process_payment(self)

    def finish_payment(self):
        self.state.finish_payment(self)