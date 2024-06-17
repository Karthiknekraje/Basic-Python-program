class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Create a list of shapes
shapes = [Rectangle(10, 20), Circle(15)]

# Calculate and print the area of each shape
for shape in shapes:
    print(f"The area of the shape is: {shape.area()}")
