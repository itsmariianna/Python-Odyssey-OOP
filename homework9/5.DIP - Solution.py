from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def sending_message(self, recipient, title):
        ...

class SendingEmail(Notifier):

    def sending_message(self, recipient, title):
        # code...
        print(f"Email has been sent to <{recipient}> with title <{title}>")

class SendingSMS(Notifier):

    def sending_message(self, recipient, title):
        print(f"SMS has been sent to <{recipient}> with title <{title}>")

class Notification:
    def __init__(self, notifier):
        self.notifier = notifier

    def get_notification(self, recipient, message):
        self.notifier.sending_message(recipient, message)

mail = Notification(SendingEmail())
mail.get_notification("example@mail.com", "Payment Update")

sms = Notification(SendingSMS())
sms.get_notification("099123456", "Happy Birthday")


