from models.movie import Movie
from models.screen import Screen
from datetime import date, time

class Show:
    def __init__(self, show_id: str, movie: Movie, show_date: date, start_time: time, end_time: time, screen: Screen):
        self.show_id = show_id
        self.movie = movie
        self.show_date = show_date
        self.start_time = start_time
        self.end_time = end_time
        self.screen = screen
        self.booked_seats = set()  # Track booked seats per show
    
    def is_seat_available(self, seat_id):
        """Check if a seat is available for this specific show."""
        return seat_id not in self.booked_seats
    
    def get_available_seats(self):
        """Get all available seats for this show."""
        available = []
        for seat in self.screen.seats:
            if self.is_seat_available(seat.seat_id):
                available.append(seat)
        return available
    
    def get_booked_seats(self):
        """Get all booked seats for this show."""
        booked = []
        for seat in self.screen.seats:
            if seat.seat_id in self.booked_seats:
                booked.append(seat)
        return booked
    
    def book_seat_for_show(self, seat_id):
        """Mark a seat as booked for this specific show."""
        if self.is_seat_available(seat_id):
            self.booked_seats.add(seat_id)
            return True
        return False
    
    def release_seat_for_show(self, seat_id):
        """Release a booked seat for this show."""
        if seat_id in self.booked_seats:
            self.booked_seats.discard(seat_id)
            return True
        return False