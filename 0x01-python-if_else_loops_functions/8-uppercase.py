#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # Check if char is lowercase
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)


if __name__ == '__main__':
    uppercase("Best School 98 Battery street")
