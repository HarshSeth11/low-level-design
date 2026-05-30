from gateways.paypal import Paypal
from gateways.razorpay import Razorpay
from gateways.stripe import Stripe
from adapters.paypal_adapter import Paypal_Adapter
from adapters.razorpay import Razorpay_Adapter
from adapters.stripe import Stripe_Adapter

from payment.payment_service import Payment_Service


def main():
    # Create instances of payment gateways
    paypal = Paypal()
    razorpay = Razorpay()
    stripe = Stripe()

    # Create adapters for each gateway
    paypal_adapter = Paypal_Adapter(paypal)
    razorpay_adapter = Razorpay_Adapter(razorpay)
    stripe_adapter = Stripe_Adapter(stripe)

    # Create payment service instances for each adapter
    paypal_service = Payment_Service(paypal_adapter)
    razorpay_service = Payment_Service(razorpay_adapter)
    stripe_service = Payment_Service(stripe_adapter)

    # Process payments through adapters
    paypal_service.process_payment(100)
    razorpay_service.process_payment(200)
    stripe_service.process_payment(300)

if __name__ == "__main__":
    main()