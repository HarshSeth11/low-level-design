from decimal import Decimal

from models.users import User
from strategies.equal_split import EqualSplit

from services.balance_service import BalanceService
from services.expense_service import ExpenseService
from services.group_service import GroupService
from services.settlement_service import SettlementService

from repositories.group_repository import GroupRepository


def print_balances(users):
    print("\n==============================")
    print("Current Balance Sheets")
    print("==============================")

    for user in users:
        print(f"\n{user.name}")

        if not user.balance_sheet.balances:
            print("  No pending balances")
            continue

        for other_user, amount in user.balance_sheet.balances.items():
            print(f"  {other_user} : {amount}")


def main():

    # -------------------------------
    # Services
    # -------------------------------
    group_repo = GroupRepository()

    balance_service = BalanceService()
    expense_service = ExpenseService()
    group_service = GroupService(group_repo)
    settlement_service = SettlementService()

    # -------------------------------
    # Users
    # -------------------------------
    harsh = User("U1", "Harsh", "harsh@gmail.com")
    rahul = User("U2", "Rahul", "rahul@gmail.com")
    aman = User("U3", "Aman", "aman@gmail.com")

    # -------------------------------
    # Create Group
    # -------------------------------
    group = group_service.create_group(
        "Goa Trip",
        harsh
    )

    group.add_member(rahul)
    group.add_member(aman)

    # -------------------------------
    # Expense 1
    # Harsh pays ₹900
    # Split among Harsh, Rahul, Aman
    # -------------------------------
    expense_service.add_expense(
        description="Dinner",
        amount=Decimal("900"),
        payer=harsh,
        participants=[harsh, rahul, aman],
        split_strategy=EqualSplit(),
        group=group
    )

    print_balances([harsh, rahul, aman])

    # -------------------------------
    # Settlement
    # Rahul pays Harsh ₹300
    # -------------------------------
    settlement_service.settle(
        from_user=rahul,
        to_user=harsh,
        amount=Decimal("300")
    )

    print_balances([harsh, rahul, aman])

    # -------------------------------
    # Expense 2
    # Aman pays ₹600
    # Split among Rahul and Aman
    # -------------------------------
    expense_service.add_expense(
        description="Taxi",
        amount=Decimal("600"),
        payer=aman,
        participants=[rahul, aman],
        split_strategy=EqualSplit(),
        group=group
    )

    print_balances([harsh, rahul, aman])


if __name__ == "__main__":
    main()