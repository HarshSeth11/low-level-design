from strategies.pricing_strategy import PricingStrategy
import math

class HourlyPricing(PricingStrategy):
    RATE_PER_HOUR = 20

    def calculate_price(self, ticket):
        duration = ticket.exit_time - ticket.entry_time

        # Convert duration to hours
        hours = duration.total_seconds() / 3600

        # Charge for at least 1 hour
        hours = max(1, math.ceil(hours))

        return hours * self.RATE_PER_HOUR   # ₹20 per hour