#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for element in range(len(my_list)):
        if new_list[element] == search:
            new_list[element] = replace
    return new_list

# End of function
