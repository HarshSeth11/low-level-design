from logger.logger import Logger  

class UserService:
    def __init__(self):
        self.logger = Logger()
    
    def create_user(self, user_details):
        self.logger.log(f"Creating user with details: {user_details}")
        # Logic to create user
        self.logger.log("User created successfully")