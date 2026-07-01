from models.show import Show

class ShowRepository:
    def __init__(self):
        self.shows = []

    def add_show(self, show: Show):
        self.shows.append(show)
        print(f"Show: {show.show_id} is successfully added to the show repository.")

    def get_show_by_id(self, show_id):
        for show in self.shows:
            if show.show_id == show_id:
                return show

        return None
    
    def get_all_shows(self):
        return self.shows
    
    def remove_show(self, show_id):
        for show in self.shows:
            if show.show_id == show_id:
                self.shows.remove(show)
                print(f"Show: {show.show_id} is successfully removed from the show repository.")
                return True
        return False

    def get_movie_shows(self, movie_id):
        movie_shows = []
        for show in self.shows:
            if show.movie.movie_id == movie_id:
                movie_shows.append(show)

        return movie_shows
    
    def get_shows_by_screen(self, screen_id):
        screen_shows = []
        for show in self.shows:
            if show.screen.screen_id == screen_id:
                screen_shows.append(show)
        return screen_shows