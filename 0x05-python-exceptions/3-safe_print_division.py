#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list that are integers.

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
        except (ValueError, TypeError, IndexError):
            continue
    print()  # New line after printing integers
    return count


# Test cases
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

# Replacing len(my_list) with the actual number of elements
my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, 7)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 9)
print("nb_print: {:d}".format(nb_print))
