#!/usr/bin/python3
from sys import argv

if __name__ == "__name__":
    s = 0
    for i in range(len(argv)):
        if i > 0:
            s += int(argv[i])
    print('{}'.format(s))