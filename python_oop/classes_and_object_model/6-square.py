#!/usr/bin/env python3
"""Square module with size, position, and printable representation."""


class Square:
    """Defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of the square."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i > 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """Print the square using '#' considering position offsets."""
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation identical to my_print()."""
        if self.__size == 0:
            return ""

        output = "\n" * self.__position[1]
        for _ in range(self.__size):
            output += " " * self.__position[0] + "#" * self.__size + "\n"

        return output.rstrip()
