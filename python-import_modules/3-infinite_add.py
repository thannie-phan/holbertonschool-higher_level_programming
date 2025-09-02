#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print('0')
    else:
        total = sum(int(arg) for arg in argv)
        print(total)
