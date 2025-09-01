#!/usr/bin/python3
def fizzbuzz():
    for number in range (1, 101):
        str1 = 'Fizz'
        str2 = 'Buzz'
        str3 = 'FizzBuzz'
        if number % 3 == 0:
            print(str1, end=' ')
        elif number % 5 == 0:
            print(str2, end=' ')
        elif number % 5 == 0 and number % 3 == 0:
            print(str3, end=' ')
        else:
            print(number, end=' ')
