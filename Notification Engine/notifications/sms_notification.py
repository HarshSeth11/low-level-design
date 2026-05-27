from notifications.base_notification import BaseNotification

class SmsNotification(BaseNotification):
    def send(self, user, message):
        print(f"Sending SMS to {user.phone}: {message}\n")