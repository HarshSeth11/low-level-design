from abc import ABC, abstractmethod

class Colleague(ABC):
    
    def __init__(self, mediator):
        self._mediator = mediator
        self._mediator.register_colleague(self)

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def send_private(self, receiver, message):
        pass

    @abstractmethod
    def receive(self, sender, message):
        pass