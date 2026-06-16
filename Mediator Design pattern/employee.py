from colleague import Colleague

class Employee(Colleague):

    def __init__(self, name, mediator):
        super().__init__(mediator)
        self.name = name
    
    def send(self, message):
        self._mediator.send(self, message)

    def send_private(self, receiver, message):
        self._mediator.send_private(self, receiver, message)

    def receive(self, sender, message):
        print(f"\n{self.name} Received message from {sender.name} - {message}")