#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        maxV = my_list[0]
        for item in my_list:
            if item > maxV:
                maxV = item
        return maxV
