class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify(self, payment_response):
        for observer in self.observers:
            observer.update(payment_response)