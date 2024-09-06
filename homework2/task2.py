# Modify the Person class to make the age attribute private. Provide a method to get the age (get_age) and another method to set the age (set_age) with

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def func(self):
        return f"Name: {self.name}. Age: {self.__age}"
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("The age should be a positive integer.")

if __name__ == '__main__':
    user = Person("Bob", 40)
    print(user.func())

    print(f"Current Age: {user.get_age()}")

    user.set_age(65)
    print(f"Updated age: {user.get_age()}")

    user.set_age(-5)