#!/usr/bin/python3

import sys

def main():
    total_sum = 0  # Initialize the sum at 0
    for arg in sys.argv[1:]:  # Skip the script name and iterate over arguments
        total_sum += int(arg)  # Add the integer value of the argument to the sum
    print(total_sum)  # Print the sum followed by a newline

if __name__ == "__main__":
    main()  # Call main if the script is run directly
