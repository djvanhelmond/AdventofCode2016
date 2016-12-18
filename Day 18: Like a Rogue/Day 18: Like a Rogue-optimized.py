#!/usr/local/bin/python3
import numpy

class TrappedFloor():
    def __init__(self, first_row, total_rows):
        self.__local_traps = ["..^", ".^^", "^..", "^^."]
        self.__row = first_row
        self.__total_rows = total_rows
        self.__safe_tiles = self.__row.count('.')
        self.__run()

    def __run(self):
        for _ in (range(self.__total_rows-1)):
            self.__row = ''.join([ "^" if ("." + self.__row + ".")[i-1:i+2] in self.__local_traps else '.' for i in range(1, len(self.__row) + 1) ])
            self.__safe_tiles = self.__safe_tiles + self.__row.count('.')

    def count_safe_tiles(self):
        return self.__safe_tiles


if __name__ == '__main__':
    INPUT_1 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 40]
    tf = TrappedFloor(*INPUT_1)
    print("Star 1: ", tf.count_safe_tiles())
    INPUT_2 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 400000]
    tf = TrappedFloor(*INPUT_2)
    print("Star 2: ", tf.count_safe_tiles())




