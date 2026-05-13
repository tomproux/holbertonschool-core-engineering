"""
Shape module using abstract base class and duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def area(self):
        """Return area of shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Compute area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Compute perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Compute area."""
        return self.width * self.height

    def perimeter(self):
        """Compute perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape area and perimeter using duck typing."""
    print(shape.area())
    print(shape.perimeter())


if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)

    shape_info(c)
    shape_info(r)
