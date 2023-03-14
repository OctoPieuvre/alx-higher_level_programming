#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return tup1 = (length, None)
    else:
        first = sentence[0]
        tup = (length, first)
        return tup
