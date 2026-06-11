from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

        return self.next_handler
    
    @abstractmethod
    def handle(self, payment_request):
        pass