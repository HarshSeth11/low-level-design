from models.parking_lot import ParkingLot
from models.ticket import Ticket
from models.vehicle import Vehicle
from strategies.hourly_pricing import HourlyPricing

class ExitService:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        self.hourly_pricing = HourlyPricing()
    
    def free_space(self, ticket: Ticket):
        floor_id = ticket.floor_id
        
        ticket.set_exit_time()

        price = self.hourly_pricing.calculate_price(ticket)

        print(f"${price} has been charged for Vehicle Number Plate: {ticket.vehicle.number_plate}")

        for floor in self.parking_lot.floors:
            if floor.floor_id == floor_id:
                floor.free_space(ticket)
                break
        
        self.parking_lot.tickets.remove(ticket)