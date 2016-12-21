#!/usr/local/bin/python3
import math

def ElephantGame_Math(number_of_elves):
    hpot = 0    # find the hpot that fits in the number_of_elves (hpot = highest power of two)
    while math.pow(2,hpot+1) <= number_of_elves:
        hpot += 1
    return 2 * (number_of_elves - int(math.pow(2,hpot))) + 1


def ElephantGame_Math_Circle(number_of_elves):
    hpot = 0    # find the hpot that fits in the number_of_elves (hpot = highest power of three)
    while math.pow(3,hpot+1) <= number_of_elves:
        hpot += 1
    return number_of_elves - int(math.pow(3,hpot))


if __name__ == '__main__':
    INPUT = 3014387
    print("Star 1: ", ElephantGame_Math(INPUT))
    print("Star 2: ", ElephantGame_Math_Circle(INPUT))

