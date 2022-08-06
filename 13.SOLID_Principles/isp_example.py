import abc
import math


class ShapeCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class CircleCalculator(ShapeCalculator):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class RectangleCalculator(ShapeCalculator):

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width


"""Few classes with specific methods, not one with all methods inside it"""
