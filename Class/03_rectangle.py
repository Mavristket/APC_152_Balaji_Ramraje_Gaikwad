class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
rectangle = Rectangle(length, breadth)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
