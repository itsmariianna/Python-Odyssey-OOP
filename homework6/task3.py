# Task 3: Write a class Temperature that stores temperature in Celsius but allows the user to set and get the temperature in Fahrenheit using the property decorator.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Temperature should be int or float")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (9/5) * self.__celsius + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Temperature should be int or float")
        self.__celsius = (5/9) * (value - 32)


    def __repr__(self) -> str:
        return f'Celsius: {self.__celsius}. Fahrenheit: {(9/5) * self.__celsius + 32}'


temp = Temperature(12)
print(temp.fahrenheit)

temp.celsius = 32
print(temp.fahrenheit)