#!/usr/bin/python3

def print_alphabt():
    print("{}".format(''.join([chr(i) for i in range(97, 123) 
                               if i != 101 and i != 113])), end='')


if __name__ == "__main__":
    print_alphabt()
