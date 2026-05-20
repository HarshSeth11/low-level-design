from abc import ABC, abstractmethod

class BaseSortingStrategy(ABC):
    @abstractmethod
    def sort(self, data, metrics):
        pass