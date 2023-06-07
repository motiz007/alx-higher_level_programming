#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str
    nstr = ""
    counter = 0
    for letter in (str):
        if counter != n:
            nstr += str[counter]
        counter += 1
    return nstr
