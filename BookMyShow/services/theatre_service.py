class TheatreService:
    def __init__(self, theatre_repository):
        self.theatre_repository = theatre_repository
    
    def get_all_theatres(self):
        return self.theatre_repository.get_all_theatres()
    
    def add_theatre(self, theatre):
        self.theatre_repository.add_theatre(theatre)
    
    def remove_theatre(self, theatre_id):
        self.theatre_repository.remove_theatre(theatre_id)
    
    def get_theatre_by_id(self, theatre_id):
        return self.theatre_repository.get_theatre_by_id(theatre_id)
    
    def get_all_movies_in_theatre(self, theatre_id, show_repository):
        """Get all movies being shown in a particular theatre."""
        return self.theatre_repository.get_all_movies_in_theatre(theatre_id, show_repository)
