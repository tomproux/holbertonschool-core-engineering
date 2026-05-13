"""
Module defining Shape hierarchy with duck typing demonstration.

Implements an abstract Shape class and concrete Circle and Rectangle classes.
Also provides a shape_info function that uses duck typing to display
area and perimeter of shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete implementation of a circle shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Compute the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Compute the circumference of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete implementation of a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Compute the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.

    Args:
        shape: An object that implements area() and perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shape_info(circle)
    shape_info(rectangle)
