#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (any): The size of the square.
        """
        self.__size = size
