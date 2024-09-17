from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

# 1. Account (Abstract Base Class)

class Account(ABC):

    def __init__(self, account_number, balance, account_type):
        self.set_account_number(account_number)
        self.set_balance(balance)
        self.set_account_type(account_type)


    # Setters

    def set_account_number(self, account_number):
        if not isinstance(account_number, str) or len(account_number) == 0:
            raise ValueError("Account number should be non empty string")
        else:
            self.__account_number = account_number

        
    def set_balance(self, balance):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance can't be negative")
        else:
            self.__balance = balance


    def set_account_type(self, account_type):
        if account_type not in ("Checking", "Savings", "Joint"):
            raise ValueError("Account type should be 'Checking', 'Savings' or 'Joint'")
        else:
            self.__account_type = account_type


    # Getters

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def get_account_type(self):
        return self.__account_type

        
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

    def __init__(self, account_number, balance, overdraft_limit: float ):
        super().__init__(account_number, balance, "Checking")
        self.set_overdraft_limit(overdraft_limit)
        self.transaction_history = []


    # Setter and Getter for overdraft_limit

    def set_overdraft_limit(self, overdraft_limit: float) -> None:
        if not isinstance(overdraft_limit, (int, float)) or overdraft_limit < 0:
            raise ValueError("Overdraft limit must be a non-negative number")
        else:
            self.__overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.__overdraft_limit


    # Methods for transaction (CheckingAccount)

    def log_transaction(self, transaction_type: str, amount: float) -> None:
        transaction_log = f'Transaction Logged for Checking Account: Success\nTransaction type : {transaction_type}\nAmount : {amount}'
        self.transaction_history.append(transaction_log)
        return transaction_log

    def show_transaction_history(self) -> None:
        if len(self.transaction_history) == 0:
            return f'Transaction history for Checking account {self.account_number} is empty'
        else:
            return '\n'.join(self.transaction_history)
        

    # Methods for CheckingAccount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("You should enter poitive deposit")
        self.set_balance(self.get_balance() + amount)
        self.log_transaction('Deposit', amount)
    

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount should be positive")
        if self.get_balance() + self.get_overdraft_limit() >= amount:
            self.set_balance(self.get_balance() - amount)
            self.log_transaction('Withdrawal', amount)
        else:
            raise ValueError("Not enough funds")
        
    
    def transfer(self, destination: Account , amount: float) -> None:
        if not isinstance(destination, Account):
            raise ValueError("Destination must be an Account instance")
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction('Transfer', amount)


    def show_balance(self) -> None:
        return f'Checking account balance: ${self.balance}'
    
    
    def get_account_type(self) -> str:
        return 'Account type : Checking'




    
# 1.3. SavingsAccount (Derived from Account)
    
class SavingsAccount(Account,TransactionManager):

    # Fields

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance, 'Savings')
        self.set_interest_rate(interest_rate)
        self.transaction_history = []


    # Setter and getter for interest_rate

    def set_interest_rate(self, interest_rate: float) -> None:
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Interest rate must be a non-negative number")
        else:
            self.__interest_rate = interest_rate

    def get_interest_rate(self) -> float:
        return self.__interest_rate


    # Methods for transaction (SavingsAccount)
    
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        transaction_log = f'Transaction Logged for Savings Account: Success\nTransaction type: {transaction_type}\nAmount: {amount}'
        self.transaction_history.append(transaction_log)
        print(transaction_log)

    def show_transaction_history(self) -> None:
        if not self.transaction_history:
            return f'Transaction history for Savings account {self.get_account_number()} is empty'
        return '\n'.join(self.transaction_history)
    
    
    # Methods for SavingsAccount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.set_balance(self.get_balance() + amount)
        self.log_transaction('Deposit', amount)


    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.get_balance() >= amount:
            self.set_balance(self.get_balance() - amount)
            self.log_transaction('Withdrawal', amount)
        else:
            raise ValueError("Not enough funds")


    def transfer(self, destination: Account , amount: float) -> None:
        if not isinstance(destination, Account):
            raise ValueError("Destination must be an Account instance")
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction('Transfer', amount)


    def show_balance(self) -> None:
        return f'Savings account balance: ${self.balance}'
    
    def get_account_type(self) -> str:
        return 'Account type : Savings'





# 1.4. JointAccount (Derived from Account)

