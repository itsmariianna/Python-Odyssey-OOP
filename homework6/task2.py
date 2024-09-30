# Task 2: Implement a class Rectangle where the width and height attributes use the property decorator to calculate the area and perimeter dynamically when accessed.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Width cannot be negative number or string")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Height cannot be negative number or string")
        self.__height = value

    def area(self):
        a = self.height * self.width
        return f'Area : {a}'

    def perimeter(self):
        p = 2 * (self.height + self.width)
        return f'Perimeter : {p}'
    

item1 = Rectangle(3, 4)
print(item1.area())

item2 = Rectangle(7, 9)
print(item2.perimeter())


try:
    item3 = Rectangle(8, -10)
    print(item3.area())
except ValueError as e:
    print(f'There is an error: {e}')