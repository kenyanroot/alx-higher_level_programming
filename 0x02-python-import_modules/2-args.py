#!/usr/bin/python3

import sys

def main():
    num_args = len(sys.argv) - 1  # Subtract 1 for the script name itself
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):  # Skip the script name
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
