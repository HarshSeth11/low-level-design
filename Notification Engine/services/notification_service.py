from factories.notification_factory import NotificationFactory

class NotificationService:
    def send_notification(self, notification_type, user, message):
        notification = NotificationFactory.create_notification(notification_type)
        notification.send(user, message)