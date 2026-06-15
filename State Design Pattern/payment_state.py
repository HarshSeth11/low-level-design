from abc import ABC, abstractmethod

class PaymentState(ABC):
    @abstractmethod
    def initialize_payment(self, payment):
        pass

    @abstractmethod
    def process_payment(self, payment):
        pass

    @abstractmethod
    def finish_payment(self, payment):
        pass
