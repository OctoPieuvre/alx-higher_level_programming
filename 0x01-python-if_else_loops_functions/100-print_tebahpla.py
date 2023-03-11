#!/usr/bin/python3
for i in range(122, 95, -1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(i - diff)), end='')
