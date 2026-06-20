from real_customer import RealCustomer
from null_customer import NullCustomer
class CustomerFactory:
    customer = ["Harsh", "Rahul"]

    @staticmethod
    def get_customer(name):
        if name in CustomerFactory.customer:
            return RealCustomer(name)
        
        return NullCustomer()