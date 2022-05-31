#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            dis = 'Fizz'
            print('{} '.format(dis), end="")
        elif i % 5 == 0 and i % 3 != 0:
            dis = 'Buzz'
            print('{} '.format(dis), end="")
        elif i % 5 == 0 and i % 3 == 0:
            dis = 'FizzBuzz'
            print('{} '.format(dis), end="")
        else:
            dis = i
            print('{} '.format(dis), end="")
