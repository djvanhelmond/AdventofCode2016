#!/usr/local/bin/python3

class TrappedFloor():
    def __init__(self, first_row, total_rows):
        self.__traps = ["..^", ".^^", "^..", "^^."]
        self.__row = first_row
        self.__safe_tiles = self.__row.count('.')
        self.__total_rows = total_rows
        self.__run()

    def __run(self):
        for _ in (range(1, self.__total_rows)):
            self.__row = ''.join([ "^" if ("." + self.__row + ".")[i-1:i+2] in self.__traps else '.' for i in range(1, len(self.__row) + 1) ])
            self.__safe_tiles += self.__row.count('.')

    def count_safe_tiles(self):
        return self.__safe_tiles


if __name__ == '__main__':
    INPUT_1 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 40]
    tf = TrappedFloor(*INPUT_1)
    print("Star 1: ", tf.count_safe_tiles())
    INPUT_2 = ["......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 400000]
    tf = TrappedFloor(*INPUT_2)
    print("Star 2: ", tf.count_safe_tiles())




