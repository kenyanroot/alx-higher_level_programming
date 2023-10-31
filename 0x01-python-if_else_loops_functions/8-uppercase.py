#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if char is lowercase
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

if __name__ == '__main__':
    uppercase("best")
    uppercase("Best School 98 Battery street")
