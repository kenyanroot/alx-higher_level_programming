#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(a), int(b)
    result = ops[operator](a, b)
    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
