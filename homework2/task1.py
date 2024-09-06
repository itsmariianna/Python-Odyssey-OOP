# Write a Python class named Person that has attributes for name and age. Include a method to display the person’s details.
# Extend the Person class by adding an __init__ constructor method that initializes name and age when an object is created. Ensure the method uses self to assign the values.
# Add a method to the Person class called greet that prints a greeting message including the person’s name.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        return f"Name: {self.name}. Age: {self.age}"
    
    def greet(self):
        return f"Hello, {self.name}!"
    
if __name__ == '__main__':
    user = Person("Bob", 40)
    print(user.func())
    print(user.greet())