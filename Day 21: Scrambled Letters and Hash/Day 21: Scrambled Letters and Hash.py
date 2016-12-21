#!/usr/local/bin/python3

def read_input_file(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = read_input_file('./input_test')


class Scrambler():
    def __init__(self, puzzle_input, instructions):
        self.puzzle_input = puzzle_input
        self.instructions = instructions
        self.__scramble()

    def __scramble(self):
        for instruction in self.instructions:
            print(instruction)
            if "swap position" in instruction:
                self.__swap_pos_X_Y(int(instruction.split()[2]),int(instruction.split()[5]))
            elif "swap letter" in instruction:
                self.__swap_char_X_Y(instruction.split()[2],instruction.split()[5])
            elif "rotate based on position" in instruction:
                self.__rotate_pos_char(instruction.split()[6])
            elif "rotate" in instruction:
                self.__rotate_steps(instruction.split()[1],instruction.split()[2])
            elif "reverse positions" in instruction:
                self.__reverse_pos_X_Y(int(instruction.split()[2]),int(instruction.split()[4]))
            elif "move position" in instruction:
                self.__move_pos_X_Y(instruction.split()[2],instruction.split()[5])
            print(self.puzzle_input)
            print("===")


    def __swap_pos_X_Y(self, X, Y):
        scr = list(self.puzzle_input)
        scr[X] = self.puzzle_input[Y]
        scr[Y] = self.puzzle_input[X]
        self.puzzle_input = ''.join(scr)

    def __swap_char_X_Y(self, X, Y):
        self.puzzle_input = self.puzzle_input.replace(X, "#").replace(Y, X).replace("#", Y)

    def __rotate_pos_char(self, X):
        print("rot_pos", X)
        return False

    def __rotate_steps(self, dir, X):
        print("rot_step", dir, X)
        return False

    def __reverse_pos_X_Y(self, X, Y):
        self.puzzle_input = self.puzzle_input[:X]+''.join(reversed(self.puzzle_input[X:Y+1]))+self.puzzle_input[Y+1:]

    def __move_pos_X_Y(self, X, Y):
        print("move_pos", X, Y)
        return False


if __name__ == '__main__':
    scrambler = Scrambler("abcde", INPUT)
#    print("Star 1: ", scrambler.lowest_free())
#    print("Star 2: ", scrambler.total_address())









