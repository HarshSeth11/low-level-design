class PaymentResponse:
    def __init__(self, status, message, transaction_id=None):
        self.status = status
        self.message = message
        self.transaction_id = transaction_id