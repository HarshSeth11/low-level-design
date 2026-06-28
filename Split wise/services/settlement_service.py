from models.users import User
from models.settlement import Settlement
from uuid import uuid4
from datetime import datetime

class SettlementService:

    def settle(self, from_user: User, to_user: User, amount):

        print("\n===================================")
        print("[SettlementService] Settlement Started")
        print("===================================")

        print(
            f"{from_user.name} pays "
            f"{to_user.name} ₹{amount}"
        )

        settlement = Settlement(
            f"SET-{uuid4()}",
            from_user,
            to_user,
            amount,
            datetime.now()
        )

        from_user.balance_sheet.update_balance(
            to_user.user_id,
            amount
        )

        to_user.balance_sheet.update_balance(
            from_user.user_id,
            -amount
        )

        settlement.payment_completed()

        print("Settlement Completed")

        return settlement