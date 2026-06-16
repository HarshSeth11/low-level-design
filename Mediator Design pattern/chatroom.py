from mediator import Mediator

class ChatRoom(Mediator):
    def __init__(self):
        self._colleagues = []

    def register_colleague(self, mediator):
        self._colleagues.append(mediator)

    def send(self, sender, message):
        print(f"\n{sender.name} Broadcast message : ")
        for employee in self._colleagues:
            if employee == sender:
                continue

            employee.receive(sender, message)


    def send_private(self, sender, receiver, message):
        for employee in self._colleagues:
            if employee == receiver:
                print(f"\n{sender.name} messaged {receiver.name} Privately -")
                employee.receive(sender, message)           
