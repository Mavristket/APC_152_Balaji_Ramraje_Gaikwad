import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter radius: "))
circle = Circle(radius)

print("Area:", round(circle.area(), 2))
print("Circumference:", round(circle.circumference(), 2))
