#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        return tuple_b
    if tuple_b == ():
        return tuple_a
    if tuple_a == () and tuple_b == ():
        return None
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_total = []
    len_a = len(list_a)
    len_b = len(list_b)
    idx = 0
    if len_a < 2:
        list_a.append(0)
    if len_b < 2:
        list_b.append(0)
    list_total.append(list_a[0] + list_b[0])
    list_total.append(list_a[1] + list_b[1])
    return tuple(list_total)
