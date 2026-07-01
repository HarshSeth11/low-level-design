

class MovieService:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def get_movie_by_id(self, movie_id):
        return self.movie_repository.get_movie_by_id(movie_id)
    
    def get_all_movies(self):
        return self.movie_repository.get_all_movies()
    
    def add_movie(self, movie):
        self.movie_repository.add_movie(movie)

    def remove_movie(self, movie_id):
        return self.movie_repository.remove_movie(movie_id)
    
    def get_movie_shows(self, movie_id, show_repository):
        return show_repository.get_movie_shows(movie_id)