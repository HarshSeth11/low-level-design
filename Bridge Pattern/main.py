from credit_card_method import CreditCardPayment
from debit_card_method import DebitCardMethod
from upi_method import UpiPayment
from paytm_gateway import PaytmGateway
from razorpay_gateway import RazorpayGateway

def main():
    # Gateways
    paytm_gateway = PaytmGateway()
    razorpay_gateway = RazorpayGateway()

    # Methods
    credit_card_method_1 = CreditCardPayment(paytm_gateway)
    debit_card_method_1 = DebitCardMethod(razorpay_gateway)
    upi_method_1 = UpiPayment(paytm_gateway)
    upi_method_2 = UpiPayment(razorpay_gateway)

    # call methods
    credit_card_method_1.make_payment(200)
    debit_card_method_1.make_payment(800)
    upi_method_1.make_payment(400)
    upi_method_2.make_payment(900)

if __name__ == '__main__':
    main()