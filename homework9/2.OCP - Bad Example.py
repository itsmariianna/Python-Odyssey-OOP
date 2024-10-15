class Shape:
    def __init__(self, shapetype, radius = 0, a = 0, b = 0):
        self.shapetype = shapetype
        self.radius = radius
        self.a = a
        self.b = b
    
    def calculating_area(self):
        if self.shapetype == "circle":
            area = 3.14 * self.radius * self.radius
            return area
        elif self.shapetype == "square":
            area = self.a * self.a
            return area
        elif self.shapetype == "rectangle":
            area = self.a * self.b
            return area


circle = Shape("circle", radius = 6)
square = Shape("square", a = 5)
rectangle = Shape("rectangle", a = 4, b = 8)

print(circle.calculating_area())
print(square.calculating_area())
print(rectangle.calculating_area())

