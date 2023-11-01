#!/usr/bin/python3
import random


def corrected_last_digit_description(number):
    # Extract the last digit
    last_digit = number % 10 if number >= 0 else (number % -10) * -1
    
    if number < 0:
        last_digit *= -1

    # Create the base output string
    output = f"Last digit of {number} is {last_digit}"

    # Append the necessary condition based on the last digit
    if last_digit > 5:
        output += " and is greater than 5"
    elif last_digit == 0:
        output += " and is 0"
    else:
        output += " and is less than 6 and not 0"

    return output

if __name__ == '__main__':
    number = random.randint(-10000, 10000)
    print(corrected_last_digit_description(number))
