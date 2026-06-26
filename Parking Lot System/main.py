from models.parking_lot import ParkingLot
from models.vehicle import Vehicle
from enums.vehicle_type import VehicleType
from services.parking_service import ParkingService
from services.exit_service import ExitService


def main():
    parking_lot = ParkingLot()
    parking_service = ParkingService(parking_lot)
    exit_service = ExitService(parking_lot)

    parking_lot.add_floor(10, 20, 5)
    parking_lot.add_floor(20, 5, 8)


    bike1 = Vehicle("PB70-WQ-7635", VehicleType.BIKE)        
    bike2 = Vehicle("PB70-WQ-7634", VehicleType.BIKE)
    car1 = Vehicle("PB70-WQ-7534", VehicleType.CAR)
    car2 = Vehicle("PB70-WQ-7534", VehicleType.CAR)
    truck1 = Vehicle("PB70-WQ-7834", VehicleType.TRUCK)

    ticket1 = parking_service.park_vehicle(bike1)
    ticket2 = parking_service.park_vehicle(bike2)
    ticket3 = parking_service.park_vehicle(car1)


    exit_service.free_space(ticket3)

    ticket4 = parking_service.park_vehicle(car2)
    exit_service.free_space(ticket1)
    exit_service.free_space(ticket2)
    exit_service.free_space(ticket4)

if __name__ == "__main__":
    main()