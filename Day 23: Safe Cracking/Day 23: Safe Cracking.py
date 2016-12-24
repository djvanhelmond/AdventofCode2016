#!/usr/local/bin/python3
from collections import defaultdict

def read_instructions(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content


class HiddenSafe():
    def __init__(self, instruction_list):
        self.instruction_list = [ instruction.split() for instruction in instruction_list ]
        self.program_counter = 0
        self.registers = defaultdict(int)
        self.__instr_set = {
            'cpy': self.__cpy,
            'inc': self.__inc,
            'dec': self.__dec,
            'jnz': self.__jnz,
            'tgl': self.__tgl
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
        if y.isalpha():
            y = self.registers[y]
        if int(x) != 0:
            self.program_counter += int(y) - 1

    def __tgl(self, x):
        if x.isalpha():
            x = self.registers[x]
        toggle_pc = self.program_counter + int(x) - 1
        if (0 <= toggle_pc < (len(self.instruction_list) -1 )):
            if self.instruction_list[toggle_pc][0] == "inc":
                self.instruction_list[toggle_pc][0] = "dec"
            elif self.instruction_list[toggle_pc][0] == "dec":
                self.instruction_list[toggle_pc][0] = "inc"
            elif self.instruction_list[toggle_pc][0] == "tgl":
                self.instruction_list[toggle_pc][0] = "inc"
            elif self.instruction_list[toggle_pc][0] == "cpy":
                self.instruction_list[toggle_pc][0] = "jnz"
            elif self.instruction_list[toggle_pc][0] == "jnz":
                self.instruction_list[toggle_pc][0] = "cpy"

    def __execute(self):
        instruction_register = self.instruction_list[self.program_counter]
        self.program_counter += 1
        self.__instr_set[instruction_register[0]](*instruction_register[1:])

    def run(self):
        while self.program_counter < len(self.instruction_list):
            self.__execute()


def star1(safe_instuction_list):
    safe_behind_a_painting = HiddenSafe(safe_instuction_list)
    safe_behind_a_painting.registers["a"] = 7
    safe_behind_a_painting.run()
    return safe_behind_a_painting.registers["a"]

def star2(safe_instuction_list):
    return False


if __name__ == '__main__':
    INPUT = read_instructions('./input')
    print("Star 1: ", star1(INPUT))
#    print("Star 2: ", star2(INPUT))







