#!/usr/bin/env python3
"""Module for appending to files."""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters
       added.

    Args:
        filename: The path to the text file to append to. Defaults to empty
        string.
        text: The string content to append. Defaults to empty string.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
