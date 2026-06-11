from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, payment_response):
        pass