from payment_context import PaymentContext

def main():
    payment1 = PaymentContext()
    payment1.initialize_payment()
    payment1.process_payment()
    payment1.finish_payment()
    
if __name__ == "__main__":
    main()