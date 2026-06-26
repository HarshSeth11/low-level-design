from abc import ABC, abstractmethod
from enums.spot_type import SpotType

class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None
        self.is_occupied = False

    def can_fit(self, vehicle):
        if self.spot_type == "BIKE" and vehicle.vehicle_type == "Bike":
            return True
        elif self.spot_type == "CAR" and vehicle.vehicle_type in ["Bike", "CAR"]:
            return True
        elif self.spot_type == "TRUCK" and vehicle.vehicle_type in ["Bike", "CAR", "TRUCK"]:
            return True
        return False
    

    def is_available(self):
        print(f"\nSpot is {'available' if not self.is_occupied else 'not available'}")
        return not self.is_occupied

    def park(self, vehicle):
        self.vehicle = vehicle
        self.is_occupied = True
        print(f"\nVehicle - {self.vehicle.number_plate} is parked at {self.spot_id}")

    def free_space(self):
        self.vehicle = None
        self.is_occupied = False
        print(f"\nspot - {self.spot_id} is free")