#!/usr/bin/python3

def print_alphabet():
    print("{}".format(''.join([chr(i) for i in range(97, 123)])), end='')


if __name__ == "__main__":
    print_alphabet()
