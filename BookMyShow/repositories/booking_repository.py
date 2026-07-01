from models.booking import Booking

class BookingRepository:
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking: Booking):
        self.bookings.append(booking)
        print(f"Booking id: {booking.booking_id} is successfully added to the Repository.")
        return True

    def get_booking_by_id(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
            
        return None

    def get_user_all_bookings(self, user_id):
        user_bookings = []
        for booking in self.bookings:
            if booking.user.user_id == user_id:
                user_bookings.append(booking)

        return user_bookings
    
    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.cancel_booking()
                return True
        return False
    
    def confirm_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.confirm_booking()
                return True
        return False
    
    def get_all_bookings(self):
        return self.bookings
    