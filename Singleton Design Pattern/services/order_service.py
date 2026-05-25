from logger.logger import Logger

class OrderService:
    def __init__(self):
        self.logger = Logger()
    
    def create_order(self, order_details):
        self.logger.log(f"Creating order with details: {order_details}")
        # Logic to create order
        self.logger.log("Order created successfully")   