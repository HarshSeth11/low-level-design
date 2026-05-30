from abc import ABC, abstractmethod

class Payment_Interface(ABC):
    @abstractmethod
    def pay(self, amount):
        pass