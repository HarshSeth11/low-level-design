from strategies.upi_payment import UPIPayment
from strategies.cash_payment import CashPayment
from strategies.card_payment import CardPayment

class PaymentFactory:

    @staticmethod
    def select_gateway():

        payment_methods = {
            1: UPIPayment,
            2: CashPayment,
            3: CardPayment
        }

        while True:

            choice = int(input("""
1. UPI
2. Cash
3. Card

Enter choice: """))

            if choice in payment_methods:
                return payment_methods[choice]()

            print("Invalid choice!")