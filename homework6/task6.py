# Task 6: Create a class Employee that manages the salary attribute with a custom descriptor. Ensure that the __get__ and __set__ methods validate the salary (e.g., it must be positive and not exceed a predefined maximum).

class ManagingSalary:
    minimum = 150

    @classmethod
    def validate(cls, arg):
        if arg < 0 or arg < cls.minimum:
            raise ValueError("Salary should be positive integer and above $150")
        
    def __get__(self, instance, owner):
        return instance.__dict__.get("__salary")
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__["__salary"] = value


class Employee:

    salary = ManagingSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name} : ${self.salary}"
    
person = Employee("Sam", 175)
print(person)

person.salary = 200
print(person)

try:
    person.salary = 120
    print(person)
except ValueError as e:
    print(e)