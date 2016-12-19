#!/usr/local/bin/python3
import numpy

class ElephantGame():
    def __init__(self, number_of_elves):
        self.elves = [ i for i in range(1, number_of_elves + 1) ]
        self.__play()

    def __play(self):
        while len(self.elves) != 1:
            if len(self.elves) % 2 == 1:
                del self.elves[1::2]
                del self.elves[0]
            else:
                del self.elves[1::2]


def star1(number):
    game = ElephantGame(number)
    return game.elves[0]

if __name__ == '__main__':
    INPUT = 3014387
    print("Star 1: ", star1(INPUT))




