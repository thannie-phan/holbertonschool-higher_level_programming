#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if (chr(alphabet)) in ('q', 'e'):
        continue
    print('{}'.format(chr(alphabet)), end='')
