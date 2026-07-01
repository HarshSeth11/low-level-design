from models.theatre import Theatre

class TheatreRepository:
    def __init__(self):
        self.theatres = []

    def add_theatre(self, theatre: Theatre):
        self.theatres.append(theatre)
        print(f"Theatre : {theatre.theatre_id} is added to the Theatre Repository.")

    def get_all_theatres(self):
        return self.theatres
    
    def remove_theatre(self, theatre_id):
        for theatre in self.theatres:
            if theatre.theatre_id == theatre_id:
                self.theatres.remove(theatre)
                print(f"Theatre : {theatre.theatre_id} is removed from the Theatre Repository.")
                break
    
    def get_theatre_by_id(self, theatre_id):
        for theatre in self.theatres:
            if theatre.theatre_id == theatre_id:
                return theatre
        return None
    
    def get_all_movies_in_theatre(self, theatre_id, show_repository):
        """Get all unique movies being shown in a particular theatre."""
        theatre = self.get_theatre_by_id(theatre_id)
        if not theatre:
            return []
        
        movies = []
        movie_ids = set()
        
        # Iterate through all screens in the theatre
        for screen in theatre.screens:
            # Get all shows for this screen
            shows = show_repository.get_shows_by_screen(screen.screen_id)
            # Collect unique movies
            for show in shows:
                if show.movie.movie_id not in movie_ids:
                    movie_ids.add(show.movie.movie_id)
                    movies.append(show.movie)
        
        return movies