from abc import ABC, abstractmethod

class SplitStrategies(ABC):
    @abstractmethod
    def split(self, expense):
        pass