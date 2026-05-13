#!/usr/bin/env python3
"""Square module with private size attribute, validation, and area method."""


class Square:
    """Defines a square with controlled access to its size attribute."""

    def __init__(self, size=0):
        """Initialize a Square instance."""
        self.__size = 0
        self.size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
