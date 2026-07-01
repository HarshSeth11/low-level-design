from models.show import Show
from enums.booking_status import BookingStatus

class Booking:
    def __init__(self, booking_id, user, show: Show, seats, status: BookingStatus):
        self.booking_id = booking_id
        self.user = user
        self.show = show
        self.seats = seats  # List of Seat objects
        self.status = status

    def confirm_booking(self):
        self.status = BookingStatus.COMPLETED
        print("Booking Confirmed!")
        return self
    
    def cancel_booking(self):
        self.status = BookingStatus.CANCELLED
        print("Booking Cancelled!")
        return self
    
    def get_total_price(self):
        """Calculate total price based on seats and show."""
        if not self.seats:
            return 0
        # This could be extended with dynamic pricing based on seat type
        return len(self.seats) * 100  # Base price per seat
    

