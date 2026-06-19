from database_memento import DatabaseMemento

class Database:
    def __init__(self):
        self.record = {}

    def insert(self, key, val):
        self.record[key] = val

    def update(self, key, val):
        self.record[key] = val

    def delete(self, key):
        del self.record[key]

    def create_memento(self):
        return DatabaseMemento(self.record)
    
    def restore_from_memento(self, memento):
        self.record = memento.get_state()
        print("Data restored from backup!")

    def display(self):
        if self.record is None:
            print(f"No records in Database!")
            return
        for key, value in self.record.items():
            print(f"{key} : {value}")
