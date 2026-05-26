#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization of Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python Dictionary with data to serialize
        filename: The filename of the output JSON file.
                 If the file already exists, it will be replaced.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file back into a Python dictionary.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r') as f:
        return json.load(f)
