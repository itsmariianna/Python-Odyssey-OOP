# Task 1: Create a class Person that uses the property decorator to control access to the age attribute. Ensure that the age is a positive integer, and if an invalid value is assigned, raise a ValueError.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError("Age cannot be a negative number")
        self.__age = value

    def __repr__(self):
        return f'Name : {self.name}\nAge: {self.age}'
    

person1 = Person("Sam", 14)
print(person1.age)
person1.age = 19
print(person1.age)

try:
    person1.age = -20
except ValueError as e:
    print(f'ERROR : {e}')
