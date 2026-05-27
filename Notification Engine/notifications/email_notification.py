from notifications.base_notification import BaseNotification

class EmailNotification(BaseNotification):
    def send(self, user, message):
        print(f"Sending email to {user.email}: {message}\n")