class JointAccount(Account,TransactionManager):

    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self.set_joint_owners(joint_owners)
        self.transaction_history = []


    # Setter and getter for joint_owners

    def set_joint_owners(self, joint_owners: List[str]) -> None:
        if not all(isinstance(owner, str) and len(owner) > 0 for owner in joint_owners):
            raise ValueError("All joint owners should be non-empty strings")
        else:
            self.__joint_owners = joint_owners

    def get_joint_owners(self) -> List[str]:
        return self.__joint_owners


    # Transactions for Joint Account
    
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        transaction_log = f'Transaction Logged for Joint Account: Success\nTransaction type: {transaction_type}\nAmount: {amount}'
        self.transaction_history.append(transaction_log)
        print(transaction_log) 

    def show_transaction_history(self) -> None:
        if not self.transaction_history:
            return f'Transaction history for Joint account {self.get_account_number()} is empty'
        return '\n'.join(self.transaction_history)    
    
    
    # Methods for Joint Account

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.set_balance(self.get_balance() + amount)
        self.log_transaction('Deposit', amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.get_balance() >= amount:
            self.set_balance(self.get_balance() - amount)
            self.log_transaction('Withdrawal', amount)
        else:
            raise ValueError("Not enough funds")

    def transfer(self, destination: Account, amount: float) -> None:
        if not isinstance(destination, Account):
            raise ValueError("Destination must be an Account instance")
        self.withdraw(amount)
        destination.deposit(amount)
        self.log_transaction('Transfer', amount)
    
    def get_account_type(self) -> str:
        return 'Account type : Joint'
    
    def add_owner(self, customer_name: str) -> None:
        self.joint_owners.append(customer_name)



# 1.6. Transaction (Concrete Class)

class Transaction:
    def __init__(self, from_account: 'Account', to_account: Optional['Account'], amount: float, transaction_type: str):
        self.set_from_account(from_account)
        self.set_to_account(to_account)
        self.set_amount(amount)
        self.set_transaction_type(transaction_type)
        self.set_timestamp(datetime.now())


    # Setters

    def set_from_account(self, from_account: 'Account') -> None:
        if not isinstance(from_account, Account):
            raise ValueError("From account must be an instance of Account")
        self.__from_account = from_account


    def set_to_account(self, to_account: Optional['Account']) -> None:
        if to_account is not None and not isinstance(to_account, Account):
            raise ValueError("To account must be an instance of Account or None")
        self.__to_account = to_account


    def set_amount(self, amount: float) -> None:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number")
        self.__amount = amount

    def set_transaction_type(self, transaction_type: str) -> None:
        if transaction_type not in ['Deposit', 'Withdrawal', 'Transfer']:
            raise ValueError("Transaction type must be 'Deposit', 'Withdrawal', or 'Transfer'")
        self.__transaction_type = transaction_type


    def set_timestamp(self, timestamp: datetime) -> None:
        if not isinstance(timestamp, datetime):
            raise ValueError("Timestamp must be a datetime object")
        self.__timestamp = timestamp

    #  Getters

    def get_from_account(self) -> 'Account':
        return self.__from_account

    def get_to_account(self) -> Optional['Account']:
        return self.__to_account

    def get_amount(self) -> float:
        return self.__amount

    def get_transaction_type(self) -> str:
        return self.__transaction_type

    def get_timestamp(self) -> datetime:
        return self.__timestamp


    # Methods for Transaction

    def log(self) -> str:
        to_account_info = f" to Account {self.__to_account.get_account_number()}" if self.__to_account else ""
        return f"{self.__timestamp}: {self.__transaction_type} of ${self.__amount} from Account {self.__from_account.get_account_number()}{to_account_info}."


# 1.7. Customer

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.set_name(name)
        self.set_contact_info(contact_info)
        self.__accounts: List[Account] = []

    # Setters

    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.__name = name

    def set_contact_info(self, contact_info: str) -> None:
        if not isinstance(contact_info, str) or len(contact_info) == 0:
            raise ValueError("Contact info must be a non-empty string")
        self.__contact_info = contact_info
    
    # Getters

    def get_name(self) -> str:
        return self.__name

    def get_contact_info(self) -> str:
        return self.__contact_info

    # Methods

    def add_account(self, account: Account) -> None:
        if not isinstance(account, Account):
            raise ValueError("Account must be an instance of Account")
        self.__accounts.append(account)

    def view_accounts(self) -> str:
        if not self.__accounts:
            return "No accounts available."
        account_info = []
        for account in self.__accounts:
            account_info.append(f"Account Number: {account.get_account_number()}\nType: {account.get_account_type()}\nBalance: ${account.get_balance()}")
        return "\n\n".join(account_info)

    def view_transaction_history(self) -> str:
        history = []
        for account in self.__accounts:
            history.append(f"Transaction history for Account {account.get_account_number()}:\n{account.show_transaction_history()}")
        return "\n\n".join(history) if history else "No transaction history available."



    
 



