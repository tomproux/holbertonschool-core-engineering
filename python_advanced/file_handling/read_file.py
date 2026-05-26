#!/usr/bin/env python3
"""Module for reading and printing file contents."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout.

    Args:
        filename: The path to the text file to read. Defaults to empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
