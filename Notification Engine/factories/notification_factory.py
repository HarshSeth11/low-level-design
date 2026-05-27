from notifications.email_notification import EmailNotification
from notifications.sms_notification import SmsNotification
from notifications.push_notification import PushNotification

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == 'email':
            return EmailNotification()
        elif notification_type == 'sms':
            return SmsNotification()
        elif notification_type == 'push':
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")