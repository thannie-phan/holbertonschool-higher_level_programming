#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = []
    try:
        for row in range (len(matrix)):
    except:
        
    for element in range(len(matrix)):   
        try:
            value = matrix[element] / div
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