#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
    except (TypeError):
        print('Only accept integer')
        return False
    except (ValueError):
        print('Only accept integer')
        return False
