from enums.payment_status import PaymentStatus

class Settlement:
    def __init__(self, settlement_id, payer, receiver, amount, timestamp):
        self.settlement_id = settlement_id
        self.payer = payer
        self.receiver = receiver
        self.amount = amount
        self.status = PaymentStatus.PENDING
        self.timestamp = timestamp

    def payment_completed(self):
        self.status = PaymentStatus.SUCCESS

    def payment_failed(self):
        self.status = PaymentStatus.FAILED