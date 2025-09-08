#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for index, num in enumerate(my_list):
        if num % 2 == 0:
            new_list[index] = True
        elif num % 2 != 0:
            new_list[index] = False
    return new_list
# End of function
