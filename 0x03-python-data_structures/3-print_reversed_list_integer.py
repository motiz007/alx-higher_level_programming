#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    l_idx = len(my_list) - 1
    while l_idx >= 0:
        print("{:d}".format(my_list[l_idx]))
        l_idx -= 1
