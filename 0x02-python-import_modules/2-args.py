#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print ('{:d} arguments.'.format(count))
    elif count == 1:
        print ('{:d} argument:'.format(count))
    else:
        print ('{:d} arguments:'.format(count))

    for i in range(count):
        print('{:d}: {}'.format(count + 1, sys.argv[i + 1])
