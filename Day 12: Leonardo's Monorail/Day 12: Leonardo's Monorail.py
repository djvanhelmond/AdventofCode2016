#!/usr/local/bin/python3
from collections import OrderedDict

def read_instructions(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content


class BunnyComputer():
    def __init__(self, instruction_list):
        self.instruction_list = instruction_list
        self.program_counter = 0
        self.registers = OrderedDict()
        self.registers["a"] = 0
        self.registers["b"] = 0
        self.registers["c"] = 0
        self.registers["d"] = 0
        self.__instr_set = {
            'cpy': self.__cpy,
            'inc': self.__inc,
            'dec': self.__dec,
            'jnz': self.__jnz
        }

    def __cpy(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        self.registers[y] = int(x)

    def __inc(self, x):
        self.registers[x] += 1

    def __dec(self, x):
        self.registers[x] -= 1

    def __jnz(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        if int(x) != 0:
            self.program_counter += int(y) - 1

    def __execute(self):
        instruction_register = self.instruction_list[self.program_counter].split()
        self.program_counter += 1
        self.__instr_set[instruction_register[0]](*instruction_register[1:])

    def run(self):
        while self.program_counter < len(self.instruction_list):
            self.__execute()


def star1(inst_list):
    monorail = BunnyComputer(inst_list)
    monorail.run()
    return monorail.registers["a"]

def star2(inst_list):
    monorail = BunnyComputer(inst_list)
    monorail.registers["c"] = 1
    monorail.run()
    return monorail.registers["a"]


if __name__ == '__main__':
    INPUT = read_instructions('./input')
    print("Star 1: ", star1(INPUT))
    print("Star 2: ", star2(INPUT))









