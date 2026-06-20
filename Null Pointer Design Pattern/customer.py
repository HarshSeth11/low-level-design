from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_name(self):
        pass