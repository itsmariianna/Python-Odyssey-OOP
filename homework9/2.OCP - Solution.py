from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculating_area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculating_area(self):
        area = self.radius * self.radius * 3.14
        return area
    
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calculating_area(self):
        area = self.a * self.b
        return area
    
class Square(Shape):
    def __init__(self, a):
        self.a = a

    def calculating_area(self):
        area = self.a * self.a
        return area

circle = Circle(5)
square = Square(8)
rectangle = Rectangle(4, 5)

print(circle.calculating_area())
print(square.calculating_area())
print(rectangle.calculating_area())
