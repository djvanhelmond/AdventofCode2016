#!/usr/local/bin/python3
import itertools


def read_input_file(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = read_input_file('./input')


class Scrambler():
    def __init__(self, puzzle_input, instructions):
        self.puzzle_input = puzzle_input
        self.instructions = instructions
        self.__scramble()

    def __scramble(self):
        for instruction in self.instructions:
#            print(instruction)
            if "swap position" in instruction:
                self.__swap_pos_X_Y(int(instruction.split()[2]),int(instruction.split()[5]))
            elif "swap letter" in instruction:
                self.__swap_char_X_Y(instruction.split()[2],instruction.split()[5])
            elif "rotate based on position" in instruction:
                self.__rotate_pos_char(instruction.split()[6])
            elif "rotate" in instruction:
                self.__rotate_steps(instruction.split()[1],int(instruction.split()[2]))
            elif "reverse positions" in instruction:
                self.__reverse_pos_X_Y(int(instruction.split()[2]),int(instruction.split()[4]))
            elif "move position" in instruction:
                self.__move_pos_X_Y(int(instruction.split()[2]),int(instruction.split()[5]))
#            print(self.puzzle_input)
#            print("===")


    def __swap_pos_X_Y(self, X, Y):
        scr = list(self.puzzle_input)
        scr[X] = self.puzzle_input[Y]
        scr[Y] = self.puzzle_input[X]
        self.puzzle_input = ''.join(scr)

    def __swap_char_X_Y(self, X, Y):
        self.puzzle_input = self.puzzle_input.replace(X, "#").replace(Y, X).replace("#", Y)

    def __rotate_pos_char(self, X):
        index = self.puzzle_input.index(X)
        if index < 4:
            index = index + 1
        else:
            index = index + 2
        self.__rotate_steps("right", index)

    def __rotate_steps(self, dir, X):
        if dir == "left":
            for i in range(X):
                self.puzzle_input = self.puzzle_input[1:] + self.puzzle_input[0]
        elif dir == "right":
            for i in range(X):
                self.puzzle_input = self.puzzle_input[-1] + self.puzzle_input[:-1]

    def __reverse_pos_X_Y(self, X, Y):
        self.puzzle_input = self.puzzle_input[:X]+''.join(reversed(self.puzzle_input[X:Y+1]))+self.puzzle_input[Y+1:]

    def __move_pos_X_Y(self, X, Y):
        scr = list(self.puzzle_input)
        take = scr.pop(X)
        new_str = []
        for pos in range(len(self.puzzle_input)):
            if pos == Y:
                new_str.append(take)
            else:
                new_str.append(scr.pop(0))
        self.puzzle_input = ''.join(new_str)



def star2():
    all_pw = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g", "h"]))
    for n in all_pw:
        scrambler = Scrambler(''.join(n), INPUT)
        if scrambler.puzzle_input == "fbgdceah":
            return ''.join(n)


if __name__ == '__main__':
    scrambler = Scrambler("abcdefgh", INPUT)
    print("Star 1: ", scrambler.puzzle_input)
    print("Star 2: ", star2())





# bdeac
# abdec



# abdec




