#!/usr/bin/python3
def best_score(a_dictionary):
    """
    a function that return a biggest integer value
    """

    if not a_dictionary:
        return None
    else:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
