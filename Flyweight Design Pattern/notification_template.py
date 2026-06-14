class NotificationTemplate:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def send(self, user):
        print(
            f"Sending '{self.title}' "
            f"to {user}"
        )