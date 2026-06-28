class GroupRepository:
    def __init__(self):
        self.groups = {}

    def save(self, group):
        self.groups[group.group_id] = group

    def get(self, group_id):
        return self.groups.get(group_id)

    def get_by_user_id(self, user_id):
        groups = []

        for group in self.groups.values():
            for member in group.members:
                if member.user_id == user_id:
                    groups.append(group)
                    break   # No need to check remaining members

        return groups