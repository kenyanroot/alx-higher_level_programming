#!/usr/bin/python3

def print_decimal_hexadecimal():
    for i in range(99):  # Iterate from 0 to 98
        print("{} = {}".format(i, hex(i)))

if __name__ == '__main__':
    print_decimal_hexadecimal()
