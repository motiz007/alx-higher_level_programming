#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        my_list = []
    n_list = []
    length = len(my_list)
    if idx < 0 or idx >= length:
        n_list = my_list.copy()
        return n_list
    else:
        n_list = my_list.copy()
        n_list[idx] = element
        return n_list
