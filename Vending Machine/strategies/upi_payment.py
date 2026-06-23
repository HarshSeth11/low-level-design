from strategies.payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    def pay(self, amount : int):
        print(f"{amount} rupee is successfully paid via UPI")
        return {"amount": amount, "status": "success"}