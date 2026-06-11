from observer.subject import Subject
from observer.email_observer import EmailObserver
from singleton.logger import Logger
from observer.sms_observer import SmsObserver
from factory.payment_factory import PaymentGatewayFactory
from template.payment_processor import PaymentProcessor
from models.payment_request import PaymentRequest


class PaymentFacade:
    def __init__(self):
        self.logger = Logger()
        
    def process_payment(self, amount, currency, gateway):

        payment_request = PaymentRequest(amount=amount, currency=currency)

        subject = Subject()

        subject.attach(
            EmailObserver()
        )

        subject.attach(
            SmsObserver()
        )
        
        payment_gateway = PaymentGatewayFactory.create_gateway(gateway)
        payment_processor = PaymentProcessor(payment_gateway, subject)

        payment_processor.execute_payment(payment_request)