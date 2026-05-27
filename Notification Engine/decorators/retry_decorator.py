from notifications.base_notification import BaseNotification

class RetryDecorator(BaseNotification):
    def __init__(self, base_notification : BaseNotification):
        self.base_notification = base_notification

    def send(self, user, message):
        print("Retrying to send notification...")
        self.base_notification.send(user, message)