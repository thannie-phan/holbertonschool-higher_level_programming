#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for index, num in enumerate(my_list):
        if num % 2 == 0:
            my_list[index] = True
        else:
            my_list[index] = False
    return my_list
# End of function
