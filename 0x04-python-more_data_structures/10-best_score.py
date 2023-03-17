#!/usr/bin/python3
def best_score(a_dictionary):
    """
    a function that return a biggest integer value
    """

    if len(a_dictionary.keys()) == 0:
        return (None)
    else:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
