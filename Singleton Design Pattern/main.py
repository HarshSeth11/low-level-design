from services import user_service, order_service, payment_service

def main():
    user_service_instance = user_service.UserService()
    order_service_instance = order_service.OrderService()
    payment_service_instance = payment_service.PaymentService()

    user_details = {"name": "John Doe", "email": "john.doe@example.com"}
    order_details = {"user_id": 1, "items": ["item1", "item2"]}
    payment_details = {"user_id": 1, "amount": 100.00} 

    user_service_instance.create_user(user_details)
    order_service_instance.create_order(order_details)
    payment_service_instance.process_payment(payment_details)

if __name__ == "__main__":
    main()