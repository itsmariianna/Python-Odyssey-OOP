from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime


# 1. Account (Abstract Base Class)

class Account(ABC):

    def __init__(self, account_number, balance, account_type):

        # Fields

        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        
        # Methods

        @abstractmethod
        def deposit(self, amount: float) -> None:
            """Deposit money to the account"""
            ...
        
        @abstractmethod
        def withdraw(self, amount: float) -> None:
            """Withdraw money from the account"""
            ...

        @abstractmethod
        def transfer(self, destination: 'Account', amount: float) -> None:
            """Transfer money to another account"""
            ...

        @abstractmethod
        def show_balance(self) -> None:
            """Show balance of the account"""
            ...

        @abstractmethod
        def get_account_type(self) -> str:
            """Show the type of the account"""
            ...
        
#1.5. TransactionManager (Interface)

class TransactionManager(ABC):

    #Methods

    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        """Logging a transaction"""
        ...

    @abstractmethod
    def show_transaction_history(self) -> None:
        """Showing a transaction history"""
        ...



# 1.2. CheckingAccount (Derived from Account)

class CheckingAccount(Account,TransactionManager):

    # Fields

    def __init__(self, account_number, balance, overdraft_limit: float ):
        super().__init__(account_number, balance, "Checking")
        self.overdraft_limit = overdraft_limit

    # Methods

    def log_transaction(self, transaction_type: str, amount: float) -> None:
        return f'Transaction Logged for Checking Account: Success\nTransaction type : {transaction_type}\nAmount : {amount}'

    def show_transaction_history(self) -> None:
        return f'Transaction history for Checking account {self.account_number}'

    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            raise ValueError("Not enough founds")
    
    def transfer(self, destination: Account , amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)

    def show_balance(self) -> None:
        return f'Checking account balance: ${self.balance}'
    
    def get_account_type(self) -> str:
        return 'Account type : Checking'




    
# 1.3. SavingsAccount (Derived from Account)
    
class SavingsAccount(Account,TransactionManager):

    # Fields

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance, 'Savings')
        self.interest_rate = interest_rate

    # Methods
    
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        return f'Transaction Logged for Savings Account : Success\nTransaction type : {transaction_type}\nAmount : {amount}'

    def show_transaction_history(self) -> None:
        return f'Transaction history for Savings account {self.account_number}'

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Not enough founds")

    def transfer(self, destination: Account , amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)

    def show_balance(self) -> None:
        return f'Savings account balance: ${self.balance}'
    
    def get_account_type(self) -> str:
        return 'Account type : Savings'



# 1.4. JointAccount (Derived from Account)

class JointAccount(Account,TransactionManager):

    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self.joint_owners = joint_owners
    
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        return f'Transaction Logged for Joint Account : Success\nTransaction type : {transaction_type}\nAmount : {amount}'

    def show_transaction_history(self) -> None:
        return f'Transaction history for Joint account {self.account_number}'

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Not enough founds")

    def transfer(self, destination: Account , amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        
    def show_balance(self) -> None:
        return f'Joint account balance: ${self.balance}'
    
    def get_account_type(self) -> str:
        return 'Account type : Joint'
    
    def add_owner(self, customer_name: str) -> None:
        self.joint_owners.append(customer_name)



# 1.6. Transaction (Concrete Class)
class Transaction:
    def __init__(self, from_account: 'Account', to_account: Optional['Account'], amount: float, transaction_type: str, timestamp: datetime):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def log(self) -> None:
        return f"{self.timestamp}: {self.transaction_type} of ${self.amount} from Account {self.from_account.account_number}\n{'to Account ' + str(self.to_account.account_number) if self.to_account else ''}."


# 1.7. Customer
class Customer:

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts = []

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)

    def view_accounts(self) -> None:
        for account in self.accounts:
            return f"Account Number: {account.account_number}\nType: {account.get_account_type()}\nBalance: ${account.balance}"

    def view_transaction_history(self) -> None:
        return f'Cannot show transaction history'

if  __name__=='__main__':

    checkingAcc = CheckingAccount(1234,10000,50000)
    savingsAcc = SavingsAccount(5678,20000,50000)
    jointAcc = JointAccount(2445,30000,50000)
    transaction = Transaction(checkingAcc,jointAcc,40000,'Transfer','09/12/2024')




    print(transaction.log())
    print(checkingAcc.show_transaction_history())
    print(savingsAcc.account_type)
    print(jointAcc.balance)




