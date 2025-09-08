#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary)
    for keys in sorted_key:
        print('{}: {}'.format(keys, a_dictionary[keys]))

# End of function
