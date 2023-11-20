#!/usr/bin/python3


def safe_print_integer(value):
    """
    Print an integer value followed by a new line.

    Args:
    value: The value to be printed, can be of any type.

    Returns:
    bool: True if value is an integer and has been correctly printed,
          otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
