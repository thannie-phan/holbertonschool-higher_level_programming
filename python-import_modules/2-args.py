#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print('0 arguments.')
    elif argc == 1:
        print(f'{argc} argument:')
    else:
        print(f'{argc} arguments:')

    for num_args, arg in enumerate(argv, start=1):
        print(f'{num_args}: {arg}')
