from notifications.base_notification import BaseNotification    

class PushNotification(BaseNotification):
    def send(self, user, message):
        print(f"Sending push notification to {user.username}: {message}\n")