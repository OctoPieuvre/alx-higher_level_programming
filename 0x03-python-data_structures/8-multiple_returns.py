#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tup1 = (length, None)
        return tup1
    else:
        first = sentence[0:1]
        tup = (length, first)
        return tup
