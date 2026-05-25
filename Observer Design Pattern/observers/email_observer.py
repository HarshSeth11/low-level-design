from .observer import Observer

class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, data):
        print(f"EmailObserver: Received update on {self.email} with data: {data}\n")