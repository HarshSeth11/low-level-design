from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle
from models.ticket import Ticket
from enums.vehicle_type import VehicleType

class Floor:
    def __init__(self, floor_id, bike_spots: int, car_spots: int, truck_spots: int):
        self.floor_id = floor_id
        self.parking_spots = []
        self.available_bike_spots  = []
        self.available_car_spots = []
        self.available_truck_spots = []

        for i in range(bike_spots):
            parking_spot = ParkingSpot(f"#BIKE-{i+1}", VehicleType.BIKE)
            self.parking_spots.append(parking_spot)
            self.available_bike_spots.append(parking_spot)
            bike_spots-=1

        for i in range(car_spots):
            parking_spot = ParkingSpot(f"#CAR-{i+1}", VehicleType.CAR)
            self.parking_spots.append(parking_spot)
            self.available_car_spots.append(parking_spot)
            car_spots-=1

        for i in range(truck_spots):
            parking_spot = ParkingSpot(f"#TRUCK-{truck_spots}", VehicleType.TRUCK)
            self.parking_spots.append(parking_spot)
            self.available_truck_spots.append(parking_spot)
            truck_spots-=1

    def park_vehicle(self, vehicle: Vehicle):
        if vehicle.vehicle_type == VehicleType.BIKE and len(self.available_bike_spots) > 0:
            spot = self.available_bike_spots.pop()
            spot.park(vehicle)
            return spot
        elif vehicle.vehicle_type in [VehicleType.CAR, VehicleType.BIKE] and len(self.available_car_spots) > 0:
            spot = self.available_car_spots.pop()
            spot.park(vehicle)
            return spot
        elif vehicle.vehicle_type in [VehicleType.CAR, VehicleType.BIKE, VehicleType.TRUCK] and len(self.available_truck_spots) > 0:
            spot = self.available_truck_spots.pop()
            spot.park(vehicle)
            return spot
        return None
    
    def free_space(self, ticket: Ticket):
        spot_id: ParkingSpot = ticket.spot_id
        for spot in self.parking_spots:
            if spot.spot_id == spot_id:
                spot.free_space()
                if spot.spot_type == VehicleType.BIKE:
                    self.available_bike_spots.append(spot)
                elif spot.spot_type == VehicleType.CAR:
                    self.available_car_spots.append(spot)
                elif spot.spot_type == VehicleType.TRUCK:
                    self.available_truck_spots.append(spot)
        