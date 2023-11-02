#!/usr/bin/python3


import hidden_4


def print_names():
    names = dir(hidden_4)  # Retrieve all names in the module
    filt_n = [name for name in names if not name.startswith('__')]
    for name in sorted(filt_n):
        print(name)


if __name__ == "__main__":
    print_names()
