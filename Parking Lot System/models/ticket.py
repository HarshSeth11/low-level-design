from models.vehicle import Vehicle
from datetime import datetime

class Ticket:
    def __init__(self, ticket_id : str, vehicle: Vehicle, floor_id, spot_id):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.floor_id = floor_id
        self.entry_time = datetime.now()
        self.exit_time = None

    def set_exit_time(self):
        self.exit_time = datetime.now()
    