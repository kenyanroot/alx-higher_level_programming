#!/usr/bin/python3

def print_custom_alphabet():
    for i in range(97, 123):  # ASCII values for 'a' to 'z' are 97 to 122 inclusive
        if chr(i) != 'q' and chr(i) != 'e':
            print(chr(i), end="")

if __name__ == '__main__':
    print_custom_alphabet()
