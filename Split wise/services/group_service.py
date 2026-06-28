from models.group import Group
from models.users import User
from repositories.group_repository import GroupRepository
from uuid import uuid4

class GroupService:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def create_group(self, name, created_by: User):
        print(f"\n[GroupService] Creating group '{name}'")

        group = Group(
            group_id=f"GROUP-{uuid4()}",
            name=name,
            created_by=created_by
        )

        self.group_repository.save(group)

        print(f"[GroupService] Group created successfully")
        print(f"  Group ID : {group.group_id}")
        print(f"  Members  : {[user.name for user in group.members]}")

        return group