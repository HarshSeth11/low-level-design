from customer import Customer

class RealCustomer(Customer):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name