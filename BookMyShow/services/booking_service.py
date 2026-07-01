

from enums.booking_status import BookingStatus
from models.booking import Booking

class BookingService:
    def __init__(self, booking_repository, seat_lock_service=None):
        self.booking_repository = booking_repository
        self.seat_lock_service = seat_lock_service
    
    def create_booking(self, booking_id, user, show, seats):
        """Create a new booking with selected seats."""
        booking = Booking(booking_id, user, show, seats, BookingStatus.PENDING)
        # Lock seats temporarily
        if self.seat_lock_service:
            for seat in seats:
                self.seat_lock_service.lock_seat(seat, booking_id)
        return self.booking_repository.add_booking(booking)
    
    def add_booking(self, booking):
        return self.booking_repository.add_booking(booking)

    def get_booking_by_id(self, booking_id):
        return self.booking_repository.get_booking_by_id(booking_id)
    
    def get_user_all_bookings(self, user_id):
        return self.booking_repository.get_user_all_bookings(user_id)

    def get_all_bookings(self):
        return self.booking_repository.get_all_bookings()
    
    def confirm_booking(self, booking_id):
        """Confirm a booking and mark seats as booked in the show."""
        booking = self.booking_repository.get_booking_by_id(booking_id)
        if booking:
            for seat in booking.seats:
                booking.show.book_seat_for_show(seat.seat_id)
            return self.booking_repository.confirm_booking(booking_id)
        return False
    
    def cancel_booking(self, booking_id):
        """Cancel a booking and release seats in the show."""
        booking = self.booking_repository.get_booking_by_id(booking_id)
        if booking:
            for seat in booking.seats:
                booking.show.release_seat_for_show(seat.seat_id)
            # Unlock seats
            if self.seat_lock_service:
                for seat in booking.seats:
                    self.seat_lock_service.unlock_seat(seat.seat_id, booking_id)
            return self.booking_repository.cancel_booking(booking_id)
        return False
    
    def get_booking_total_price(self, booking_id):
        """Get total price for a booking."""
        booking = self.booking_repository.get_booking_by_id(booking_id)
        if booking:
            return booking.get_total_price()
        return 0