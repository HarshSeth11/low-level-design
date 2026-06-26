from abc import ABC, abstractmethod
from models.ticket import Ticket

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, ticket: Ticket):
        pass