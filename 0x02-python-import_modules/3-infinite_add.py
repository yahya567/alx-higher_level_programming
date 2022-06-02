#!/usr/bin/python3
from sys import argv

if __name__ == "__name__":
    s = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
                s += int(argv[i])
    print('{}'.format(s))
