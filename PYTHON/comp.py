class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare_area(self, other_rectangle):
        if self.area() > other_rectangle.area():
            return "The first rectangle has a larger area."
        elif self.area() < other_rectangle.area():
            return "The second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."

# Example usage:
print("First rectangle:")
length = int(input("length:"))
breadth = int(input("breadth:"))
rectangle1 = Rectangle(length, breadth)

print("Second rectangle:")
length = int(input("length:"))
breadth = int(input("breadth:"))
rectangle2 = Rectangle(length, breadth)

print("Area of Rectangle 1:", rectangle1.area())
print("Perimeter of Rectangle 1:", rectangle1.perimeter())

print("Area of Rectangle 2:", rectangle2.area())
print("Perimeter of Rectangle 2:", rectangle2.perimeter())

comparison_result = rectangle1.compare_area(rectangle2)
print(comparison_result)

