#!/usr/local/bin/python3
from collections import defaultdict

def read_input_file(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = read_input_file('./input')


class Firewall():
    def __init__(self, rule_list):
        self.rule_list = [ (int(rule.split("-")[0]),int(rule.split("-")[1]))  for rule in rule_list ]
        self.rule_list.sort()

    def lowest_free(self):
        lowest = 0
        find_low = list(self.rule_list)
        while len(find_low) != 0:
            range = find_low.pop(0)
            if range[0] <= lowest + 1:
                if range[1] >= lowest + 1:
                    lowest = range[1]
            else:
                return lowest + 1

    def total_address(self):
        total = 0
        address = 0
        index = 0
        while address < 4294967296:
            low, high = self.rule_list[index]
            if address >= low:
                if address <= high:
                    address = high + 1
                else:
                    index += 1
            else:
                total += 1
                address += 1
        return total


if __name__ == '__main__':
    fw = Firewall(INPUT)
    print("Star 1: ", fw.lowest_free())
    print("Star 2: ", fw.total_address())









