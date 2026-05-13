#!/usr/bin/env python3
class Square:
    """Square class with size validation."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
