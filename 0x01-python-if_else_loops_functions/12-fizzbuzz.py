#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers from 1 to 100 separated by space.
    Replace numbers by Fizz, Buzz, or FizzBuzz if conditions met.
    """

for number in range (1, 101):
    if number % 15 == 0:
        print("FizzBuzz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    elif number % 3 == 0:
        print("Fizz", end= " ")
    else:
        print("{}".format(number), end=" ")
