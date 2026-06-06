from abc import ABC, abstractmethod

class LeaveHandler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        pass