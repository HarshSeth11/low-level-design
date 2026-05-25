from observers.email_observer import EmailObserver
from observers.sms_observer import SMSObserver
from observers.push_observer import PushObserver
from subject.youtube_channel import Youtube_Channel

def main():
    channel = Youtube_Channel("CodeWithHarsh")

    email_observer = EmailObserver("harshsethr@gmail.com")

    sms_observer = SMSObserver("1234567890")

    push_observer = PushObserver("harshsethr")

    channel.subscribe(email_observer)
    channel.subscribe(sms_observer)
    channel.subscribe(push_observer)

    channel.upload_video("Observer Design Pattern in Python")

if __name__ == "__main__":
    main()