#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_number = my_list[0]
    for num in my_list:
        if num > max_number:
            max_number = num
    return max_number
# End of function
