#!/usr/bin/env python3
"""Module for writing to files."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename: The path to the text file to write to. Defaults to empty string.
        text: The string content to write. Defaults to empty string.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
