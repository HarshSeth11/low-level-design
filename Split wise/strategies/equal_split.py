from models.expenses import Expense
from models.split import Split
from decimal import Decimal, ROUND_DOWN

class EqualSplit:

    def split(self, expense: Expense):
        participants = expense.participants
        payer = expense.payer
        splits = []

        if not participants:
            return []


        # participants contain only the people sharing the expense.
        # payer may or may not be one of them.
        amount = Decimal(str(expense.amount))

        share = (amount / len(participants)).quantize(
            Decimal("0.01"),
            rounding=ROUND_DOWN
        )

        remaining = amount - share * len(participants)

        for i, participant in enumerate(participants):
            if participant.user_id == payer.user_id:
                continue

            final_share = share

            if i == len(participants) - 1:
                final_share += remaining

            splits.append(
                Split(
                    to_user=payer,
                    from_user=participant,
                    amount=final_share
                )
            )
        
        return splits