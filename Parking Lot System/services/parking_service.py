from models.parking_lot import ParkingLot
from models.ticket import Ticket
from models.vehicle import Vehicle

class ParkingService:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.parking_lot.floors:
            spot = floor.park_vehicle(vehicle)
            if spot:
                ticket = Ticket(f"TICKET-{floor.floor_id}-{spot.spot_id}", vehicle, floor.floor_id, spot.spot_id)
                self.parking_lot.tickets.append(ticket)
                return ticket
        return None
    