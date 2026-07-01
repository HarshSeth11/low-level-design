"""
BookMyShow - Main Application
Demonstrates how a single seat can be used in multiple shows at different times.

KEY INSIGHT:
- A Screen has physical Seats (reusable across all shows)
- Each Show tracks which seats are BOOKED specifically for that show
- The same seat can be booked in different shows because availability is PER-SHOW
"""

from datetime import date, time
from uuid import uuid4

from models.user import User
from models.theatre import Theatre
from models.screen import Screen
from models.movie import Movie
from models.show import Show
from models.booking import Booking
from enums.booking_status import BookingStatus

from repositories.theatre_repository import TheatreRepository
from repositories.movie_repository import MovieRepository
from repositories.show_repository import ShowRepository
from repositories.booking_repository import BookingRepository

from services.theatre_service import TheatreService
from services.movie_service import MovieService
from services.show_service import ShowService
from services.booking_service import BookingService
from services.seat_lock_service import SeatLockService


def print_section(title):
    """Pretty print section headers."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    # Initialize Repositories
    theatre_repo = TheatreRepository()
    movie_repo = MovieRepository()
    show_repo = ShowRepository()
    booking_repo = BookingRepository()
    
    # Initialize Services
    theatre_service = TheatreService(theatre_repo)
    movie_service = MovieService(movie_repo)
    show_service = ShowService(show_repo)
    seat_lock_service = SeatLockService(lock_timeout_minutes=5)
    booking_service = BookingService(booking_repo, seat_lock_service)
    
    # ===== CREATE MOVIES =====
    print_section("1. Creating Movies")
    
    movie1 = Movie("M001", "Avatar")
    movie2 = Movie("M002", "Inception")
    movie_repo.add_movie(movie1)
    movie_repo.add_movie(movie2)
    
    # ===== CREATE THEATRE AND SCREENS =====
    print_section("2. Creating Theatre with Screen")
    
    # Create a screen with 3 rows (A, B, C) and 5 seats per row
    screen_layout = {"A": 5, "B": 5, "C": 5}
    screen1 = Screen("SCREEN_001", "Screen 1 - Premium", screen_layout)
    
    theatre1 = Theatre("T001", "PVR Cinemas - Downtown", [screen1])
    theatre_repo.add_theatre(theatre1)
    
    print(f"\nScreen has {len(screen1.seats)} total seats:")
    for seat in screen1.seats[:5]:  # Print first 5 seats as example
        print(f"  - {seat.seat_number} (ID: {seat.seat_id})")
    print(f"  ... and {len(screen1.seats) - 5} more seats")
    
    # ===== CREATE MULTIPLE SHOWS =====
    print_section("3. Creating Multiple Shows for Same Screen")
    
    show_date = date(2026, 7, 5)
    
    # Morning Show - 10:00 AM
    show1 = Show(
        "SHOW_001",
        movie1,
        show_date,
        time(10, 0),
        time(12, 30),
        screen1
    )
    show_repo.add_show(show1)
    print(f"Show 1 (Morning): {movie1.name} @ 10:00 AM - 12:30 PM")
    
    # Afternoon Show - 3:00 PM
    show2 = Show(
        "SHOW_002",
        movie1,
        show_date,
        time(15, 0),
        time(17, 30),
        screen1
    )
    show_repo.add_show(show2)
    print(f"Show 2 (Afternoon): {movie1.name} @ 3:00 PM - 5:30 PM")
    
    # Evening Show - 7:00 PM
    show3 = Show(
        "SHOW_003",
        movie2,
        show_date,
        time(19, 0),
        time(21, 30),
        screen1
    )
    show_repo.add_show(show3)
    print(f"Show 3 (Evening): {movie2.name} @ 7:00 PM - 9:30 PM")
    
    # ===== CREATE USERS =====
    print_section("4. Creating Users")
    
    user1 = User("U001", "John Doe", "john@example.com")
    user2 = User("U002", "Jane Smith", "jane@example.com")
    print(f"User 1: {user1.name} ({user1.email})")
    print(f"User 2: {user2.name} ({user2.email})")
    
    # ===== DEMONSTRATE SEAT REUSABILITY ACROSS SHOWS =====
    print_section("5. Demonstrating Seat Reusability Across Shows")
    print("\nKey Point: The SAME physical seat (e.g., A1) exists in the screen")
    print("but is tracked separately for each show!\n")
    
    # Get seat A1 from the screen
    seat_a1 = None
    for seat in screen1.seats:
        if seat.seat_number == "A1":
            seat_a1 = seat
            break
    
    print(f"Seat Being Tested: {seat_a1.seat_number} (ID: {seat_a1.seat_id})")
    print(f"\nAvailability Status:")
    print(f"  Show 1 (10:00 AM): Available = {show1.is_seat_available(seat_a1.seat_id)}")
    print(f"  Show 2 (3:00 PM):  Available = {show2.is_seat_available(seat_a1.seat_id)}")
    print(f"  Show 3 (7:00 PM):  Available = {show3.is_seat_available(seat_a1.seat_id)}")
    
    # ===== BOOKING FOR SHOW 1 (10:00 AM) =====
    print_section("6. Booking Seats for Show 1 (10:00 AM)")
    
    # Get seats A1, A2, A3
    seats_for_show1 = [seat for seat in screen1.seats if seat.seat_number in ["A1", "A2", "A3"]]
    
    booking1 = Booking(
        f"B{uuid4().hex[:8]}",
        user1,
        show1,
        seats_for_show1,
        BookingStatus.PENDING
    )
    
    booking_repo.add_booking(booking1)
    print(f"Created booking {booking1.booking_id} for user {user1.name}")
    print(f"Seats: {', '.join([s.seat_number for s in seats_for_show1])}")
    
    # Confirm booking - this marks seats as booked IN SHOW 1 ONLY
    booking_service.confirm_booking(booking1.booking_id)
    print(f"Booking Confirmed! Price: ${booking1.get_total_price()}")
    
    # ===== CHECK AVAILABILITY AFTER BOOKING =====
    print_section("7. Availability After Booking in Show 1")
    
    print(f"\nSeat A1 Availability:")
    print(f"  Show 1 (10:00 AM): Available = {show1.is_seat_available(seat_a1.seat_id)} ✗ (BOOKED)")
    print(f"  Show 2 (3:00 PM):  Available = {show2.is_seat_available(seat_a1.seat_id)} ✓ (STILL AVAILABLE!)")
    print(f"  Show 3 (7:00 PM):  Available = {show3.is_seat_available(seat_a1.seat_id)} ✓ (STILL AVAILABLE!)")
    
    print(f"\n💡 Notice: Seat A1 is booked in Show 1 but STILL AVAILABLE in Shows 2 & 3!")
    
    # ===== BOOKING FOR SHOW 2 (3:00 PM) - SAME SEAT! =====
    print_section("8. Booking SAME Seat (A1) for Show 2 (3:00 PM)")
    
    seat_a1_for_show2 = [seat for seat in screen1.seats if seat.seat_number == "A1"]
    
    booking2 = Booking(
        f"B{uuid4().hex[:8]}",
        user2,
        show2,
        seat_a1_for_show2,
        BookingStatus.PENDING
    )
    
    booking_repo.add_booking(booking2)
    print(f"Created booking {booking2.booking_id} for user {user2.name}")
    print(f"Seat: A1 (same seat as in Show 1!)")
    
    booking_service.confirm_booking(booking2.booking_id)
    print(f"✓ Successfully booked! This proves the SAME SEAT can be used in multiple shows.")
    
    # ===== DISPLAY BOOKING SUMMARY =====
    print_section("9. Booking Summary")
    
    print(f"Show 1 (10:00 AM) - Booked Seats:")
    for seat in show1.get_booked_seats():
        print(f"  - {seat.seat_number}")
    print(f"Available Seats: {len(show1.get_available_seats())}")
    
    print(f"\nShow 2 (3:00 PM) - Booked Seats:")
    for seat in show2.get_booked_seats():
        print(f"  - {seat.seat_number}")
    print(f"Available Seats: {len(show2.get_available_seats())}")
    
    print(f"\nShow 3 (7:00 PM) - Booked Seats:")
    for seat in show3.get_booked_seats():
        print(f"  - {seat.seat_number}")
    print(f"Available Seats: {len(show3.get_available_seats())}")
    
    # ===== USER BOOKINGS =====
    print_section("10. User Booking History")
    
    user1_bookings = booking_service.get_user_all_bookings(user1.user_id)
    print(f"\n{user1.name}'s Bookings ({len(user1_bookings)}):")
    for booking in user1_bookings:
        print(f"  - {booking.show.movie.name} at {booking.show.start_time}")
        print(f"    Seats: {', '.join([s.seat_number for s in booking.seats])}")
        print(f"    Status: {booking.status.value}, Total: ${booking.get_total_price()}")
    
    user2_bookings = booking_service.get_user_all_bookings(user2.user_id)
    print(f"\n{user2.name}'s Bookings ({len(user2_bookings)}):")
    for booking in user2_bookings:
        print(f"  - {booking.show.movie.name} at {booking.show.start_time}")
        print(f"    Seats: {', '.join([s.seat_number for s in booking.seats])}")
        print(f"    Status: {booking.status.value}, Total: ${booking.get_total_price()}")
    
    # ===== GET MOVIES IN THEATRE =====
    print_section("11. Movies Available in Theatre")
    
    movies_in_theatre = theatre_service.get_all_movies_in_theatre(theatre1.theatre_id, show_repo)
    print(f"\nMovies in {theatre1.name}:")
    for movie in movies_in_theatre:
        print(f"  - {movie.name}")
    
    # ===== CANCEL BOOKING DEMO =====
    print_section("12. Cancelling a Booking")
    
    print(f"Cancelling {booking1.booking_id}...")
    booking_service.cancel_booking(booking1.booking_id)
    
    print(f"\nShow 1 - Booked Seats After Cancellation:")
    booked = show1.get_booked_seats()
    if booked:
        for seat in booked:
            print(f"  - {seat.seat_number}")
    else:
        print("  (No booked seats)")
    print(f"Available Seats: {len(show1.get_available_seats())}")
    
    # ===== FINAL SUMMARY =====
    print_section("Summary: How Multiple Shows Share Seats")
    
    print("""
✓ Single Seat Reusability Across Shows:
  
  1. SCREEN LEVEL: Each screen has a fixed set of physical seats
  2. SHOW LEVEL: Each show independently tracks which seats are booked
  3. BOOKING: When you book a seat, it's registered ONLY for that show
  
  Example with Seat A1:
  ├─ Show 1 (10:00 AM): A1 is BOOKED
  ├─ Show 2 (3:00 PM):  A1 is AVAILABLE (different show, different tracking)
  └─ Show 3 (7:00 PM):  A1 is AVAILABLE (different show, different tracking)
  
  The Same Physical Seat is Reused ✓
  Independent Availability Per Show ✓
  
Benefits:
  • Efficient memory usage (one seat object per physical seat)
  • Flexible booking (same seat available in multiple shows)
  • Clear separation of concerns (show-specific state vs seat properties)
    """)


if __name__ == "__main__":
    main()
