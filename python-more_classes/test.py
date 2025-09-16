#!/usr/bin/python3

numbers = [5, 10, 15, 20]
new = map(str, numbers)
new_list = list(new)

new = [str(item) for item in numbers]

new_list = ','.join(new_list)
print(new_list)