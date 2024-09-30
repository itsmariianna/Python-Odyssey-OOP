# Task 8: Write a class PasswordValidator that uses a descriptor to validate passwords according to a set of rules (e.g., minimum length, contains numbers). Show how this is used in a class Account.

class PasswordValidator:
    min_len = 8

    @classmethod
    def validation(cls, arg):
        if not isinstance(arg, str):
            raise ValueError("Password should be a sring")
        elif len(arg) < cls.min_len:
            raise ValueError("Password should conain at least 8 symbols")
                
    def __get__(self, instance, owner):
        return instance.__dict__.get("__password")
    
    def __set__(self, instance, value):
        self.validation(value)
        instance.__dict__["__password"] = value



class Account:
    password = PasswordValidator()

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return f'{self.user} -> {self.password}'


person = Account("Bob", 'asdf1234')
print(person)

try:
    person2 = Account("Nancy", 12345)
    print(person2)
except ValueError as e:
    print(e)