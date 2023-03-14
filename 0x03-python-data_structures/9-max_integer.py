#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        my_list = sorted(my_list)
        maxi = my_list[length-1]
        return maxi
