#!/usr/bin/python3
def fizzbuzz():
    """prints Fizz if number is multiple of 3, Buzz if it's a multiple of 5,
    and FizzBuzz if a multiple of both"""
    for a in range(1, 101):
        if a % 15 == 0:
            print("FizzBuzz", end="")
        elif a % 3 == 0:
            print("Fizz", end="")
        elif a % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(a), end="")
        print(end=" ")
