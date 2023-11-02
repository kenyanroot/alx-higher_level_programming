#!/usr/bin/python3

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


if __name__ == "__main__":
    # Test the function with some values
    print(magic_calculation(10, 5))
    print(magic_calculation(5, 10))
