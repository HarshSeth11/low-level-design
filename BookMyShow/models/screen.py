from models.seat import Seat
from uuid import uuid4
from enums.seat_type import SeatType

class Screen:
    def __init__(self, screen_id: str, screen_name:str, seat_layout: dict):
        self.screen_id = screen_id
        self.screen_name = screen_name
        self.seat_layout = seat_layout
        self.seats = []

        self._add_seats()

    def _add_seats(self):

        for row in sorted(self.seat_layout.keys()):
            count = self.seat_layout[row]
            if count <= 0:
                raise ValueError("count should be greater than 0.")
            for col in range(1, count + 1):
                seat_name = row+str(col)
                seat = Seat(f"{self.screen_id}-{seat_name}", seat_name, row, col, SeatType.REGULAR)

                self.seats.append(seat)