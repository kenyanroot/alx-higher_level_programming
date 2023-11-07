#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    for num, res in zip(my_list, list_result):
        status = "is" if res else "is not"
        print("{:d} {:s} divisible by 2".format(num, status))
