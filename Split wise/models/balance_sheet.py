from decimal import Decimal

class BalanceSheet:

    def __init__(self):
        self.balances = {}

    def update_balance(self, user_id, delta):
        current = self.balances.get(user_id, Decimal("0"))
        new_balance = current + delta

        if new_balance == 0:
            self.balances.pop(user_id, None)
        else:
            self.balances[user_id] = new_balance