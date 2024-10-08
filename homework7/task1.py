# # Description: Create a class Person that uses __slots__ to restrict attributes to name, age, and email. Implement a method to display the details of the person.
# # Define the class with __slots__.
# # Create an instance and assign values to the attributes.
# # Attempt to assign an attribute that is not defined in __slots__ and note the result.

class Person:
    __slots__ = ("name", "age", "email")

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}, email: {self.email}'

p1 = Person("Bob", "23", "bob@gmail.com")
print(p1)

try:
    p1.city = "New York"
except AttributeError as e:
    print(f"ERROR: {e}")



