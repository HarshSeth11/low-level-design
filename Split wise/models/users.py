from models.balance_sheet import BalanceSheet

class User:

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.balance_sheet = BalanceSheet()