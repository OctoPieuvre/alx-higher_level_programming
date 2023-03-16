#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    res = 0
    for i in sys.argv:
        i = int(i)
        res = res + i

    print('{:d}'.format(res))
