#!/usr/bin/python3

import hidden_4

def print_names():
    names = dir(hidden_4)  # Retrieve all names in the module
    filtered_names = [name for name in names if not name.startswith('__')]
    for name in sorted(filtered_names):
        print(name)

if __name__ == "__main__":
    print_names()
