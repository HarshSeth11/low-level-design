from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, number_plate, vehicle_type):
        super().__init__(number_plate)
        self.vehicle_type = vehicle_type
        