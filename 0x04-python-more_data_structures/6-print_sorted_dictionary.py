#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    cles = list(a_dictionary.keys())
    cles.sort()
    for i in cles:
        print('{}: {}'.format(i, my_dict[i]))
