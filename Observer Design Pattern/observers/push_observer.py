from .observer import Observer

class PushObserver(Observer):
    def __init__(self, username):
        self.username = username
    
    def update(self, data):
        print(f"PushObserver: Received update for {self.username} with data: {data}\n")
        