#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    len_a = len(list_a)
    len_b = len(list_b)

    if len_a < 2:
        list_a.append(0)
    if len_b < 2:
        list_b.append(0)

    list_total = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    return tuple(list_total)
