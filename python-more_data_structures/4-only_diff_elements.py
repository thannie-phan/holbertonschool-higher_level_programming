#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    combine_first = set_1.union(set_2)
    common = set_1.intersection(set_2)
    everything = combine_first - common
    return everything

# End of function
