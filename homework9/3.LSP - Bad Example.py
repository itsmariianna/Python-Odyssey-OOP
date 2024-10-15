class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area
    
class Square(Rectangle):
    def set_width(self, width):
        self.height = width
        self.width = width
    
    def set_height(self, height):
        self.height = height
        self.width = height


shape = Square(2, 3)
print(shape.calculate_area())
shape.set_height(3)
print(shape.calculate_area())
