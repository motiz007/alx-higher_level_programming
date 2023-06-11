#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 and idx > length:
        return None
    count = 0
    for item in my_list:
        if count == idx:
            return item
        count += 1
