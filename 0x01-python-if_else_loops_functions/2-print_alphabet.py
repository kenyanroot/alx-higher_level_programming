#!/usr/bin/python3

def print_alphabet():
    for i in range(97, 123):  # ASCII values for 'a' to 'z' are 97 to 122 inclusive
        print(chr(i), end="")

if __name__ == '__main__':
    print_alphabet()
