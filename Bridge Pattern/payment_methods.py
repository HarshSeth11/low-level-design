from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, gateway):
        self.gateway = gateway

    @abstractmethod
    def make_payment(self, amount):
        pass