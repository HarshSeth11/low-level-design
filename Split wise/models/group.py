from models.users import User

class Group:
    def __init__(self, group_id: str, name: str, created_by: User):
        self.group_id = group_id
        self.name = name
        self.members = [created_by]
        self.expenses = []

    def add_member(self, user: User):
        self.members.append(user)
    
    def remove_member(self, user: User):
        self.members.remove(user)