from datetime import datetime, timedelta

class SeatLockService:
    """Service to manage temporary seat locks during booking process."""
    
    def __init__(self, lock_timeout_minutes=5):
        self.locked_seats = {}  # {seat_id: {booking_id, locked_at}}
        self.lock_timeout_minutes = lock_timeout_minutes
    
    def lock_seat(self, seat, booking_id):
        """Lock a seat temporarily for a booking."""
        seat.mark_locked()
        self.locked_seats[seat.seat_id] = {
            'booking_id': booking_id,
            'locked_at': datetime.now()
        }
        print(f"Seat {seat.seat_number} locked for booking {booking_id}")
    
    def unlock_seat(self, seat_id, booking_id):
        """Unlock a seat."""
        if seat_id in self.locked_seats:
            if self.locked_seats[seat_id]['booking_id'] == booking_id:
                del self.locked_seats[seat_id]
                print(f"Seat {seat_id} unlocked")
                return True
        return False
    
    def is_seat_locked(self, seat_id):
        """Check if a seat is currently locked."""
        if seat_id not in self.locked_seats:
            return False
        
        lock_info = self.locked_seats[seat_id]
        locked_at = lock_info['locked_at']
        elapsed = datetime.now() - locked_at
        
        # Check if lock has expired
        if elapsed > timedelta(minutes=self.lock_timeout_minutes):
            # Lock has expired, remove it
            del self.locked_seats[seat_id]
            return False
        
        return True
    
    def get_locked_seats_for_booking(self, booking_id):
        """Get all seats locked for a specific booking."""
        return [seat_id for seat_id, lock_info in self.locked_seats.items()
                if lock_info['booking_id'] == booking_id]
    
    def release_expired_locks(self):
        """Release all expired locks."""
        expired_seats = []
        for seat_id, lock_info in self.locked_seats.items():
            locked_at = lock_info['locked_at']
            elapsed = datetime.now() - locked_at
            if elapsed > timedelta(minutes=self.lock_timeout_minutes):
                expired_seats.append(seat_id)
        
        for seat_id in expired_seats:
            del self.locked_seats[seat_id]
            print(f"Lock expired for seat {seat_id}")
        
        return expired_seats

