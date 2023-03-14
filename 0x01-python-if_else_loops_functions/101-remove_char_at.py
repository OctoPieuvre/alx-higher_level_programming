#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str = str[:n] + str[n+1:]
    else:
        str = str[:n-1] + str[n+1:]
    return str
