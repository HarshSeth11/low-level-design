from payment_request_builder import PaymentRequestBuilder


request = (PaymentRequestBuilder()
            .set_amount(200)
            .set_gateway("PAYTM")
            .set_currency("INR")
            .set_customer_id("Harsh01")
            .set_description("Purchasing a AI Course.")
            .build())
    
print(request.__dict__)