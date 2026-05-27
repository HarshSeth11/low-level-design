from models.user import User
from services.notification_service import NotificationService

def main():
    user1 = User("CodeWithHarsh", "codewithharsh@example.com", "+1234567890")

    user2 = User("JaneDoe", "janedoe@example.com", "+0987654321")

    notification_service = NotificationService()
    notification_service.send_notification("email", user1, "Welcome to the Notification Engine!")
    notification_service.send_notification("sms", user2, "Your order has been shipped!")
    notification_service.send_notification("push", user1, "You have a new message!")

if __name__ == "__main__":
    main()