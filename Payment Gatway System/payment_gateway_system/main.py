from facade.payment_facade import PaymentFacade


def main():
    payment_facade = PaymentFacade()
    payment_facade.process_payment(amount=100, currency="USD", gateway="Stripe")
    

if __name__ == "__main__":
    main()

