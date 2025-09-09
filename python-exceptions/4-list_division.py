#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for element in range(list_length):
        try:
            value = my_list_1[element] / my_list_2[element]
        except (ZeroDivisionError):
            print("division by 0")
            value = 0
        except (TypeError, ValueError):
            print("wrong type")
            value = 0
        except (IndexError):
            print("out of range")
            value = 0
        finally:
            result.append(value)
    return result
