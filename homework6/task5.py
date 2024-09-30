# Task 5: Build a class ValidatedString where you implement a custom descriptor that validates if the string has a minimum length when assigned. Demonstrate this descriptor with a class User where the username attribute uses this descriptor.
class ValidatedString:
    min_len = 8

    @classmethod
    def validation(cls, arg):
        if not isinstance(arg, str):
            raise ValueError("Your username should be a string!")
        elif len(arg) < cls.min_len:
            raise ValueError("Your username should contain minimum 8 symbols!")

    def __get__(self, instance, owner):
        return instance.__dict__.get("__username")
    
    def __set__(self, instance, value):
        self.validation(value)
        instance.__dict__["__username"] = value


class User:
    username = ValidatedString()

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f'Username: {self.username}'
    
person = User('User310717')
print(person)