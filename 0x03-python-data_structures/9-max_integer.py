#!/urs/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maxV = 0
        for item in my_list:
            if item > maxV:
                maxV = item
        return maxV
