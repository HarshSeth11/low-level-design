from abc import ABC, abstractmethod

class BaseNotification(ABC):
    @abstractmethod
    def send(self, user, message):
        pass