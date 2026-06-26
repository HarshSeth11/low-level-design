from models.floor import Floor
from models.vehicle import Vehicle
from models.ticket import Ticket
from strategies.hourly_pricing import HourlyPricing

class ParkingLot:
    def __init__(self):
        self.floors = []
        self.tickets = []
        self.hourly_pricing = HourlyPricing()
    
    def add_floor(self, bike_count, car_count, truck_count):
        print("\nadd_floor_working")
        floor_id = len(self.floors) + 1
        floor = Floor(f"FLOOR-{floor_id}", bike_count, car_count, truck_count)
        self.floors.append(floor)
        print(f"\nFloor added successfully")
    