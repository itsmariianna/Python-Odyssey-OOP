# I Bad Example
from abc import ABC, abstractmethod

class PaymentMethods(ABC):

    @abstractmethod
    def idram_payment(self):
        ...

    @abstractmethod
    def card_payment(self):
        ...

    @abstractmethod
    def account_number_payment(self):
        ...

class Payment(PaymentMethods):

    def idram_payment(self, sender, reciver, amount):
        #code...
        print(f"YOU MADE PAYMENT SUCCESSFULLY!\nSender: {sender}\nReciver: {reciver}\nAmount: ${amount}")

    def card_payment(self):
        raise NotImplementedError("Card payment is not supported")
    
    def account_number_payment(self):
        raise NotImplementedError("Account number payment is not supported")

pay = Payment()
pay.idram_payment("Bob", "Ann", 50)

try:
    pay.card_payment()
except NotImplementedError as e:
    print(f'ERROR; {e}')

try:
    pay.account_number_payment()
except NotImplementedError as e:
    print(f'ERROR; {e}')
           