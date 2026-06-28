class BalanceService:

    def update_balance_sheet(self, splits):

        print("\n[BalanceService] Updating balances")

        for split in splits:

            from_user = split.from_user
            to_user = split.to_user

            print(
                f"  {from_user.name} owes "
                f"{to_user.name} ₹{split.amount}"
            )

            to_user.balance_sheet.update_balance(
                from_user.user_id,
                split.amount
            )

            from_user.balance_sheet.update_balance(
                to_user.user_id,
                -split.amount
            )

        print("[BalanceService] Updated Successfully")