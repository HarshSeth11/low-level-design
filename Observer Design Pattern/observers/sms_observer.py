from .observer import Observer

class SMSObserver(Observer):
    def __init__(self, mobile):
        self.mobile = mobile

    def update(self, data):
        print(f"SMSObserver: Received update on {self.mobile} with data: {data}\n")