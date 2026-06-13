class PaymentRequest:
    def __init__(self, amount=None, currency=None, gateway=None, customer_id=None, description=None):
        self.amount = amount
        self.currency = currency
        self.gateway = gateway
        self.customer_id = customer_id
        self.description = description