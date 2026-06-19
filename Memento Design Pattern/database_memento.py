import copy

class DatabaseMemento:
    def __init__(self, record):
        self.record = copy.deepcopy(record)

    def get_state(self):
        return copy.deepcopy(self.record)