from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass