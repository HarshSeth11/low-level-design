from customer import Customer

class NullCustomer(Customer):

    def get_name(self):
        return "Customer Not Found!"