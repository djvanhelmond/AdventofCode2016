#!/usr/local/bin/python3

def expand(data):
    in_data = list(data)
    out_data = []
    while len(in_data) != 0:
        char = in_data.pop(0)
        if char != "(":
            out_data.append(char)
        else:
            marker = []
            rep_sec = []
            while in_data[0] != ")":
                marker.append(in_data.pop(0))
            in_data.pop(0)
            a, b = ''.join(marker).split('x')
            for _ in range(0, int(a)):
                rep_sec.append(in_data.pop(0))
            for _ in range(0, int(b)):
                out_data.extend(rep_sec)
    return ''.join(out_data)


INPUT = "ADVENT"
assert expand(INPUT) == "ADVENT"
assert len(expand(INPUT)) == 6

INPUT = "A(1x5)BC"
assert expand(INPUT) == "ABBBBBC"
assert len(expand(INPUT)) == 7

INPUT = "(3x3)XYZ"
assert expand(INPUT) == "XYZXYZXYZ"
assert len(expand(INPUT)) == 9

INPUT = "A(2x2)BCD(2x2)EFG"
assert expand(INPUT) == "ABCBCDEFEFG"
assert len(expand(INPUT)) == 11

INPUT = "(6x1)(1x3)A"
assert expand(INPUT) == "(1x3)A"
assert len(expand(INPUT)) == 6

INPUT = "X(8x2)(3x3)ABCY"
assert expand(INPUT) == "X(3x3)ABC(3x3)ABCY"
assert len(expand(INPUT)) == 18


def read_input_moves(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = (read_input_moves('./input'))

print("Star 1: ", len(expand(INPUT[0])))







