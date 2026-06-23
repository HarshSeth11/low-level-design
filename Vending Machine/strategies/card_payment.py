from strategies.payment_strategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def pay(self, amount : int):
        print(f"{amount} rupee is successfully paid via Card")
        return {"amount": amount, "status": "success"}