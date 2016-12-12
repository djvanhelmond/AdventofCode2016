#!/usr/local/bin/python3
from collections import OrderedDict

def read_instructions(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content


class Computer():
    def __init__(self, instruction_list):
        self.instruction_list = instruction_list
        self.instruction_register = 0
        self.registers = OrderedDict()
        self.registers["a"] = 0
        self.registers["b"] = 0
        self.registers["c"] = 0
        self.registers["d"] = 0

    def cpy(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        self.registers[y] = int(x)

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def jnz(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        if int(x) != 0:
            self.instruction_register += int(y) - 1

    def execute(self):
        inst = self.instruction_list[self.instruction_register].split()
        self.instruction_register += 1
        if inst[0] == "cpy":
            self.cpy(inst[1], inst[2])
        if inst[0] == "inc":
            self.inc(inst[1])
        if inst[0] == "dec":
            self.dec(inst[1])
        if inst[0] == "jnz":
            self.jnz(inst[1], inst[2])

    def run(self):
        while self.instruction_register < len(self.instruction_list):
            self.execute()


INPUT = read_instructions('./input')

def star1(inst_list):
    monorail = Computer(inst_list)
    monorail.run()
    return monorail.registers["a"]

def star2(inst_list):
    monorail = Computer(inst_list)
    monorail.registers["c"] = 1
    monorail.run()
    return monorail.registers["a"]


print("Star 1: ", star1(INPUT))
print("Star 2: ", star2(INPUT))









