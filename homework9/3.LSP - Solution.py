class Shape:
    def calculate_area(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


rect = Rectangle(2, 3)
print(rect.calculate_area())

square = Square(3)
print(square.calculate_area())