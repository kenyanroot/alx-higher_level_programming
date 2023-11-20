#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list on the same line.
    Args:
    my_list (list): The list to be printed from.
    x (int): The number of elements to print.
    Returns:
    int: The actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # New line after printing list elements
    return count
