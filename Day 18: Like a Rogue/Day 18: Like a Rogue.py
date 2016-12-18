#!/usr/local/bin/python3
import numpy

class TrappedFloor():
    def __init__(self, first_row, total_rows):
        self.__first_row = first_row
        self.__total_columns = len(self.__first_row) + 2
        self.__total_rows = total_rows
        self.__floor = numpy.zeros((self.__total_rows, self.__total_columns), dtype=bool)
        self.__load_first_row()
        self.__generate_rows()

    def show(self):
        for i in range(self.__total_rows):
            line = []
            for j in range(1, self.__total_columns-1):
                if self.__floor[i,j]:
                    line.append("^")
                else:
                    line.append(".")
            print(''.join(line))


    def __load_first_row(self):
        for j in range(len(self.__first_row)):
            if self.__first_row[j] == "^":
                self.__floor[0, j+1] = True

    def __generate_rows(self):
        for i in range(1,self.__total_rows):
            for j in range(1, self.__total_columns - 1):
                # Its left and center tiles are traps, but its right tile is not.
                if self.__floor[i - 1][j - 1] and self.__floor[i - 1][j] and not self.__floor[i - 1][j+1]:
                    self.__floor[i, j] = True
                # Its center and right tiles are traps, but its left tile is not.
                if not self.__floor[i - 1][j - 1] and self.__floor[i - 1][j] and self.__floor[i - 1][j+1]:
                    self.__floor[i, j] = True
                # Only its left tile is a trap.
                if self.__floor[i - 1][j - 1] and not self.__floor[i - 1][j] and not self.__floor[i - 1][j+1]:
                    self.__floor[i, j] = True
                # Only its right tile is a trap.
                if not self.__floor[i - 1][j - 1] and not self.__floor[i - 1][j] and self.__floor[i - 1][j+1]:
                    self.__floor[i, j] = True

    def count_safe_tiles(self):
        return ((self.__total_columns - 2) * self.__total_rows) - sum(sum(self.__floor))


def star1(vault):
    return tf.count_safe_tiles()

if __name__ == '__main__':
    INPUT_1 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 40]
    tf = TrappedFloor(*INPUT_1)
    print("Star 1: ", star1(tf))
    INPUT_2 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 400000]
    tf = TrappedFloor(*INPUT_2)
    print("Star 2: ", star1(tf))




