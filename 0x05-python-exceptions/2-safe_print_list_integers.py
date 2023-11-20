#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
    my_list (list): The list to be printed from, can contain any type.
    x (int): The number of elements to access in my_list.

    Returns:
    int: The actual number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError, IndexError):
            continue
    print()  # New line after printing integers
    return count
