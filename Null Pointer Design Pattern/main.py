from customer_factory import CustomerFactory

customer1 = CustomerFactory.get_customer("Harsh")
customer2 = CustomerFactory.get_customer("Mohit")

print(customer1.get_name())
print(customer2.get_name())