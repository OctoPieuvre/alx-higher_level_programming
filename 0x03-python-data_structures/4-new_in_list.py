#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_n_list):
        my_new_list = my_list.copy()
        my_new_list[idx] = element
        return my_new_list
    else:
        return my_list
