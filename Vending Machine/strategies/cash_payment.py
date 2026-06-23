from strategies.payment_strategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def pay(self, amount : int):
        print(f"{amount} rupee is successfully paid via Cash")
        return {"amount": amount, "status": "success"}