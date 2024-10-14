class SendingEmail:

    def sending_email(self, recipient, title):
        # code...
        print(f"Email has been sent to <{recipient}> with title <{title}>")

class Notification:

    def __init__(self):
        self.message = SendingEmail()

    def get_notification(self, recipient, title):
        self.message.sending_email(recipient, title)

example = Notification()
example.get_notification("mail@example.com", "Security Alert")