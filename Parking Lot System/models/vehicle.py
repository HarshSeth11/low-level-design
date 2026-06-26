from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, number_plate, vehicle_type):
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type