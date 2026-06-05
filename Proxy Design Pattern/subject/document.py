from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def view(self):
        pass
