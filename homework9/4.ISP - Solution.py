from abc import ABC, abstractmethod

class IdramPaymentMethod(ABC):

    @abstractmethod
    def idram_payment(self):
        ...

class CardPaymentMethod(ABC):

    @abstractmethod
    def card_payment(self):
        ...

class AccountNumberPaymentMethod(ABC):

    @abstractmethod
    def account_number_payment(self):
        ...


class IdramPayment(IdramPaymentMethod):
    def idram_payment(self, sender, reciver, amount):
        #code...
        print(f"\nIDRAM - PAYMENT SUCCESSFULLY!\nSender: {sender}\nReciver: {reciver}\nAmount: ${amount}")

class CardPayment(CardPaymentMethod):
    def card_payment(self, sender, reciver, amount):
        #code...
        print(f"\nCARD PAYMENT - SUCCESSFULLY!\nSender: {sender}\nReciver: {reciver}\nAmount: ${amount}")

class AccountNumberPayment(AccountNumberPaymentMethod):
    def account_number_payment(self, sender, reciver, amount):
        #code...
        print(f"\nACCOUNT NUMBER PAYMENT - SUCCESSFULLY!\nSender: {sender}\nReciver: {reciver}\nAmount: ${amount}")

pay1 = IdramPayment()
pay1.idram_payment("Bob", "Ann", 50)

pay2 = CardPayment()
pay2.card_payment("Lisa", "James", 15)

pay3 = AccountNumberPayment()
pay3.account_number_payment("Kevin", "Sam", 30)
        
