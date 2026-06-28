from models.expenses import Expense
from models.users import User
from strategies.split_strategies import SplitStrategies
from strategies.equal_split import EqualSplit
from models.group import Group
from uuid import uuid4
from services.balance_service import BalanceService

class ExpenseService:
    def __init__(self):
        self.balance_sheet_service = BalanceService()
    
    def add_expense(self, description, amount: int, payer: User, split_strategy: SplitStrategies, participants = None, group: Group = None):

        print("\n===================================")
        print("[ExpenseService] Adding Expense")
        print("===================================")

        expense_id = f"EXP-{uuid4()}"

        expense = Expense(
            expense_id,
            description,
            amount,
            payer,
            split_strategy,
            participants,
            group
        )

        print(f"Description : {description}")
        print(f"Amount      : ₹{amount}")
        print(f"Payer       : {payer.name}")

        print("Participants:")
        for participant in participants:
            print(f"   • {participant.name}")

        expense.splits = split_strategy.split(expense)

        print("\nGenerated Splits")

        for split in expense.splits:
            print(
                f"   {split.from_user.name} "
                f"owes "
                f"{split.to_user.name} "
                f"₹{split.amount}"
            )

        self.balance_sheet_service.update_balance_sheet(expense.splits)

        if group:
            group.expenses.append(expense)
            print(f"\nExpense added to group '{group.name}'")

        print("Expense Created Successfully")

        return expense

            
            
