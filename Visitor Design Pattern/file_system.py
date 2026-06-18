from abc import ABC, abstractmethod
from visitors import Visitor

class FileSystem(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    @abstractmethod
    def accept(self, visitor : Visitor):
        pass

    