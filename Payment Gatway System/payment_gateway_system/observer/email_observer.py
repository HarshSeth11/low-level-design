from observer.observer import Observer
from singleton.logger import Logger

class EmailObserver(Observer):

    def __init__(self):
        # Initialize any necessary attributes for email notifications
        self.logger = Logger()

    def update(self, payment_response):
        # Logic to send email notification based on payment_response
        self.logger.info(f"Email Notification: Payment status is {payment_response.status}")