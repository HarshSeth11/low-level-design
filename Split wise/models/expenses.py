from models.users import User
from models.group import Group
from strategies.split_strategies import SplitStrategies

class Expense:
    def __init__(self, expense_id, description, amount: int, payer: User, split_strategy: SplitStrategies, participants = None, group: Group = None):
        self.expense_id = expense_id
        self.description = description
        self.participants: list = participants or []
        self.amount = amount
        self.payer = payer
        self.group = group
        self.split_strategy = split_strategy
        self.splits = []

    # def split_expense(self):
    #     splits = self.split_strategy.split(self)
    #     self.splits = splits
        # for split in splits:
        #     payment_from = split.payment_from
        #     payment_to = split.payment_to
        #     payment_from.balance_sheet.add(split)
        #     payment_to.balance_sheet.add(split)

