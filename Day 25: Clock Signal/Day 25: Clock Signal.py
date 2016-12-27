#!/usr/local/bin/python3
from collections import defaultdict
import time

def read_instructions(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content


class BunnyAntenna():
    def __init__(self, instruction_list):
        self.a_init = 0
        self.instruction_list = [ instruction.split() for instruction in instruction_list ]
        self.program_counter = 0
        self.registers = defaultdict(int)
        self.__instr_set = {
            'cpy': self.__cpy,
            'inc': self.__inc,
            'dec': self.__dec,
            'jnz': self.__jnz,
            'out': self.__out
        }
        self.stdout = []

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

    def __out(self, x):
        self.stdout.append(self.registers['b'])

    def __is_repeating(self, sample_len):
        if len(self.stdout) > sample_len:
            if (sum(self.stdout[::2]) == 0 and sum(self.stdout[1::2]) == sample_len/2):
                return True
            else:
                self.__reset()
                self.a_init += 1
                self.registers['a'] = str(self.a_init)
        return False

    def __reset(self):
        self.program_counter = 0
        self.registers = defaultdict(int)
        self.stdout = []

    def __execute(self):
        instruction_register = self.instruction_list[self.program_counter]
        self.program_counter += 1
        self.__instr_set[instruction_register[0]](*instruction_register[1:])

    def run(self):
        while not self.__is_repeating(10):
            self.__execute()


def star1(safe_instuction_list):
    ba = BunnyAntenna(safe_instuction_list)
    ba.run()
    return ba.a_init


if __name__ == '__main__':
    INPUT = read_instructions('./input')
    print("Star 1: ", star1(INPUT))







