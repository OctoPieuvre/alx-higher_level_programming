#!/usr/bin/python3
"""Define a class that inherit list"""


class Mylist(list):
    """A subclass of list that provides a method to print the list sorted. """

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
