#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element by element.

    Args:
    my_list_1 (list): First list of elements.
    my_list_2 (list): Second list of elements.
    list_length (int): Number of elements to process.

    Returns:
    list: List containing the results of the division.
    """
    division_result = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            division_result.append(result)
    return division_result
