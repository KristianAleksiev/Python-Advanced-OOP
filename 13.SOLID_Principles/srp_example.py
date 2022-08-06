# SR

def my_sum(numbers):  # Not a single responsibility method, not predictable if circumstances change
    the_sum = sum(numbers)
    if the_sum % 2 == 0:
        print(the_sum / 2)  # Return
    else:
        print(the_sum / 3)  # Return


class Student:
    """Class in violation of SRP ->
    - Student prop management
    - Student database management
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def register(self, student):
        pass


"""Class student should be split in two classes like:"""


class Student1:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRegistration:
    def get_name(self, id):
        pass

    def register(self, student):
        pass


# Example 2
"""
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # SRP Violation - Calculate area for both triangle and rectangle
    def print_triangle_area(self):
        area = self.width * self.height / 2
        print(area)  # SRP Violation - calculation and printing

    def print_rectangle_area(self):
        area = self.width * self.height
        print(area)  # SRP Violation - calculation and printing


triangle = Shape(10, 5)
rect = Shape(10, 5)

triangle.print_triangle_area()
rect.print_rectangle_area()

Correct below:
"""


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def triangle_area(self):
        return self.width * self.height / 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_area(self):
        return self.width * self.height


class Printer:
    def print(self, obj):
        print(obj)


printer = Printer()
triangle = Triangle(10, 5)
rectangle = Rectangle(10, 5)

printer.print(triangle.triangle_area())
printer.print(rectangle.rectangle_area())
