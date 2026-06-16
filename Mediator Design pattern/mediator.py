from abc import ABC, abstractmethod

class Mediator(ABC):
    
    @abstractmethod
    def register_colleague(self, mediator):
        pass

    @abstractmethod
    def send(self, sender, message):
        pass

    @abstractmethod
    def send_private(self, sender, receiver, message):
        pass