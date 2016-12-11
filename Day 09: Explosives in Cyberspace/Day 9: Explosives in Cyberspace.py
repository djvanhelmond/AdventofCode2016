#!/usr/local/bin/python3


def star1(data):
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
    return len(''.join(out_data))


def star2(data):
    in_data = list(data)
    data_length = 0
    while len(in_data) != 0:
        char = in_data.pop(0)
        if char != "(":
            data_length = data_length + 1
        else:
            marker = []
            rep_sec = []
            while in_data[0] != ")":
                marker.append(in_data.pop(0))
            in_data.pop(0)
            a, b = ''.join(marker).split('x')
            for _ in range(0, int(a)):
                rep_sec.append(in_data.pop(0))
            data_length = data_length + (star2(rep_sec) * int(b))
    return data_length


def read_input_moves(filename):
    content = []
    with open(filename) as input_file:
        for lines in input_file:
            content.append(lines)
    return content
INPUT = (read_input_moves('./input'))

print("Star 1: ", star1(INPUT[0]))
print("Star 2: ", star2(INPUT[0]))


