#!/usr/bin/python3
from re import I


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
    except IndexError:
        print()
        return i
    print()
    return x
