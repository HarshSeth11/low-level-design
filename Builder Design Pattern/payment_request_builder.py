from payment_request import PaymentRequest

class PaymentRequestBuilder:
    def __init__(self):
        self.request = PaymentRequest()

    def set_amount(self, amount) -> "PaymentRequestBuilder":
        self.request.amount = amount
        return self
    
    def set_currency(self, currency) -> "PaymentRequestBuilder":
        self.request.currency = currency
        return self

    def set_gateway(self, gateway) -> "PaymentRequestBuilder":
        self.request.gateway = gateway
        return self
    
    def set_customer_id(self, customer_id) -> "PaymentRequestBuilder":
        self.request.customer_id = customer_id
        return self
    
    def set_description(self, description) -> "PaymentRequestBuilder":
        self.request.description = description
        return self
    
    def build(self) -> PaymentRequest:
        return self.request
    