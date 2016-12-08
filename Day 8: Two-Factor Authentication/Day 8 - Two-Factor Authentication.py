#!/usr/local/bin/python3
import numpy

def read_input_moves(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = (read_input_moves('./input'))


OCR = {
    "011001001010010111101001010010": "A",
    "111101000011100100001000011110": "E",
    "011001001010000101101001001110": "G",
    "100101001011110100101001010010": "H",
    "011001001010010100101001001100": "O",
    "111001001010010111001000010000": "P",
    "111001001010010111001010010010": "R",
    "100011000101010001000010000100": "Y"
}


class Instruct:
    def __init__(self, instruction):
        self.instruction = instruction.split()
        self.action = self.instruction[0]
        if self.instruction[0] == "rect":
            self.register = int(self.instruction[1].split("x")[0])
            self.shift = int(self.instruction[1].split("x")[1])
        else:
            self.action = self.instruction[1]
            self.register = int(self.instruction[2][2:])
            self.shift = int(self.instruction[4])


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = numpy.zeros((self.height, self.width), dtype=bool)

    def show_char(self, char):
        return ''.join(["1" if self.pixels[i, j] else "0"
                        for i in range(0, self.height) for j in range(char * 5, char * 5 + 5)])

    def countpixel(self):
        return sum([self.pixels[i, j] for i in range(0, self.height) for j in range(0, self.width)])

    def rect(self, width, height):
        self.pixels[:height, :width] = True

    def rotx(self, column, shift):
        self.pixels[:, column] = numpy.roll(self.pixels[:, column], shift)

    def roty(self, row, shift):
        self.pixels[row] = numpy.roll(self.pixels[row], shift)

    def execute(self, instruction):
        if instruction.action == "rect":
            self.rect(instruction.register, instruction.shift)
        if instruction.action == "column":
            self.rotx(instruction.register, instruction.shift)
        if instruction.action == "row":
            self.roty(instruction.register, instruction.shift)


def star1(instruction_list, width, height):
    small_screen = Screen(width, height)
    instructions = [Instruct(instruction) for instruction in instruction_list]
    for step in instructions:
        small_screen.execute(step)
    return small_screen.countpixel()


def star2(instruction_list, width, height):
    code = []
    small_screen = Screen(width, height)
    instructions = [Instruct(instruction) for instruction in instruction_list]
    for step in instructions:
        small_screen.execute(step)
    for char in range(width // 5):
        code.append(OCR[small_screen.show_char(char)])
    return ''.join(code)


print("Star 1: ", star1(INPUT, 50, 6))
print("Star 2: ", star2(INPUT, 50, 6))
