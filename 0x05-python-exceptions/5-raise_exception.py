#!/usr/bin/python3


def raise_exception():
    """
    Raises a TypeError exception.
    """
    raise TypeError


# Test case
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
