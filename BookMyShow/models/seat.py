from enums.seat_type import SeatType
from enums.seat_status import SeatStatus

class Seat:
    def __init__(self, seat_id: str, seat_number: str, row: str, column: int, seat_type: SeatType):
        self.seat_id = seat_id
        self.seat_number = seat_number
        self.row = row
        self.column = column
        self.seat_type = seat_type
        # NOTE: Seat status is per-show, managed by Show model, not globally
        # This seat object is reusable across multiple shows
