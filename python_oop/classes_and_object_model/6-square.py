#!/usr/bin/env python3
"""Module that defines a Square class with size validation."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

    def __str__(self):
        """Return string representation identical to my_print()."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip()
