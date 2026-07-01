from models.movie import Movie

class MovieRepository:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)
        print(f"Movie: {movie.name} is added to the repository!")

    def get_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
            
        return None
    
    def get_all_movies(self):
        return self.movies

    def remove_movie(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                self.movies.remove(movie)
                print(f"Movie: {movie.name} is removed from the repository!")
                return True
        return False
    
    