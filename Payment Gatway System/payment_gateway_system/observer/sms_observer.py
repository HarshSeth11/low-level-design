from observer.observer import Observer
from singleton.logger import Logger

class SmsObserver(Observer):

    def __init__(self):
        # Initialize any necessary attributes for email notifications
        self.logger = Logger()

    def update(self, payment_response):
        # Logic to send SMS notification based on payment_response
        self.logger.info(f"SMS Notification: Payment status is {payment_response.status}")