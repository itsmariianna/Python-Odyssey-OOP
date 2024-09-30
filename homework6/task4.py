# Task 4: Implement a Descriptor class to manage access to a score attribute in a Student class. Use the __get__ and __set__ methods to ensure the score is within a valid range (e.g., 0-100).

class Descriptor:
    minimum = 0
    maximum = 100

    @classmethod
    def verify(cls, arg):
        if not cls.minimum <= arg <= cls.maximum:
            raise ValueError("Score should be between 0 and 100")

    def __get__(self, instance, owner):
        return instance.__dict__.get('__score', None)
    
    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__['__score'] = value


class Student:
    score = Descriptor()

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'Student : {self.name}\nScore : {self.score}\n'
    
person = Student("Sam", 90)
print(person)

try:
    person.score = -10
    print(person)
except ValueError as e:
    print(e)

try:
    person.score = 120
    print(person)
except ValueError as e:
    print(e)