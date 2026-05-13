#!/usr/bin/env python3
"""Module that defines a Square class with size and position validation."""


class Square:
    """Class that defines a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): A tuple of 2 positive integers. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: A tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character with position offset.

        If size is 0, print an empty line.
        Position is applied using spaces for horizontal offset
        and blank lines for vertical offset.
        """
        print(self.__str__())

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The square drawn with '#' characters, offset by position.
        """
        if self.__size == 0:
            return ""

        lines = []
        lines.extend([""] * self.__position[1])
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
