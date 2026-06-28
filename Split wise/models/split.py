from models.users import User

class Split:
    def __init__(self, to_user: User, from_user: User, amount: int):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount