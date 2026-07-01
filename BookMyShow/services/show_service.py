
class ShowService:
    def __init__(self, show_repository):
        self.show_repository = show_repository

    def get_show_by_id(self, show_id):
        return self.show_repository.get_show_by_id(show_id)
    
    def add_show(self, show):
        self.show_repository.add_show(show)

    def get_all_shows(self):
        return self.show_repository.get_all_shows()
    
    def remove_show(self, show_id):
        self.show_repository.remove_show(show_id)

    def get_movie_shows(self, movie_id):
        return self.show_repository.get_movie_shows(movie_id)
    
    def get_shows_by_screen(self, screen_id):
        return self.show_repository.get_shows_by_screen(screen_id)
    